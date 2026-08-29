# ¿Se puede ver el mosaicismo de MVA en el WGS bulk? — Análisis y resultado negativo

Fecha: 29-ago-2026. Datos: `WGS_EX2312012`, GRCh38, 44x, 4.74 M variantes PASS.
**Solo el VCF** — no se usaron los FASTQ.

## La pregunta

MVA se define por **aneuploidías mosaico variegadas**: distintas células portan trisomías o
monosomías de **cromosomas distintos**. La pregunta es si esa firma se ve en un WGS bulk de sangre,
lo que sería un diferenciador frente a un análisis de variante germinal estándar.

## Método

Tres pruebas independientes, cada una diseñada para descartar el artefacto de la anterior.

### Prueba 1 — Desbalance alélico (BAF) por cromosoma
En un cromosoma diploide las variantes heterocigotas se agrupan en una fracción alterna de 0.50. Una
trisomía las separa hacia 0.33/0.67. Se midió la fracción de het "desbalanceadas" (BAF <0.38 o >0.62)
sobre 2.27 M de SNVs het PASS.

**Resultado bruto:** chr20, 21, 22 y X por encima del basal (16.4%).

### Prueba 2 — Control por profundidad
El desbalance aparente crece cuando baja la cobertura. Repetido restringiendo a **DP 40–48**:

| Cromosoma | % desbalance | vs basal | Veredicto |
|---|---|---|---|
| chr20 | 19.1% | 1.38× | sobrevive |
| chr22 | 17.8% | 1.28× | sobrevive |
| chr21 | 14.3% | 1.03× | **se cae — era artefacto de cobertura** (DP medio 50.7) |
| chrX | 16.9% | 1.22× | esperado: varón, solo regiones PAR |
| chrY | 60.3% | 4.33× | esperado: haploide |

### Prueba 3 — Distribución espacial (ventanas de 5 Mb)
Una aneuploidía de cromosoma completo eleva **todas** las ventanas. Un artefacto de mapeo eleva unas
pocas.

| Cromosoma | Mediana por ventana | Ventanas altas | Rango |
|---|---|---|---|
| chr20 | **13.1%** (normal) | 2 de 13 | 11.1–65.2% |
| chr22 | **14.0%** (normal) | 2 de 7 | 11.9–26.1% |
| chr18 (control) | 13.1% | 0 de 15 | 10.6–15.4% |

Las ventanas altas de chr20 y chr22 caen en el centrómero y en **22q11**, la región de duplicaciones
segmentales más conocida del genoma. **Artefacto de mapeo, no aneuploidía.**

### Prueba 4 — Dosis por cobertura (media recortada al 10%)
Más sensible al mosaico bajo: una trisomía presente en el X% de las células sube la cobertura X/2 %.

| Cromosoma | Desvío | Equivaldría a |
|---|---|---|
| chr21 | **+7.02%** | ~14% de células |
| chr22 | **+6.14%** | ~12% de células |
| chr20 | +4.51% | ~9% de células |
| chr17 | +3.71% | ~7% de células |
| chr19 | +3.15% | ~6% de células |
| chr16 | +2.92% | ~6% de células |
| los otros 16 autosomas | −1.2% a +1.5% | ruido |

## El conflicto entre pruebas, y cómo se resuelve

**La prueba 4 sugiere ganancia en 6 cromosomas. Las pruebas 1–3 (BAF) dicen que no.** No se pueden
sostener las dos.

Argumentos por los que gana el BAF:

1. **El patrón de la prueba 4 sigue propiedades técnicas del cromosoma, no biológicas.** Cinco de los
   seis (19, 22, 17, 16, 20) son precisamente los cromosomas más ricos en GC del genoma, y el sesgo
   de GC en librerías con PCR es un artefacto documentado que infla la cobertura ahí. El sexto,
   chr21, es acrocéntrico y pequeño, con brazo p de heterocromatina no ensamblada que atrae lecturas
   mal mapeadas. chr18, de tamaño casi idéntico a chr17 pero pobre en GC, no se desvía (+0.10%).
2. **Una aneuploidía *variegada* no produciría un patrón ordenado.** Por definición la variegación es
   estocástica; que los cromosomas afectados coincidan con el ranking de GC es demasiada coincidencia.
3. **Las dos medidas deberían coincidir y no lo hacen.** Una trisomía en el 14% de las células (lo que
   implicaría el +7% de chr21) desplazaría el BAF de las heterocigotas a ~0.47/0.53, detectable con
   11,463 SNVs. La prueba 2 da a chr21 un desbalance de 14.3% — indistinguible del basal de 13.9%.
4. **El BAF es intrínsecamente más robusto**: es un cociente interno de cada sitio, así que se cancela
   el sesgo de cobertura. La dosis compara profundidades absolutas entre regiones y hereda todos los
   sesgos de librería.

**Verificación parcial y su límite:** la correlación medida entre GC y cobertura dio r = 0.43 (n = 22),
más baja de lo esperado — pero el GC se estimó con solo 2–3 ventanas de 200 kb por cromosoma, muestreo
demasiado pobre para caracterizar un cromosoma entero. **No es una refutación de la hipótesis del GC;
es una medición insuficiente**, y se reporta como tal. Confirmarla exigiría GC por ventana sobre la
referencia completa y una normalización tipo GC-LOESS sobre los BAM.

**Veredicto:** no hay evidencia sólida de aneuploidía mosaico. La señal de dosis es más
parsimoniosamente explicada por sesgo técnico, y queda registrada como hipótesis pendiente en vez de
como hallazgo.

## Por qué el resultado negativo era esperable — y por qué importa

No es una limitación de los datos: **es la naturaleza de la enfermedad.**

En MVA la aneuploidía es *variegada* — cada célula pierde o gana un cromosoma **distinto**. El
criterio diagnóstico clásico es >25% de metafases con aneuploidías **de cromosomas variados**. Si el
30% de los linfocitos es aneuploide y esa carga se reparte entre 22 autosomas posibles, cada
cromosoma individual queda alterado en ~1.4% de las células, lo que equivale a un cambio de dosis
de ~0.7%. **Un WGS bulk a 44x no puede resolver eso**, y promediar sobre millones de células borra
justo la heterogeneidad que define el fenotipo.

Es la razón por la que MVA se diagnostica con **cariotipo célula a célula**, no con secuenciación bulk.

Consecuencias prácticas:

1. Para el **Track 1** esto es un control negativo útil: descarta que la señal causal esté en una
   aneuploidía constitucional y refuerza que el hallazgo es la variante germinal en **BUB1B**
   (ver `HALLAZGOS.md`).
2. Para el **Track 2** es una advertencia: cualquier propuesta terapéutica cuyo desenlace se mida
   como "reducción de la carga de aneuploidía" **no es evaluable con estos datos**. Necesitaría
   cariotipo, FISH o secuenciación de célula única.
3. El análisis con los FASTQ crudos y corrección de GC podría bajar el límite de detección, pero no
   por debajo de la barrera estadística que impone la variegación. Conviene decirlo antes de gastar
   85 GB y horas de cómputo persiguiéndolo.

## Reproducir

```bash
cd ~/datos/HACKATHON-MVA-2026/data
bcftools view -f PASS -g het -v snps WGS_EX2312012_HGWCNDSX7.vcf.gz \
  | bcftools query -f '%CHROM\t%POS\t[%AD]\t[%DP]\n'
# luego las cuatro pruebas descritas arriba
```
