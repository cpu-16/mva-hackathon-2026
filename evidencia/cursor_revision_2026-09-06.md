# Revisión adversarial de Cursor (Grok 4.6) — 6-sep-2026

Prompt: buscar afirmaciones de los dos reportes que **contradigan los archivos de resultados del propio
equipo**, con cita de archivo y línea. Salida íntegra abajo, sin editar.

**Verificación de esta sesión, hallazgo por hallazgo** (cada uno contra su archivo fuente, no contra el
texto de Cursor):

| Hallazgo | Veredicto | Qué se hizo |
|---|---|---|
| Alelos plantados en r9 son 533901 + la missense propia (`T>G`, ausente de ClinVar), no 4600147 (`T>A`) | ✅ real, confirmado en `replay/out_r9/*.json` | corregido en Track 1 |
| «2.27 M SNV heterocigotos» contradice los 2.927.826 de `mosaico/` | ❌ **falso positivo** — recontado del VCF: 2.274.451 SNV bialélicos autosómicos PASS. El 2,93 M cuenta *todas* las llamadas heterocigotas | se añadió la aclaración para que nadie lo lea como choque |
| «no BAM, luego no GC-LOESS» sigue vivo en Track 1 | ✅ real (nuestro `mosaico/RESULTADOS.md` lo retractó) | corregido |
| Lista de contactos a 5 Å omite Asn1004 (3,14 Å), más cercano que dos de los citados | ✅ real, confirmado en `vus/censo.json` | corregido en el reporte y en `vus/RESULTADOS.md` |
| κ del probando «≈2,3» no es el estadístico de la tabla de control (2,74 chr8 / 4,60 chr17) | ✅ real, confirmado en `control_resultado.json`. La conclusión (el más bajo) se sostiene | corregido |
| MVA2: «filtro 2» vs «filtro 4» | ✅ real, pero al revés de como lo cuenta Cursor: el reporte sigue a la hoja **corregida**; los restos de la versión vieja estaban en `TRANSFER_MVA2_MVA3.md` §5/§7 | corregido en TRANSFER |
| «dieciocho brazos» atribuido a las líneas de Ippolito | ✅ real: 18 es el extremo alto del rango DepMap (`dosis.json`), no una medida de esas líneas | corregido |
| «targets the … consequence of the underlying lesion» sin acotar | ✅ razonable | acotado a «as established in cancer cells» |
| «one shuffled-phenotype run» | ✅ real y peor de lo que dice Cursor: `tools/control_hpo.sh` corre `hpos_barajados` con los cinco términos ajenos, así que **no existe ningún control barajado** | retirado y declarado |
| Sección de mosaicismo del Track 1 anclada al 14% | ✅ real — el mismo error que ya se corrigió en el Track 2 y nunca se propagó | propagados 2,07%, no identificabilidad y la retirada |
| q = 5×10⁻⁸ vs 5,2×10⁻⁸; 85 GB vs 84,7 GB | ✅ cosméticos | corregidos |

Los números que Cursor no pudo rastrear a los archivos listados **sí tienen fuente**: están en
`mosaico/RESULTADOS.md`, `pipeline/`, `tools/results/` y `track2/DATOS_CANDIDATO.md`, que no estaban en
la lista que se le dio. No es un hallazgo, es el alcance del prompt.

---

## Contradiction

**`entrega/methods_track1.md:297–300`** — “Planting the two public ClinVar records that reproduce this case's architecture (533901 `chr15:40209701 T>G` nonsense, 4600147 `chr15:40220612 T>A` VUS missense) into three unrelated healthy genomes returns **0.5871 with the real phenotype and 0.3965 with the five clean r9 unrelated terms**”
— `replay/out_r9/BUB1B_HG001_r9.json:50–56` (same in HG002/HG005) planted `chr15:40220612:T:G` with `"clinvar_id": "absent"`, not 4600147 `T>A`. `hpo/RESULTADOS.md:85` says the r9 replay spiked “the child's two alleles”.
— **contradiction**

**`entrega/methods_track1.md:241`** — “per-chromosome B-allele frequency across 2.27 M heterozygous SNVs”
— `mosaico/RESULTADOS.md:39`: “The proband VCF supplies 2,927,826 autosomal heterozygous calls”.
— **contradiction**

**`entrega/methods_track1.md:245`** — “Only the VCF was available, with no BAM, so no GC-LOESS normalisation was possible.”
— `mosaico/RESULTADOS.md:147–149`: that sentence “is wrong twice over: the challenge distributes the raw reads, and the analysis that mattered did not need them.” `track2/REPORT_track2_EN.md:534–538` retracts it as “our choice of input, not a limit of the challenge”.
— **contradiction**

