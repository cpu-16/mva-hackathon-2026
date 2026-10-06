#!/usr/bin/env python3
"""Comprueba que las cifras de los entregables siguen coincidiendo con sus archivos de resultados.

No es un buscador de palabras. Cada comprobacion:

  1. calcula el valor VERDADERO leyendo el JSON/TSV del que salio el numero, y
  2. extrae el numero que el documento afirma, con una regex anclada al texto, y
  3. los compara.

Falla si el documento cambia, si el dato cambia, o si dejan de coincidir. Un cambio de
redaccion que borre el ancla tambien falla, a proposito: una afirmacion que ya no se puede
localizar no se puede verificar.

Uso:
    python3 analysis/verificar_afirmaciones.py                 # fuentes markdown
    python3 analysis/verificar_afirmaciones.py --paquete       # ademas, los PDF renderizados
    python3 analysis/verificar_afirmaciones.py --control-negativo

El control negativo altera un numero en una COPIA temporal y exige que la verificacion falle.
Si pasara, la verificacion no sirve.

Salida: exit 0 si todo cuadra, exit 1 si no. No toca ningun archivo del proyecto.

ponytail: sin framework de tests, sin fixtures. Un diccionario de hechos y una lista de anclas.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------- rutas

# El proyecto vive en dos carpetas con la misma informacion y distinto nombre de archivo.
# CARPETA DE ANALISIS (con datos del paciente) y REPO (sin ellos).
LAYOUTS = {
    "analisis": {
        "T1": "entrega/methods_track1.md",
        "T2": "track2/REPORT_track2_EN.md",
        "M2": "entrega/methods_track2.md",
        "PDF1": "entrega/listo-para-enviar/ciberpty_track1_report.pdf",
        "PDF2": "entrega/listo-para-enviar/ciberpty_track2_report.pdf",
    },
    "repo": {
        "T1": "submission/ciberpty_track1_report.md",
        "T2": "report/REPORT_track2_EN.md",
        "M2": "submission/ciberpty_track2_methods.md",
        "PDF1": "submission/ciberpty_track1_report.pdf",
        "PDF2": "submission/ciberpty_track2_report.pdf",
    },
}

# Los datos crudos solo existen en la carpeta de analisis.
DATOS = Path("/home/gar16/datos/HACKATHON-MVA-2026")


# ---------------------------------------------------------------- hechos

def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def top_row(tsv: Path) -> tuple[str, float]:
    """Gen y score combinado de la primera fila de un .genes.tsv de Exomiser."""
    with tsv.open(encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        fields = fh.readline().rstrip("\n").split("\t")
    gene = fields[header.index("GENE_SYMBOL")]
    score = float(fields[header.index("EXOMISER_GENE_COMBINED_SCORE")])
    return gene, score


def hechos(datos: Path) -> dict:
    """Todo numero verificable, recalculado desde su archivo fuente."""
    h: dict = {}

    # --- control HPO limpio (r9), tres fondos GIAB
    r9 = [_json(datos / f"replay/out_r9/BUB1B_{s}_r9.json") for s in ("HG001", "HG002", "HG005")]
    scores = {round(j["unrelated"]["score"], 4) for j in r9}
    deltas = {round(j["delta_phenotype_abs"], 4) for j in r9}
    plantados = {round(j["planted"]["score"], 4) for j in r9}
    assert len(scores) == 1, f"el score r9 no es identico en los tres fondos: {scores}"
    assert len(deltas) == 1, f"el delta r9 no es identico en los tres fondos: {deltas}"
    assert len(plantados) == 1, f"el score plantado no es identico: {plantados}"
    h["hpo_r9_score"] = scores.pop()
    h["hpo_r9_delta"] = deltas.pop()
    h["score_referencia"] = plantados.pop()
    h["hpo_r9_ranks"] = [j["unrelated"]["gene_rank"] for j in r9]
    h["hpo_r9_rank1_de_3"] = sum(1 for r in h["hpo_r9_ranks"] if r == 1)

    # --- tier de 30 fondos 1000G
    tsvs = sorted((datos / "replay/out").glob("A1k_*_real.genes.tsv"))
    tops = [(t.name.split("_")[1], *top_row(t)) for t in tsvs]
    muestra, gen, maximo = max(tops, key=lambda x: x[2])
    h["tier1k_n"] = len(tops)
    h["tier1k_max"] = round(maximo, 4)
    h["tier1k_gen"] = gen
    h["tier1k_muestra"] = muestra
    h["tier1k_por_encima"] = sum(1 for _, _, s in tops if s > h["score_referencia"])

    # --- potencia. Sin redondear: la tolerancia la fija el numero de decimales del documento.
    pot = _json(datos / "potencia/resultados.json")
    h["potencia_central"] = pot["power_central"]
    h["potencia_f002"] = pot["sweeps"]["f"]["0.02"]
    h["potencia_r2"] = pot["sweeps"]["r"]["2.0"]
    h["potencia_r_central"] = pot["central_params"]["r"]
    h["potencia_f_central"] = pot["central_params"]["f"]
    # --- potencia, modelo de cuatro parametros (seguimiento pre-registrado del 8-sep)
    p4 = _json(datos / "potencia/resultados_4p.json")
    h["potencia4p_central"] = p4["central"]["power"]
    h["potencia4p_2p_mismos_datos"] = p4["central"]["power_2p_same_data"]
    h["potencia4p_n80_f030"] = p4["n_for_80"]["0.3"]
    h["potencia4p_n80_f020"] = p4["n_for_80"]["0.2"]

    # --- dosis (la correccion del 6-sep depende de esto)
    dos = _json(datos / "potencia/dosis.json")
    sol, hem = dos["strata"]["solid"], dos["strata"]["haematological"]
    h["dosis_solido_ci_cubre_cero"] = sol["ci95"][0] < 0 < sol["ci95"][1]
    h["dosis_hem_ratio2"] = hem["ratio_2"]
    h["dosis_hem_ratio18"] = hem["ratio_18"]
    # La regla pre-registrada se fijo en SOLIDOS. Si algun dia el IC de solidos dejara de
    # cubrir cero, la redaccion del 6-sep habria que rehacerla: se avisa aqui.
    assert h["dosis_solido_ci_cubre_cero"], (
        "el IC de solidos ya NO cubre cero: la clausula de falsificacion deja de aplicar y "
        "toda la redaccion de potencia del 6-sep hay que revisarla")

    # --- mosaicismo: el LOD calibrado sale de la ventana elegida, no del MC generico
    ven = _json(datos / "mosaico/ventana.json")
    fila = next(f for f in ven["filas"] if f["W"] == ven["W_elegida"])
    h["lod_k1"] = fila["lod_k1"] * 100
    h["lod_k2"] = fila["lod_k2"] * 100
    h["lod_k4"] = fila["lod_k4"] * 100
    h["control_no_concluyente"] = _json(
        datos / "mosaico/control_resultado.json")["verdict"].startswith("NO CONCLUYENTE")

    # --- censo ClinVar del VUS
    cen = _json(datos / "vus/censo.json")["clinvar"]
    h["clinvar_missense"] = cen["missense"]["total"]
    h["clinvar_missense_plp"] = cen["missense"]["P/LP"]
    h["clinvar_missense_vus"] = cen["missense"]["VUS"]
    h["clinvar_lof_plp"] = cen["lof"]["P/LP"]
    h["clinvar_lof"] = cen["lof"]["total"]
    return h


# ---------------------------------------------------------------- anclas
#
# (documento, regex, [claves esperadas en orden de los grupos de captura])
# El texto se normaliza (espacios colapsados) antes de aplicar la regex, asi que
# los saltos de linea del markdown no importan.

ANCLAS = [
    ("T1", r"score (\d+(?:\.\d+)?) on the dominant row", ["hpo_r9_score"]),
    ("T1", r"Δ = (\d+(?:\.\d+)?)\*\*, and both values", ["hpo_r9_delta"]),
    ("T1", r"phenotype moves the score by \*\*(\d+(?:\.\d+)?)\*\*", ["hpo_r9_delta"]),
    ("T1", r"maximum top-gene combined score of \*\*(\d+(?:\.\d+)?) \((\w+), (\w+)\)\*\*",
     ["tier1k_max", "tier1k_gen", "tier1k_muestra"]),
    ("T1", r"\*\*0 of (\d+) exceeding (\d+(?:\.\d+)?)\*\*", ["tier1k_n", "score_referencia"]),
    ("T1", r"maximum \*\*(\d+(?:\.\d+)?) \((\w+), (\w+)\)\*\*, \*\*0 of (\d+)\*\* above (\d+(?:\.\d+)?)",
     ["tier1k_max", "tier1k_gen", "tier1k_muestra", "tier1k_n", "score_referencia"]),
    ("T1", r"0 of 7 GIAB and 0 of (\d+) 1000G", ["tier1k_n"]),
    ("T2", r"Read (\d+(?:\.\d+)?) as an idealised scenario", ["potencia_central"]),
    ("T2", r"n = 3 per\s+arm\) \*\*power is (\d+(?:\.\d+)?)\*\*\. The two-parameter fit on the same simulated data gives (\d+(?:\.\d+)?)",
     ["potencia4p_central", "potencia4p_2p_mismos_datos"]),
    ("T2", r"first crosses 0\.80 at \*\*n = (\d+) independent cultures per arm at f = 0\.30\*\*, \*\*n = (\d+) at\s+f = 0\.20\*\*",
     ["potencia4p_n80_f030", "potencia4p_n80_f020"]),
    ("T2", r"\*\*(\d+(?:\.\d+)?)% of cells at an overdispersion κ = 2\*\*", ["lod_k2"]),
    ("T2", r"and (\d+(?:\.\d+)?)% at κ = 1, (\d+(?:\.\d+)?)% at κ = 4", ["lod_k1", "lod_k4"]),
    ("T2", r"\*\*(\d+(?:\.\d+)?) residual SD at two arms against (\d+(?:\.\d+)?) at eighteen\*\*",
     ["dosis_hem_ratio2", "dosis_hem_ratio18"]),
    ("T2", r"this gene carries \*\*([\d,]+) missense records", ["clinvar_missense"]),
    ("T2", r"\*\*(\d+) of its (\d+) truncating records are Pathogenic",
     ["clinvar_lof_plp", "clinvar_lof"]),
    ("M2", r"\*\*(\d+(?:\.\d+)?)% at an overdispersion κ = 2\*\*", ["lod_k2"]),
]

# Afirmaciones retiradas. Si vuelven a aparecer, es que un documento retrocedio de version.
PROHIBIDAS = [
    ("T1", "0.4187 with five verified-unrelated terms", "control HPO contaminado como si fuera limpio"),
    ("T1", "still running at the time of writing", "el tier de 30 genomas ya termino"),
    ("T1", "five are confirmed, one is still open", "recuento de predicciones desactualizado"),
    ("T2", "through AMPK. 2013. PMID 22890317", "titulo falso de la referencia 22"),
    ("T2", "about twelve weeks", "el cronograma honesto es 12-16 semanas"),
    ("T2", "every candidate the scientific literature points to", "exhaustividad no sostenible"),
    ("T2", "no BAM, hence no GC-LOESS", "el reto si distribuye las lecturas"),
    ("T2", "it is the only practical one", "hay otras vias, mas caras"),
    ("T2", "The 4× central scenario is therefore not defensible",
     "la regla pre-registrada era para solidos y no disparo"),
    ("T2", "That check was not ceremonial", "el filtro fue RepeatMasker, no el conteo"),
    ("M2", "7–16× below it", "el limite calibrado invierte esa lectura"),
]


def normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", texto)


def comparar(afirmado: str, verdadero) -> bool:
    afirmado = afirmado.replace(",", "")
    if isinstance(verdadero, str):
        return afirmado == verdadero
    try:
        v = float(afirmado)
    except ValueError:
        return False
    # Tolerancia = media unidad del ultimo decimal que el documento escribe, con un margen
    # minimo para el redondeo binario. Un digito equivocado nunca cae dentro.
    decimales = len(afirmado.split(".")[1]) if "." in afirmado else 0
    return abs(v - float(verdadero)) <= 0.51 * 10 ** (-decimales)


def verificar(raiz: Path, layout: dict, h: dict, textos: dict) -> list[str]:
    fallos = []
    for doc, patron, claves in ANCLAS:
        if doc not in textos:
            continue
        m = re.search(patron, textos[doc])
        if not m:
            fallos.append(f"{layout[doc]}: no se encuentra el ancla /{patron}/ "
                          f"(la afirmacion se reescribio o desaparecio)")
            continue
        for i, clave in enumerate(claves, start=1):
            if not comparar(m.group(i), h[clave]):
                fallos.append(f"{layout[doc]}: el documento dice {m.group(i)!r} donde "
                              f"{clave} vale {h[clave]!r}  [ancla /{patron}/]")
    for doc, frase, motivo in PROHIBIDAS:
        if doc in textos and normalizar(frase) in textos[doc]:
            fallos.append(f"{layout[doc]}: reaparecio una afirmacion retirada "
                          f"({frase!r}) — {motivo}")
    return fallos


def cargar_textos(raiz: Path, layout: dict, claves) -> dict:
    out = {}
    for k in claves:
        p = raiz / layout[k]
        if p.exists():
            out[k] = normalizar(p.read_text(encoding="utf-8"))
        else:
            print(f"  aviso: falta {p}, se omite")
    return out


def texto_pdf(pdf: Path) -> str:
    salida = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                            capture_output=True, text=True, check=True)
    return normalizar(salida.stdout)


def coherencia_entre_copias(h: dict) -> list[str]:
    """La carpeta de analisis y el repo deben tener los mismos markdown."""
    fallos = []
    for k in ("T1", "T2", "M2"):
        a = DATOS / LAYOUTS["analisis"][k]
        b = Path("/home/gar16/datos/mva-hackathon-2026") / LAYOUTS["repo"][k]
        if a.exists() and b.exists() and a.read_bytes() != b.read_bytes():
            fallos.append(f"desincronizado: {a} != {b}")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=str(DATOS))
    ap.add_argument("--layout", choices=list(LAYOUTS), default="analisis")
    ap.add_argument("--paquete", action="store_true",
                    help="verificar tambien los PDF renderizados")
    ap.add_argument("--control-negativo", action="store_true",
                    help="alterar un numero en una copia y exigir que la verificacion falle")
    args = ap.parse_args()

    raiz, layout = Path(args.raiz), LAYOUTS[args.layout]
    h = hechos(DATOS)
    print(f"hechos recalculados desde los archivos de resultados: {len(h)}")

    textos = cargar_textos(raiz, layout, ("T1", "T2", "M2"))
    fallos = verificar(raiz, layout, h, textos)
    fallos += coherencia_entre_copias(h)

    if args.paquete:
        for k, fuente in (("PDF1", "T1"), ("PDF2", "T2")):
            pdf = raiz / layout[k]
            if not pdf.exists():
                fallos.append(f"falta el PDF {pdf}")
                continue
            t = texto_pdf(pdf)
            # Al PDF se le aplican las mismas anclas que a su markdown fuente, salvo el
            # marcado de negritas, que pandoc no conserva.
            for doc, patron, claves in ANCLAS:
                if doc != fuente:
                    continue
                limpio = patron.replace(r"\*\*", "")
                m = re.search(limpio, t)
                if not m:
                    fallos.append(f"{pdf.name}: el PDF no contiene /{limpio}/ — "
                                  f"probablemente esta sin regenerar")
                    continue
                for i, clave in enumerate(claves, start=1):
                    if not comparar(m.group(i), h[clave]):
                        fallos.append(f"{pdf.name}: dice {m.group(i)!r}, "
                                      f"{clave} vale {h[clave]!r}")
            for doc, frase, motivo in PROHIBIDAS:
                if doc == fuente and normalizar(frase) in t:
                    fallos.append(f"{pdf.name}: afirmacion retirada presente ({frase!r}) — {motivo}")

    if args.control_negativo:
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            for k in ("T1", "T2", "M2"):
                dst = tmp / layout[k]
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(raiz / layout[k], dst)
            # Alteramos el score del control HPO en la COPIA: 0.3965 -> 0.3966.
            p = tmp / layout["T1"]
            p.write_text(p.read_text(encoding="utf-8").replace("0.3965", "0.3966"),
                         encoding="utf-8")
            copia = cargar_textos(tmp, layout, ("T1", "T2", "M2"))
            detectados = verificar(tmp, layout, h, copia)
            if detectados:
                print(f"\ncontrol negativo OK: la copia alterada produce {len(detectados)} fallo(s)")
                print(f"  ejemplo: {detectados[0]}")
            else:
                fallos.append("CONTROL NEGATIVO FALLIDO: se altero 0.3965 -> 0.3966 en una copia "
                              "y la verificacion no lo detecto. La verificacion no sirve.")

    if fallos:
        print(f"\n{len(fallos)} DISCREPANCIA(S):")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print("\ntodo cuadra")
    return 0


if __name__ == "__main__":
    sys.exit(main())
