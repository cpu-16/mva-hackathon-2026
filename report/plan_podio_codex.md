# Plan para el podio — propuesta de Codex (30-ago-2026)

Mismo brief que Cursor (`brief_plan_podio.md`). Resumen fiel de su ranking; la versión de Cursor,
completa y literal, está en `plan_podio_cursor.md`.

## Ranking de Codex

1. **MVA-Replay** (4–6 días, CPU) — empaquetar `pipeline/triage.sh` + Exomiser + los controles HPO en
   Snakemake/Nextflow y meter 30–50 arquitecturas sintéticas en un VCF público GIAB GRCh38: variantes
   bialélicas BUB1B de distintas consecuencias, variantes en cis, un solo alelo, otros genes MVA y
   controles negativos. Cada caso con fenotipo correcto, incompleto y ajeno. Salidas: sensibilidad,
   tasa de falsos positivos, estabilidad leave-one-HPO-out. **La mejor relación beneficio/esfuerzo
   según Codex.** Riesgo: que los spike-ins parezcan diseñados para que el pipeline gane.
2. **Fase estadística de BUB1B** (3–5 días) — SHAPEIT5/Beagle contra panel GRCh38, varias ventanas y
   semillas, medir estabilidad. Veredicto `supported / unresolved`. Riesgo: variantes ultra-raras a
   11 kb; el panel puede no resolverlas.
3. **Calibración de p.Asn1002Lys** (5–7 días) — ΔΔG con dos métodos CPU (FoldX + DynaMut2) sobre un
   set de variantes BUB1B de ClinVar con evidencia, más controles benignos. Calibración ROC/PR antes
   de interpretar. "Indeterminado" es resultado legítimo. Riesgo: el dominio quinasa de BUBR1 tiene
   regiones estructuralmente inciertas.
4. **Censo de fármacos aprobados con denominador farmacológico** (8–12 días) — matriz auditable
   Open Targets + ChEMBL + FDA/DailyMed, con `passes/fails/not evaluable`. Riesgo: mezclar IC50
   bioquímica, celular y clínica sin una ontología estricta degenera en una hoja de cálculo inválida.

## Lo que Codex mandó matar
Dashboard o calendario de vigilancia · más revisión bibliográfica · **farmacogenómica de bortezomib
desde el VCF** ("no hay una regla clínica validada suficientemente fuerte") · predicción aislada con
AlphaMissense/SIFT/PolyPhen · volver a inferir aneuploidía desde BAF · modelado molecular con GPU.

## Diferencia clave con Cursor
Codex **no** propuso la prueba en DepMap/PRISM, que es la que acabó ejecutándose y produciendo el
primer resultado propio. Cursor **no** propuso MVA-Replay. Coincidieron en 2, 3 y 4.
