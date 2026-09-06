# Comprobación de clon limpio — 6-sep-2026

Código del repo en commit local `ca50edb`, clonado sin hardlinks en
`/tmp/mva-clean-check-20260906`. No hubo descargas de datos ni análisis del paciente.

1. `python3 -m unittest discover -s replay -p test_output_reuse.py -v`: dos pruebas pasan.
   La suite usa archivos sintéticos y mocks; verifica prevención de reutilización, no exactitud
   del motor de priorización.
2. `python3 replay/mva_replay.py --self-check`: exit 1. Mensaje:
   `ClinVar id 533901 not found in /tmp/mva-clean-check-20260906/pipeline/resources/clinvar.vcf.gz`.
   Ese recurso no está empaquetado en el clon. El mensaje actual no distingue recurso ausente
   de alelo ausente, porque el helper `sh` no comprueba el código de salida de bcftools.

Conclusión: el código de las pruebas es portátil, pero el self-check completo depende del entorno
de análisis instalado. El resultado local 21/21 no equivale a reproducción independiente del
análisis en una instalación nueva. No se afirma que todas las otras dependencias estuvieran
correctas: la comprobación se detuvo en el primer recurso faltante.

Siguiente criterio de aceptación: instalación explícita con versiones/rutas/tamaños, error claro
ante recursos ausentes y ejecución de un caso público desde un checkout nuevo. Un caso adicional
con nueva hipótesis requiere diseño previo; no se ejecutó aquí.
