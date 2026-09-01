#!/usr/bin/env python3
"""Comprueba que cada secuencia y coordenada de la orden clínica sale del JSON verificado.

Existe porque el error más frecuente de este proyecto no ha sido un cálculo malo sino un
número bien calculado y mal copiado al documento. Un primer con una base cambiada no falla
en ninguna revisión de prosa: falla en el laboratorio.

Control positivo incluido: --demo corrompe una base y comprueba que el chequeo dispara.
"""
import json, re, sys

DOC = "clinico/PARENTAL_SEGREGATION_ORDER.md"
JSON = "clinico/primers_finales.json"


def check(text, data):
    """Devuelve la lista de fallos. Vacía = el documento coincide con el diseño verificado."""
    fails = []
    for d in data:
        p, t = d["chosen"], d["target"]
        for side in ("left", "right"):
            if f"`{p[side]}`" not in text:
                fails.append(f"{t['name']}: primer {side} {p[side]} no aparece en el documento")
            if p[f"{side}_copies"] != 1:
                fails.append(f"{t['name']}: primer {side} no es de copia única")
        start, end = p["amplicon"].split(":")[1].split("-")
        pretty = f"chr15:{int(start):,}–{int(end):,}".replace(",", ",")
        if pretty not in text:
            fails.append(f"{t['name']}: amplicón {pretty} no aparece en el documento")
        if f"{p['product']} bp" not in text:
            fails.append(f"{t['name']}: tamaño {p['product']} bp no aparece en el documento")
        for side, lbl in (("left", "F"), ("right", "R")):
            if f"{p[side + '_tm']} °C" not in text:
                fails.append(f"{t['name']}: Tm {p[side + '_tm']} ({lbl}) no aparece")
        if f"{p['margin_fwd']} nt from F" not in text:
            fails.append(f"{t['name']}: margen F {p['margin_fwd']} no aparece")
        if f"{p['margin_rev']} nt from R" not in text:
            fails.append(f"{t['name']}: margen R {p['margin_rev']} no aparece")
        # las coordenadas de las variantes, con separador de miles
        pos = f"chr15:{t['pos']:,}".replace(",", ",")
        if pos not in text:
            fails.append(f"{t['name']}: posición {pos} no aparece")
    return fails


def main():
    data = json.load(open(JSON))
    text = open(DOC).read()

    if "--demo" in sys.argv:
        # control positivo: una sola base cambiada debe hacer fallar el chequeo
        seq0 = data[0]["chosen"]["left"]
        mutated = seq0[:-1] + ("C" if seq0[-1] != "C" else "G")   # siempre una base DISTINTA
        assert mutated != seq0
        broken = text.replace(f"`{seq0}`", f"`{mutated}`", 1)
        assert broken != text, "el reemplazo no cambió nada: el primer no está en el documento"
        assert check(broken, data), "el chequeo NO detectó un primer corrompido — es inútil"
        broken2 = text.replace(f"{data[0]['chosen']['product']} bp", "999 bp", 1)
        assert check(broken2, data), "el chequeo NO detectó un tamaño corrompido — es inútil"
        print("control positivo: el chequeo dispara con un primer y con un tamaño corrompidos")

    fails = check(text, data)
    for f in fails:
        print("FALLO:", f)
    n = sum(2 + 2 + 2 + 3 for _ in data)
    print(f"{'OK' if not fails else 'HAY FALLOS'}: {n} comprobaciones sobre {len(data)} amplicones, "
          f"{len(fails)} discrepancias")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
