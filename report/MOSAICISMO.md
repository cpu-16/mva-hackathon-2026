# ¿Se puede medir la carga de aneuploidía de MVA en el WGS bulk? — Análisis de sensibilidad

Fecha: 29-ago-2026. Datos: **solo el VCF** de `WGS_EX2312012` (GRCh38, GATK 4.2.4.0, 44× nominal).
No se usaron los FASTQ ni hay BAM disponibles, lo que limita el análisis y se declara desde el inicio.

> **Versión 2.** La primera versión de este documento afirmaba haber *demostrado* que no hay
> mosaicismo. Una revisión adversarial mostró que el estadístico empleado no tenía potencia para esa
> afirmación. Esta versión corrige el error, calcula el límite de detección real y reformula la
> conclusión. El argumento resultante es más débil en lo que afirma y más fuerte en lo que sostiene.

## La pregunta

MVA se define por aneuploidías mosaico *variegadas*. Cualquier terapia futura necesitaría medir la
**carga de aneuploidía** como desenlace. La pregunta operativa es: **¿sirve el WGS bulk para eso?**

Ésta no es una pregunta sobre si este niño tiene mosaicismo — lo tiene, por definición diagnóstica.
Es una pregunta sobre el poder de resolución del ensayo.

## Métrica y por qué

En una trisomía, los sitios heterocigotos se separan hacia `1/(2+f)` y `(1+f)/(2+f)`, donde *f* es la
fracción de células trisómicas. **La media del BAF no se mueve** (la separación es simétrica); lo que
cambia es la dispersión. La métrica correcta es por tanto la **desviación media |BAF − 0.5|**, no la
media ni un conteo de valores atípicos.

*(La primera versión usó la fracción de sitios fuera de 0.38–0.62. Ese umbral está dominado por la
cola binomial: a 44× y sin mosaicismo alguno, el 9.7% de los sitios cae fuera solo por muestreo de
lecturas. Un mosaico del 14% lo llevaría a 12.8% — tres puntos, indistinguibles de la variación
técnica entre cromosomas. **El test no tenía potencia para la hipótesis que decía evaluar.**)*

## Límite de detección, calculado

Simulación de la desviación media |BAF − 0.5| a DP = 44, con 40,000 sitios por condición:

| Fracción de células con trisomía | Desviación media | Efecto sobre el basal |
|---|---|---|
| 0% (sin mosaicismo) | 0.0601 | — |
| 5% | 0.0603 | +0.0001 |
| 10% | 0.0629 | +0.0027 |
| **14%** | 0.0656 | **+0.0055** |
| 20% | 0.0704 | +0.0103 |
| 30% | 0.0808 | +0.0206 |

El ruido que hay que superar no es el estadístico sino el **sistemático entre cromosomas**. En estos
datos, la desviación medida a profundidad fija (DP 40–48) varía entre 0.0532 y 0.0581 según el
cromosoma — una dispersión de **≈0.005** atribuible a contenido GC, mapeabilidad y duplicaciones
segmentales.

**Límite de detección práctico de este VCF: trisomía clonal de un cromosoma completo presente en
~12–15% de las células.** Por debajo de eso, el efecto queda enterrado en la variación técnica entre
cromosomas.

Un punto que conviene decir explícitamente porque es contraintuitivo: **el cuello de botella no es la
cobertura**. El error de Poisson al promediar un cromosoma entero a 44× es del orden del 0.03%.
Secuenciar a 200× no bajaría el LOD de forma apreciable, porque lo que limita es el sesgo sistemático
de la librería, no el muestreo de lecturas.

## Qué se observó

Cuatro análisis — **tres son refinamientos del mismo estadístico de BAF, uno es ortogonal**
(dosis por profundidad). No son cuatro pruebas independientes, y la primera versión de este documento
los presentaba como tales.

| Análisis | Resultado |
|---|---|
| BAF por cromosoma (2.27 M SNVs het) | Señal aparente en chr20, 21, 22, X |
| Mismo test a profundidad fija (DP 40–48) | chr21 **desaparece** — era artefacto de cobertura (DP medio 50.7). chr20 y chr22 persisten |
| Perfil espacial en ventanas de 5 Mb | chr20 y chr22 tienen **medianas normales** (13.1% y 14.0%); las ventanas altas caen en el centrómero y en **22q11**, la duplicación segmental más conocida del genoma. Artefacto de mapeo local |
| Dosis por profundidad (media recortada) | Ganancia aparente de +2.9% a +7.0% en chr16, 17, 19, 20, 21, 22 |

