#!/usr/bin/env python3
"""Verifica que un término HPO NO esté anotado a ninguna forma de MVA ni a BUB1B.

Por qué existe: el control de "HPO no relacionados" del Track 1 se ha contaminado DOS veces.
La primera, con términos anotados a MVA1 (OMIM:257300). La corrección de esa ronda verificó
sólo contra OMIM:257300 — y HP:0000365 (hipoacusia) está anotado a ORPHA:1052, el término
genérico de MVA, y a OMIM:614114 (MVA2). Exomiser puntúa por similitud sobre la ontología
entera, así que cualquier enfermedad MVA contamina el control, no sólo MVA1.

Regla: un término sirve como control sólo si NO aparece anotado a ninguna enfermedad cuyo
nombre contenga "aneuploid", ni a ninguna de las MVA por identificador, ni al gen BUB1B.
"""
import json, subprocess, sys

API = "https://ontology.jax.org/api/network/annotation/"
MVA_IDS = {"OMIM:257300", "OMIM:614114", "OMIM:617598", "ORPHA:1052"}

CANDIDATES = {
    # los cinco del control r7, el que se envió
    "HP:0000365": "Hearing impairment (control r7)",
    "HP:0000509": "Conjunctivitis (control r7)",
    "HP:0002205": "Recurrent respiratory infections (control r7)",
    "HP:0002315": "Headache (control r7)",
    "HP:0000989": "Pruritus (control r7)",
    # reemplazos candidatos, deliberadamente lejanos a un síndrome de inestabilidad cromosómica
    "HP:0001945": "Fever",
    "HP:0002018": "Nausea",
    "HP:0000961": "Cyanosis",
    "HP:0012378": "Fatigue",
    "HP:0002094": "Dyspnea",
    "HP:0000988": "Skin rash",
    "HP:0002027": "Abdominal pain",
    "HP:0000737": "Irritability",
    "HP:0031narrow": "",   # placeholder ignorado si falla
}


def fetch(term):
    raw = subprocess.run(["curl", "-s", "--max-time", "60", API + term],
                         capture_output=True, text=True).stdout
    try:
        return json.loads(raw)
    except Exception:
        return None


def main():
    out = {}
    for term, label in CANDIDATES.items():
        if not label:
            continue
        d = fetch(term)
        if d is None:
            print(f"{term:14s} {label:38s}  ERROR de consulta")
            continue
        diseases = d.get("diseases", [])
        genes = d.get("genes", [])
        bad_disease = [x for x in diseases
                       if x.get("id") in MVA_IDS or "aneuploid" in (x.get("name") or "").lower()]
        bad_gene = [g for g in genes if (g.get("name") or "").upper() in
                    {"BUB1B", "CEP57", "TRIP13"}]
        clean = not bad_disease and not bad_gene
        out[term] = dict(label=label, n_diseases=len(diseases), n_genes=len(genes),
                         mva_diseases=[x.get("id") + " " + (x.get("name") or "") for x in bad_disease],
                         mva_genes=[g.get("name") for g in bad_gene], clean=clean)
        mark = "LIMPIO " if clean else "CONTAMINADO"
        print(f"{term:14s} {label:38s} {mark}  ({len(diseases)} enfermedades, {len(genes)} genes)")
        for x in bad_disease:
            print(f"                 └─ anotado a {x.get('id')} {x.get('name')}")
        for g in bad_gene:
            print(f"                 └─ anotado al gen {g.get('name')}")

    json.dump(out, open("hpo/verificacion.json", "w"), indent=2)
    limpios = [t for t, v in out.items() if v["clean"]]
    print(f"\nTérminos limpios disponibles: {len(limpios)}")
    print("  " + " ".join(limpios))
    r7 = [t for t in ("HP:0000365", "HP:0000509", "HP:0002205", "HP:0002315", "HP:0000989")
          if t in out and not out[t]["clean"]]
    print(f"\nDel control r7 ENVIADO, contaminados: {len(r7)} -> {' '.join(r7) if r7 else 'ninguno'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
