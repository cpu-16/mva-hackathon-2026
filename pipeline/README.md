# pipeline/ — panel triage (control rápido, NO el análisis principal)

El análisis principal del hackathon es **genome-wide con Exomiser + HPO**.
Este directorio es solo un control: ¿hay alguna señal obvia en genes ya ligados a MVA?

## Archivos

| archivo | qué es |
|---|---|
| `mva_panel.hg38.bed` | Coordenadas GRCh38 de 11 genes ± 5 kb. Prefijo `chr`. |
| `mva_panel.provenance.tsv` | De dónde salió cada coordenada (Ensembl REST 116, 2026-08-29). |
| `chroms_ucsc_to_ncbi.txt` / `chroms_ncbi_to_ucsc.txt` | Mapas de contig para cruzar con ClinVar (NCBI, sin `chr`). |
| `triage.sh` | Subset al BED → PASS → gnomAD AF si existe → ClinVar → flag bialélico. |
| `resources/clinvar.vcf.gz` (+ `.tbi`, `.md5`) | ClinVar GRCh38 de NCBI (snapshot del FTP). |
| `resources/hp.obo` | Ontología HPO. |
| `resources/genes_to_phenotype.txt` | Mapa gen → término HPO. |
| `resources/SOURCES.txt` | URLs, fechas y checksums. |

**Símbolo CENATAC:** el actual es `CENATAC` (HGNC:30460; antes `CCDC84`). `C1orf112` **no** es alias: ahora es `FIRRM` (ENSG00000000460), otro gen; no está en el BED.

## Cómo se corre

bcftools no está instalado todavía:

```bash
sudo dnf install bcftools htslib
```

Cuando llegue el VCF del paciente:

```bash
cd /home/gar16/datos/HACKATHON-MVA-2026/pipeline
./triage.sh /ruta/al/paciente.vcf.gz ./out
# tabla: ./out/candidates.tsv
```

Opcional: `MAX_AF=0.001 ./triage.sh paciente.vcf.gz ./out` (default 0.01).
Si el VCF no trae un tag gnomAD, el filtro de frecuencia se salta (Exomiser lo hace genome-wide).