### La señal de dosis: una explicación parcial, honestamente incompleta

Es tentador atribuir el patrón de dosis al contenido GC, ya que chr19, 22, 17 y 16 están entre los más
ricos en GC del genoma. **Pero nuestros propios datos no sostienen esa explicación de forma limpia:**
la correlación medida entre GC y cobertura fue **r = 0.43** (n = 22), y **chr21 —el mayor desvío
(+7.0%)— es de los cromosomas más pobres en GC**. La explicación por GC funciona para chr19, 22, 17 y
16, y falla para chr20 y chr21, que son más plausiblemente artefactos de mapeo en acrocéntricos y
regiones de baja complejidad.

Además, el GC se estimó con 2–3 ventanas de 200 kb por cromosoma: un muestreo demasiado pobre para
caracterizar un cromosoma entero. **Es una medición insuficiente, no una explicación establecida**, y
resolverla exigiría normalización GC-LOESS sobre los BAM, que no tenemos.

Lo que sí se sostiene: la señal de dosis **no la corrobora el indicador más robusto**. El BAF es un
cociente interno de cada sitio y cancela el sesgo de cobertura; la dosis compara profundidades
absolutas y hereda todos los sesgos de librería. Cuando ambos discrepan, la carga de la prueba recae
en la dosis.

## Conclusión

**No es que hayamos demostrado la ausencia de mosaicismo. Es que este ensayo no puede detectarlo al
nivel en que la enfermedad lo produce.**

La aritmética de la variegación, presentada como **cota ilustrativa y no como medida de este
paciente**: si el 30% de las células fuera aneuploide —el orden de magnitud del criterio diagnóstico
clásico, no un dato de este niño— y cada célula alterara un cromosoma distinto entre 22 autosomas,
cada cromosoma quedaría afectado en ~1.4% de las células. Con *k* cromosomas alterados por célula la
cifra sube a `0.30 × k / 22`, y ganancias y pérdidas del mismo cromosoma **se cancelan en bulk**. Aun
en el escenario más favorable, la carga por cromosoma queda **muy por debajo del LOD de ~12–15%**.

Y algo que ninguna mejora técnica resuelve: **promediar millones de células borra la variegación por
construcción.** Más cobertura, mejor química o corrección de GC subirían la sensibilidad para una
aneuploidía *clonal*, no para una *variegada*.

**Limitación adicional que no puede pasarse por alto:** el sello citogenético de MVA es la
**separación prematura de cromátidas (PCS)**, que es un fenómeno de metafase y **no deja huella
alguna en la secuencia de ADN extraído**. Ninguna profundidad de WGS lo detectaría. Además, la sangre
de un paciente post-quimioterapia por ERMS puede tener una carga de aneuploidía muy distinta de la de
un cultivo de linfocitos en metafase.

## Consecuencia práctica

Los endpoints adecuados **ya existen y son estándar** — no los proponemos como novedad:

| Endpoint | Estado en el campo |
|---|---|
| Cariotipo de metafases con recuento de PCS | El criterio diagnóstico de MVA |
| Ensayo de micronúcleos | Estándar internacional de mis-segregación (OECD TG 487) |
| scDNA-seq de baja cobertura | Establecido para aneuploidía desde Knouse et al. 2014 (PMID 25197050), que mostró precisamente que el bulk promedia y borra lo que la célula única sí ve |
| **WGS bulk** | **Insuficiente — cuantificado aquí: LOD ~12–15% clonal** |

Nuestra contribución no es inventar el endpoint. Es **cuantificar, con los datos que este hackathon
entrega, cuánto se queda corto el atajo** — y por tanto por qué cualquier evaluación de una terapia
candidata para MVA debe medir mis-segregación célula a célula y no puede sustituirla por
secuenciación en bloque.

Para el Track 2 esto tiene una consecuencia directa: **ninguna propuesta terapéutica cuyo desenlace
sea "reducir la carga de aneuploidía" es evaluable con los datos de este hackathon**, y cualquier
screen de compuestos debe incluir mis-segregación en las células supervivientes como criterio de
descarte, no solo viabilidad.

## Reproducir

```bash
cd ~/datos/HACKATHON-MVA-2026/data
bcftools view -f PASS -g het -v snps WGS_EX2312012_HGWCNDSX7.vcf.gz \
  | bcftools query -f '%CHROM\t%POS\t[%AD]\t[%DP]\n'
# métrica: media de |BAF-0.5| por cromosoma, estratificada a DP 40-48
# poder: simulación binomial con BAF = (1+f)/(2+f) y 1/(2+f)
```