**`track2/REPORT_track2_EN.md:175–176`** — “ten residues within 5 Å and the nearest being Leu1001, Ala1003, Trp978, Val998, Ile1000 and Phe977”
— `vus/censo.json:55–90`: ten contacts, 5th-nearest is Asn1004 at 3.14 Å, closer than Ile1000 (3.33) and Phe977 (3.46). Listed six omit Asn1004, Arg999, Trp973, Phe997. (`vus/RESULTADOS.md:70–71` repeats the same omitted list; JSON disagrees.)
— **contradiction**

**`track2/REPORT_track2_EN.md:620–621`** — “against those ten genomes, window-scale overdispersion ranges from κ ≈ 6 to 46, and the proband's ≈2.3 is the **lowest in the comparison**”
— `mosaico/CONTROL_RESULTADO.md:29–33` comparison table: proband κ_window **2.74** (chr8) and **4.60** (chr17). `mosaico/control_resultado.json:16–24` and `:215–224`: chr8 raw 2.321 / used-thinned 2.740; chr17 raw 4.923 / used-thinned 4.600. The 2.27× / ≈2.3 figure is the chromosome-wide excess in `mosaico/RESULTADOS.md:109`, not the statistic in the control table.
— **contradiction**

**`track2/REPORT_track2_EN.md:921–923`** — “For **MVA2** bortezomib **fails filter 4 and cannot be evaluated at filters 2–3**”
— `track2/TRANSFER_MVA2_MVA3.md:156–157`: “kills the candidate **at filter 2** in MVA2”; `:163–164`: “MVA2 at filter 2”; `:212–213`: “both worksheets leave [filter 4] undecided (MVA2 does not reach it)”. The TRANSFER worksheet itself (`:21`, `:65`) matches the Track 2 report, not TRANSFER §5/§7.
— **contradiction**

## Overclaim

**`track2/REPORT_track2_EN.md:668–670`** — “an MVA cell carries **about one** altered chromosome where the lines that gave the < 40 nM EC50 carry on the order of eighteen altered arms”
— `potencia/RESULTADOS_2_DOSIS.md:45–46` and `potencia/dosis.json:3–4,34–37`: 2 vs 18 arms is the DepMap haematological regression (`arms_mva` / `arms_high`). That file does not assign 18 arms to Ippolito’s five highly aneuploid lines.
— **overclaim**

**`track2/REPORT_track2_EN.md:488–490`** — “an approved agent that targets the best-characterised downstream consequence of the **underlying lesion** — proteotoxic dependency — supported by a human clinical signal tying response to aneuploidy burden”
— `depmap/RESULTADOS.md:69–74` / Track 2 `§3.5` / `§10:970–972`: the dependency was not extended to solid tumours; transfer to constitutional MVA is untested. Same report `L121` restricts this to “in cancer cells”.
— **overclaim**

**`entrega/methods_track1.md:86–88`** — “**eight leave-one-HPO-out runs**, **one least-specific-term-alone run**, **one shuffled-phenotype run**”
— No shuffled result is reported. `tools/results/controles/hpos_barajados.genes.tsv` BUB1B row is 0.5506 with Seizure / hearing impairment / ASD / conjunctivitis / recurrent respiratory infections — the same five terms and score as `hpos_original_contaminado.genes.tsv` (`entrega/methods_track1.md:103`), not a shuffle of the eight clinical terms.
— **overclaim**

## Stale

**`entrega/methods_track1.md:247–274`** (mosaicism section as a whole) still presents the first-order **~14% / 16% / 20%** limit, and `L271–272` “1–2% of cells, which is 7–16× below the 14–16% detection limit”, with no calibrated LOD, no identifiability result, and no withdrawal of the proband application.
— `mosaico/RESULTADOS.md:144–145`: “The mosaicism section's ‘~14%’ is replaced by the measured **2.1%** limit and its calibration.” `track2/REPORT_track2_EN.md:551–561, 573–582, 598–625` reports 2.07% (W=125 in `mosaico/ventana.json:37–44`), 0.1–0.2% identifiability, and the withdrawn/not-conclusive proband+control outcome.
— **stale**

## Cosmetic

**`track2/REPORT_track2_EN.md:443`** — “ρ = −0.198, q = 5×10⁻⁸, n = 946”
— `depmap/RESULTADOS.md:48`: q = **5.2×10⁻⁸**.
— **cosmetic**

**`entrega/methods_track1.md:209`** vs **`track2/REPORT_track2_EN.md:147`** — missense AF **8.99×10⁻⁷** vs **9.0×10⁻⁷** (`fase/RESULTADO.md:21`: 9.0×10⁻⁷).
— **cosmetic**

