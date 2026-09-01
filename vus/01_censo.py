#!/usr/bin/env python3
"""Why p.Asn1002Lys cannot be resolved from databases: a census of BUB1B in ClinVar,
plus the structural environment of the residue.

This is a CENSUS, not a hypothesis test. It carries no pre-registration because there is no
decision rule to fix in advance: it counts what ClinVar holds on a given date and measures a
property of a published structure. What it does carry is the exact snapshot and command, so the
count can be reproduced or refuted.
"""
import json, re, subprocess, statistics as st

CLINVAR = "pipeline/resources/clinvar.vcf.gz"
REGION = "15:40160000-40280000"       # BUB1B locus with margin
AF_PDB = "vus/AF-O60566-F1-model_v6.pdb"
KINASE = (766, 1050)                  # UniProt O60566 "Protein kinase" domain
N1002, L737 = 1002, 737


def clinvar_census():
    out = subprocess.run(["bcftools", "view", "-H", "-r", REGION, CLINVAR],
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        f = line.split("\t")
        info = f[7]
        if "GENEINFO=BUB1B" not in info:
            continue
        get = lambda k: (re.search(k + r"=([^;]+)", info) or [None, ""])[1]
        rows.append(dict(pos=int(f[1]), vid=f[2], sig=get("CLNSIG"),
                         rev=get("CLNREVSTAT"), mc=get("MC")))

    def bucket(r):
        s = r["sig"]
        if s.startswith(("Pathogenic", "Likely_pathogenic")):
            return "P/LP"
        if s.startswith(("Benign", "Likely_benign")):
            return "B/LB"
        if s.startswith("Uncertain"):
            return "VUS"
        return "other"

    mis = [r for r in rows if "missense" in r["mc"]]
    lof = [r for r in rows if any(t in r["mc"] for t in ("nonsense", "frameshift", "splice"))]
    res = dict(
        total=len(rows),
        missense=dict(total=len(mis),
                      **{k: sum(1 for r in mis if bucket(r) == k) for k in ("P/LP", "B/LB", "VUS", "other")}),
        lof=dict(total=len(lof),
                 **{k: sum(1 for r in lof if bucket(r) == k) for k in ("P/LP", "B/LB", "VUS", "other")}),
        missense_plp_detail=[dict(pos=r["pos"], id=r["vid"], sig=r["sig"], rev=r["rev"])
                             for r in mis if bucket(r) == "P/LP"],
    )
    res["missense"]["pct_vus"] = 100.0 * res["missense"]["VUS"] / max(res["missense"]["total"], 1)
    return res


def structure():
    """pLDDT and relative solvent accessibility around the two variant sites."""
    from Bio.PDB import PDBParser
    from Bio.PDB.SASA import ShrakeRupley
    # Tien et al. 2013 theoretical maxima, the standard denominator for RSA
    MAXASA = dict(A=129, R=274, N=195, D=193, C=167, E=223, Q=225, G=104, H=224, I=197,
                  L=201, K=236, M=224, F=240, P=159, S=155, T=172, W=285, Y=263, V=174)
    THREE = dict(ALA="A", ARG="R", ASN="N", ASP="D", CYS="C", GLU="E", GLN="Q", GLY="G",
                 HIS="H", ILE="I", LEU="L", LYS="K", MET="M", PHE="F", PRO="P", SER="S",
                 THR="T", TRP="W", TYR="Y", VAL="V")

    s = PDBParser(QUIET=True).get_structure("bub1b", AF_PDB)
    ShrakeRupley().compute(s, level="R")
    info = {}
    plddt = {}
    for r in s.get_residues():
        i = r.id[1]
        aa = THREE.get(r.get_resname(), "X")
        b = [a.get_bfactor() for a in r]
        plddt[i] = st.mean(b)
        info[i] = dict(aa=aa, rsa=r.sasa / MAXASA.get(aa, 200), plddt=st.mean(b))

    def span(a, b):
        v = [plddt[i] for i in range(a, b + 1) if i in plddt]
        return dict(n=len(v), mean_plddt=round(st.mean(v), 1), min_plddt=round(min(v), 1))

    # residues in contact with N1002 (any heavy atom within 5 A of any N1002 heavy atom)
    target = [r for r in s.get_residues() if r.id[1] == N1002][0]
    contacts = []
    for r in s.get_residues():
        if r.id[1] == N1002:
            continue
        d = min((a - b for a in target for b in r), default=99)
        if d <= 5.0:
            contacts.append(dict(res=int(r.id[1]), aa=THREE.get(r.get_resname(), "X"), dist=round(float(d), 2)))
    contacts.sort(key=lambda x: x["dist"])

    return dict(
        kinase_domain=span(*KINASE),
        whole_protein=span(1, max(plddt)),
        n1002=dict(**info[N1002], buried=bool(info[N1002]["rsa"] < 0.25)),
        l737=dict(**info[L737]),
        neighbourhood_992_1012=span(992, 1012),
        contacts_within_5A=contacts,
        residues_after_737=max(plddt) - L737,
    )


def main():
    cv = clinvar_census()
    stx = structure()
    out = dict(clinvar=cv, structure=stx)
    json.dump(out, open("vus/censo.json", "w"), indent=2)

    m = cv["missense"]
    print("=== ClinVar, gen BUB1B ===")
    print(f"  registros totales      {cv['total']}")
    print(f"  missense               {m['total']}")
    print(f"     P/LP                {m['P/LP']}   <-- con cuantos positivos se calibraria un predictor")
    print(f"     B/LB                {m['B/LB']}")
    print(f"     VUS                 {m['VUS']}  ({m['pct_vus']:.1f}% de las missense)")
    print(f"  perdida de funcion     {cv['lof']['total']}  de las cuales P/LP: {cv['lof']['P/LP']}")
    for d in cv["missense_plp_detail"]:
        print(f"     la unica P/LP: pos {d['pos']} id {d['id']} {d['sig']} [{d['rev']}]")

    s = stx
    print("\n=== Estructura AlphaFold (AF-O60566-F1-v6) ===")
    print(f"  dominio kinase 766-1050  pLDDT medio {s['kinase_domain']['mean_plddt']}")
    print(f"  entorno 992-1012         pLDDT medio {s['neighbourhood_992_1012']['mean_plddt']}")
    print(f"  Asn1002                  pLDDT {s['n1002']['plddt']:.1f}  RSA {s['n1002']['rsa']:.3f}"
          f"  {'ENTERRADO' if s['n1002']['buried'] else 'expuesto'}")
    print(f"  Leu737 (sitio nonsense)  pLDDT {s['l737']['plddt']:.1f}  RSA {s['l737']['rsa']:.3f}")
    print(f"  residuos perdidos tras el nonsense: {s['residues_after_737']}")
    print(f"  contactos <5 A de Asn1002: {len(s['contacts_within_5A'])}")
    print("     " + ", ".join(f"{c['aa']}{c['res']}({c['dist']})" for c in s["contacts_within_5A"][:8]))
    print("\nescrito vus/censo.json")


if __name__ == "__main__":
    main()