**`entrega/methods_track1.md:525`** — “85 GB of raw reads” vs **`track2/REPORT_track2_EN.md:536`** — “84.7 GB of FASTQ”.
— **cosmetic**

---

## Demonstrated benefit of a drug in this child or in MVA

**Nothing in this category.** Both write-ups state no drug for this child now. The only “demonstrated benefit” phrasing is negative: `track2/REPORT_track2_EN.md:833` “no demonstrated benefit in MVA” (AFP/CT/PET/whole-body MRI). Myeloma PI response is labelled as not evidence about MVA1 (`L335–338`).

## Numbers in the reports not traced to the listed results files / JSON / TSV

These appear in the write-ups and were not in `replay/RESULTADOS.md` §9, `hpo/`, `potencia/*.json`, `mosaico/ventana.json`, `mosaico/control_resultado.json`, `vus/censo.json`, `depmap/RESULTADOS.md`, `fase/RESULTADO.md`, `TRANSFER_MVA2_MVA3.md`, or `PARENTAL_SEGREGATION_ORDER.md`:

| Number | Where |
|---|---|
| 857,435 sites; SD **0.0035**; first-order 14/16/20% | Track 1 `L248–254`; Track 2 `L544–549` |
| Exomiser cascade 4,962,047 → 4,702,177 → 277,724 → 11,255 → 9,935; 2,100 recessive rows; FANCD2 0.2137; 2.59× / 2.75× | Track 1 `L40–42, 46, 67–70` |
| 1,532 panel PASS variants; three survivors | Track 1 `L196–202` |
| LOEUF 0.588; REVEL 0.472, MVP 0.852, AlphaMissense 0.923 | Track 1 `L168, 219` |
| 219,399 variants / 13,338 genes (filter-off run) | Track 1 `L186` |
| 12,431 / 5,348 ACMG rows; 53 s runtime; “twelve robustness controls” | Track 1 `L471, 518–519` (12,431 as patient “retained” is in `replay/RESULTADOS.md:68`, labelled as rows) |
| 15–20 × 10⁶ fibroblasts; 4–8 weeks | Track 2 `L713–715` (points at `track2/DATOS_CANDIDATO.md`, not in the listed set) |

r9 combined scores 0.5871 / 0.3965, ranks 1/2/3, Δ 0.1906, GIAB 0.5619, 1000G max 0.5207 CDH1 HG01885, P-B2 1/3, LOD 1.46/2.07/2.95%, power 0.897 / 0.063 / 0.387 / 0.589 / 0.196, bulk ratios 1.14/1.30/1.50/2.00×, PSMB5 ρ/q/interaction, ClinVar census 1,497 / 1 / 1,426 / 82/94, pLDDT 91.5 / 91.1 / 63.6, RSA 0.162, phase 10,911 bp / 1,391 of 1,452 / 0.0034 — these matched the listed sources.

`replay/out_r9/*/noclinvar` is **0.585** (`delta_clinvar_abs` 0.0021), with variant score 0.9986. The reports’ 0.5743 / 0.0128 is the substituted-locus X2/X3 construct in `replay/RESULTADOS.md:128–133`, not the r9 `noclinvar` object. Different experiment; not scored as a report error.

## Track 1 write-up vs Track 2 report

1. **BAM / GC-LOESS.** Track 1 `L245` (“only the VCF was available… no GC-LOESS possible”) vs Track 2 `L534–538` (choice of input; FASTQ exist). Track 1 also disagrees with itself: `L563` “the challenge distributed a VCF and raw reads, not a BAM, and we did not realign”.
2. **Mosaicism LOD.** Track 1 `L247–274` stops at 14–16% and “7–16× below”. Track 2 `L551–582` adds calibrated 2.07% “at the boundary”, identifiability 0.1–0.2%, and withdrawal of the proband result (`L598–625`).
3. **r9 planted alleles.** Track 1 `L297–300` attributes r9 0.3965 to ClinVar 4600147 `T>A`. Track 2 does not restate the plant; the r9 JSON is `T>G`.
4. **Missense AF / FASTQ size.** 8.99×10⁻⁷ vs 9.0×10⁻⁷; 85 GB vs 84.7 GB (cosmetic, above).

No other numeric clash between the two write-ups on shared quantities (0.5871 / 0.5538, 0.3965, 0.1906, 0.0034, 10,911 bp, 1,391/1,452, ClinVar census, DepMap ρ/q/p = 0.026, power 0.897, LOD 2.07%).
