# Codex — qué hacer con los 85 GB de lecturas crudas y la GPU

`codex exec`, 30-ago-2026. Brief: `brief_datos_crudos.md`.

## Veredicto

Sí deben procesar los FASTQ, pero no porque sea probable encontrar “el mosaicismo de MVA” directamente.

La mejor oportunidad competitiva es esta:

> Convertir el WGS bruto en un ensayo pre-registrado y calibrado que determine qué componentes de la aneuploidía variegada son observables en ADN bulk, cuáles no son identificables ni siquiera con cobertura infinita, y qué límite de detección tiene este caso concreto; simultáneamente, cerrar con evidencia física la fase de BUB1B y buscar variantes estructurales que el VCF original nunca pudo contener.

Eso puede producir un resultado positivo o un negativo fuerte. Ambos son defendibles. En cambio, “aplicamos cinco callers nuevos” no gana.

Mi ranking:

1. **Mosaicismo: ensayo de detectabilidad + calibración por inyección.**
2. **SV/CNV genome-wide, con adjudicación clínica.**
3. **Fase física e insert-size real: corrección obligatoria.**
4. **Re-calling de SNV/indels como auditoría del VCF.**
5. **Todo lo demás solamente si 1–4 generan una razón concreta.**

La afirmación más peligrosa ahora no es la del phasing. Es asumir que “>25% de células aneuploides” necesariamente deja una señal agregada detectable en bulk WGS. No necesariamente.

---

# 1. Qué desbloquean realmente los FASTQ

| Análisis | Qué añade frente al VCF | Valor |
|---|---|---|
| Profundidad normalizada y BAF | Busca alteraciones cromosómicas promedio y cuantifica sensibilidad | **Diferenciador principal**, si se calibra |
| Simulación/inyección de mosaicos | Mide potencia bajo distintas arquitecturas celulares | **Diferenciador principal** |
| SV/CNV | Deleciones, duplicaciones, inversiones, translocaciones y CNV ausentes del VCF SNV | **Diferenciador clínico real** |
| Insert-size y phasing físico | Comprueba directamente si algún fragmento enlaza variantes | **Corrección que deben** |
| Re-calling SNV/indels | Audita omisiones y discordancias del GATK 4.2.4 original | Control importante, rara vez diferenciador |
| QC de muestra | Cobertura, contaminación, duplicación, sexo, degradación, sesgos por lane | Necesario para validar lo anterior |
| mtDNA/heteroplasmia | Sólo relevante si aparece un candidato fenotípico convincente | Secundario |
| STR, HLA, telómeros, PRS, somatic SNVs exploratorios | Posibles técnicamente, sin hipótesis clínica fuerte | Mayormente busywork |

## Mosaicismo de lectura y BAF

Esto es lo más importante. Los FASTQ permiten:

- profundidad por ventanas de 10 kb, 100 kb y 1 Mb;
- exclusión de regiones no mapeables, centroméricas, segmental duplications y blacklist;
- corrección por GC;
- corrección por mappability;
- evaluación independiente por lane;
- BAF en SNPs comunes previamente especificados;
- combinación formal de profundidad y BAF;
- inyecciones sintéticas a fracciones conocidas.

Pero no permiten reconstruir qué cromosomas coexistían en una misma célula. Esa estructura celular se perdió cuando se extrajo ADN bulk.

## Variantes estructurales y CNV

Éste es el segundo análisis que vale la pena.

El VCF pequeño no puede representar adecuadamente:

- duplicaciones y deleciones grandes;
- inversiones;
- translocaciones;
- retrotransposones;
- eventos con breakpoints complejos;
- CNV mosaico;
- alteraciones que interrumpan BUB1B o un segundo gen relevante.

Usaría dos clases de evidencia:

- **Manta** para paired-end, split reads y ensamblaje local; combina paired/split-read evidence y puede reportar algunos eventos aunque el ensamblaje del breakpoint falle. [Manta](https://github.com/Illumina/manta)
- **DELLY** como segundo caller independiente para deleciones, duplicaciones, inversiones y translocaciones; acepta BAM/CRAM marcado y ordenado. [DELLY](https://github.com/dellytools/delly)

No presentaría la unión indiscriminada de ambos. Presentaría:

1. eventos PASS concordantes;
2. eventos no concordantes pero apoyados manualmente por profundidad, pares discordantes y split reads;
3. anotación contra genes MVA/cáncer/desarrollo;
4. revisión visual;
5. frecuencia en poblaciones y regiones problemáticas.

Un SV clínicamente plausible adicional sería una sorpresa de mucho peso. Una lista de cientos de llamadas crudas perjudicaría.

## Re-calling moderno

Debe hacerse como auditoría, no venderse como innovación.

Preguntas predefinidas:

- ¿Se reproducen los dos alelos BUB1B?
- ¿Cambian GT, AD, DP, strand balance o calidad?
- ¿Aparece una variante coding/splice de alta prioridad ausente del VCF?
- ¿Aparecen indels complejos que GATK 4.2.4 representó de otra manera?
- ¿Hay discordancias sistemáticas por regiones o clase de variante?

El mejor uso del GPU aquí sería DeepVariant o Clair3, pero el resultado relevante es la **concordancia clínica**, no el número de variantes nuevas.

## Fase e insert size

El texto correcto ya no es:

> “No se puede ejecutar un read-backed phaser porque sólo hay un VCF.”

Debe ser algo como:

> “The challenge includes short paired-end reads, so we generated alignments and tested physical phasing directly. The empirical fragment-length distribution and read-backed phasing produced no molecule or chain of overlapping fragments linking the two BUB1B variants, 10,911 bp apart. Therefore short-read physical phase remains unresolved; this is a measured negative, not a limitation inferred from file availability.”

Deben medir:

- distribución TLEN por lane y combinada;
- mediana, MAD, P95, P99, P99.9 y máximo después de excluir supplementary, duplicates, low MAPQ y pares impropios;
- fragmentos que cubran cada par de los tres heterocigotos;
- haplotype blocks producidos por WhatsHap/HapCUT2;
- evidencia individual de reads/pairs alrededor de las tres posiciones;
- posible evidencia de SV que pudiera crear una geometría inesperada.

La separación es aproximadamente:

- 40209701 → 40216470: 6,769 bp;
- 40216470 → 40220612: 4,142 bp;
- extremos: 10,911 bp.

No basta con decir que el insert típico es unos cientos de bases. El resultado debe ser “cero moléculas informativas, con N pares evaluados y una distribución empírica determinada”.

---

# 2. Mosaicismo: qué puede y qué no puede detectarse

## La limitación fundamental

Un bulk WGS observa promedios de copias y alelos, no la varianza célula a célula.

Si una fracción `f` de células tiene trisomía de un cromosoma, aproximadamente:

- copy number medio: `2 + f`;
- profundidad relativa frente a diploidía: `1 + f/2`;
- para un heterocigoto con un homólogo duplicado, BAF esperada: `1/(2+f)` o `(1+f)/(2+f)`.

Para `f = 0.02`:

- cambio de profundidad: aproximadamente 1%;
- desplazamiento de BAF: aproximadamente 0.5% respecto de 0.5.

Eso podría ser detectable al agregar miles de ventanas y SNPs si el efecto es consistente y el ruido sistemático está muy bien controlado.

Pero ahora el caso adversarial:

- algunas células ganan el homólogo materno;
- otras ganan el paterno;
- otras pierden uno u otro;
- las ganancias y pérdidas se equilibran;
- el cromosoma afectado varía entre células.

El conjunto puede tener:

- copy number medio exactamente 2;
- BAF media exactamente 0.5;
- ninguna señal de profundidad o BAF,

aunque muchas células sean aneuploides.

No es “falta de potencia”. Es **no identificabilidad**: dos poblaciones celulares biológicamente distintas producen la misma distribución observable de reads bulk.

Por eso no deben afirmar que un estadístico genome-wide siempre detectará MVA. Sólo puede detectar **desequilibrio agregado**, clones recurrentes o preferencias sistemáticas.

## ¿Per-cromosoma o agregado genome-wide?

Ambos, pero responden preguntas diferentes.

### Análisis primario: cromosoma por cromosoma

Para cada autosoma:

- log2 depth ratio normalizado;
- intervalo de confianza por block bootstrap;
- BAF modelada, no solamente `mean |BAF−0.5|`;
- likelihood de disomía frente a monosomía/trisomía mosaico;
- fracción celular estimada bajo cada modelo;
- concordancia entre lanes;
- inspección de gradientes o segmentos que indiquen CNV parcial.

Este análisis encuentra alteraciones clonales o un cromosoma sobrerrepresentado.

### Análisis secundario: omnibus genome-wide

Un estadístico global puede acumular desviaciones débiles en 22 cromosomas, pero debe ser un test predefinido y calibrado. No usaría el promedio firmado, porque las ganancias y pérdidas se cancelarían.

Opciones razonables:

- suma de log-likelihood ratios por cromosoma;
- suma de cuadrados de los z-scores de profundidad y BAF;
- exceso de dispersión entre cromosomas respecto a controles;
- prueba combinada de magnitud, con calibración empírica.

Debe reportarse como:

> “evidence of genome-wide aggregate dosage imbalance”

y no como:

> “percentage of aneuploid cells”.

Sin un modelo sobre cómo se reparten las aneuploidías entre células y cromosomas, esa conversión no está identificada.

Además, un score global tampoco salva el caso perfectamente balanceado. Puede aumentar potencia para 22 desviaciones pequeñas; no puede extraer una señal que matemáticamente es cero.

## El null correcto

No es uno solo. Necesitan tres niveles.

### 1. Null técnico externo

Procesar controles sanos desde FASTQ o CRAM con:

- plataforma y read length comparables;
- profundidad igualada por downsampling;
- mismo build y pipeline;
- preferentemente PCR-free;
- ambos sexos sólo si se analizan cromosomas sexuales.

Tres controles es un mínimo; 5–10 sería mejor. Se pueden procesar secuencialmente, guardar sólo resúmenes permitidos y borrar alineamientos para no consumir disco.

Los controles públicos no serán un “matched normal”. Sirven para estimar variación técnica y falsos positivos del pipeline.

### 2. Null interno

Usar:

- lanes como réplicas técnicas;
- ventanas autosómicas no problemáticas;
- permutación o block bootstrap de ventanas;
- cromosomas del mismo individuo para evaluar dispersión residual.

Esto mide estabilidad interna, pero **no es un null biológico suficiente**: si todos los cromosomas tienen pequeñas anomalías, el propio paciente contamina el null.

### 3. Inyecciones sintéticas

Éste es el elemento decisivo.

Antes de mirar el resultado final, generar datasets sintéticos que representen:

- trisomía clonal de chr1, chr7, chr15 y chr21 al 1%, 2%, 5%, 10%, 15% y 25%;
- monosomía en las mismas fracciones;
- ganancia preferencial materna o paterna;
- ganancias distribuidas entre los 22 cromosomas;
- ganancias y pérdidas balanceadas;
- duplicación alternante de homólogos;
- CNV segmentales de distintos tamaños;
- mezcla “adversarial” que produce media diploide y BAF 0.5.

Idealmente usar un genoma sano bien caracterizado y fase conocida, como HG002, para las inyecciones allele-specific. Downsamplear y mezclar reads es preferible a añadir ruido después sobre una tabla final.

La salida debe ser una curva:

- sensibilidad;
- especificidad;
- FDR;
- sesgo de la fracción estimada;
- intervalo de detección por arquitectura;
- porcentaje de réplicas detectadas.

No den un solo “LOD 14%”. Den algo como:

> Trisomía recurrente de un mismo cromosoma: 80% de potencia desde X%.  
> Desequilibrio disperso gains-only: 80% desde Y% global.  
> MVA balanceada entre cromosomas y homólogos: no identificable por bulk WGS, independientemente de profundidad.

Eso sí sería nuevo y científicamente útil.

## ¿Es detectable el nivel esperado de MVA?

Respuesta honesta:

- **Un clon recurrente de 10–25% en un cromosoma probablemente sí.**
- **Un efecto de 5% puede ser detectable**, especialmente combinando profundidad y BAF.
- **Un efecto por cromosoma de 1–2% es incierto y probablemente está cerca o debajo del ruido técnico práctico**, aunque el error binomial agregado sea pequeño.
- **MVA perfectamente variegada y balanceada puede ser totalmente invisible.**

La literatura sobre detección de mosaicismo estructural muestra que profundidad y BAF combinadas pueden encontrar eventos mosaico, pero normalmente se trata de una alteración recurrente en una región o cromosoma, no de inestabilidad celular balanceada. [MrMosaic](https://pmc.ncbi.nlm.nih.gov/articles/PMC5630034/) MAD-seq también combina mezcla de frecuencias alélicas y profundidad, pero presupone un cromosoma afectado de manera recurrente. [MAD-seq](https://pmc.ncbi.nlm.nih.gov/articles/PMC6028128/)

Para medir MVA como heterogeneidad celular, el ensayo correcto sigue siendo:

- cariotipo de muchas metafases;
- FISH multicolor/interphase;
- micronúcleos;
- single-cell low-pass WGS.

El bulk WGS podría detectar una consecuencia agregada, no la definición celular completa.

---

# 3. GPU de 8 GB: uso real y uso decorativo

## Donde no ayuda

La alineación será esencialmente CPU + I/O.

- BWA/BWA-MEM no usa GPU.
- `samtools sort`, CRAM encoding, duplicate marking, mosdepth, Manta, DELLY y WhatsHap son CPU.
- Parabricks completo no es una opción prudente con 8 GB.
- Entrenar un detector neuronal con un paciente sería metodológicamente indefendible.

No intentaría convertir el mosaicismo en un proyecto de deep learning. No hay tamaño muestral, labels ni validación independiente.

## Donde sí puede ayudar

### DeepVariant

DeepVariant separa aproximadamente:

1. `make_examples`: CPU e I/O;
2. `call_variants`: inferencia, acelerable con GPU;
3. `postprocess_variants`: CPU.

La RTX puede acelerar la segunda etapa. DeepVariant tiene imágenes con soporte de GPU, pero deben comprobar compatibilidad CUDA/driver y memoria en una región de prueba antes del WGS completo. [DeepVariant](https://github.com/google/deepvariant)

Con 8 GB:

- probar primero chr20 o chr21;
- limitar paralelismo de inferencia si hay OOM;
- vigilar VRAM;
- no prometer aceleración end-to-end: `make_examples` puede seguir dominando.

### Clair3

Es una alternativa razonable y probablemente más cómoda en una GPU de consumo. También requiere pileup/alignment processing en CPU y la GPU acelera principalmente inferencia. Puede usarse como segundo caller, pero no ejecutaría DeepVariant y Clair3 completos salvo que aparezca una discrepancia clínicamente relevante.

## Recomendación

- **Caller principal:** DeepVariant, si la prueba de chr20 cabe de forma estable.
- **Fallback:** DeepVariant CPU o Clair3.
- **GPU como contribución:** acelerar una auditoría rigurosa.
- **No vender el GPU como innovación.**

La respuesta llana es: **la alineación es CPU-bound y el papel del GPU es pequeño**. No hay aquí una aplicación donde la RTX transforme el análisis central.

---

# 4. Pipeline y orden de ejecución

## Antes de alinear

### Congelar un pre-registro

Debe incluir:

- hipótesis;
- endpoints primarios y secundarios;
- masks;
- tamaños de ventana;
- filtros MAPQ/base quality;
- selección de SNPs;
- modelos de mosaic fraction;
- estadístico omnibus;
- simulaciones;
- umbrales;
- criterios de llamada de SV;
- reglas para cambiar el informe.

No miren primero el plot y luego decidan qué desviación es interesante.

### Verificar referencia exacta

El FASTQ debe alinearse contra la misma referencia compatible con el VCF:

- GRCh38 exacta;
- comprobar contigs, ALT/decoys y MD5;
- confirmar representación de chr15;
- conservar manifiesto de versiones y checksums.

Una referencia GRCh38 distinta puede fabricar discordancias en calling y SV.

### Recuperar espacio

Actualmente hay aproximadamente 37 GB en:

- `2602_hg38.zip`: 23.6 GB;
- `2602_phenotype.zip`: 13.5 GB.

Si las extracciones y checksums están verificados, ésos son los primeros candidatos a borrar. No borraría los FASTQ antes de validar el CRAM correspondiente.

## Elección de alineador

Con sólo 31 GB de RAM, usaría **BWA-MEM clásico**, no BWA-MEM2 como primera opción.

BWA-MEM2 puede ser más rápido, pero hay reportes de picos alrededor o por encima de 30 GB dependiendo del dataset; con 31 GB totales existe riesgo real de OOM o swapping. [BWA-MEM2](https://github.com/bwa-mem2/bwa-mem2), [ejemplo de memoria](https://github.com/bwa-mem2/bwa-mem2/issues/115)

BWA-MEM es más lento pero predecible y apropiado para PE149. [BWA](https://github.com/lh3/bwa)

Configuración inicial:

- 20–24 threads para alineación;
- dejar cores y RAM para descompresión/CRAM;
- read group separado por lane;
- `SM` común;
- marcar lane, flowcell y platform unit correctamente.

No usaría los 32 threads a ciegas: CRAM encoding, gzip input y sort competirán por CPU y memoria.

## Estrategia de disco

No crear SAM. No conservar BAM.

### Por lane

Para cada lane:

1. verificar checksum y conteo sincronizado R1/R2;
2. alinear contra GRCh38;
3. fixmate/ordenar;
4. escribir CRAM coordinado;
5. indexar;
6. `samtools quickcheck`;
7. comprobar número de reads, mapping rate y profundidad;
8. sólo entonces borrar esos dos FASTQ si necesitan espacio.

Esperaría aproximadamente 8–18 horas por lane dependiendo del CPU, velocidad del disco y compresión. No prometería menos sin un benchmark de 10–20 millones de pares.

### Consolidación

Después:

1. merge coordinado de los cuatro CRAM;
2. duplicate marking global;
3. CRAM final;
4. CRAI;
5. validación;
6. comparar read counts por RG contra los CRAM de lane;
7. borrar CRAM intermedios sólo después de validar el final.

El duplicate marking debe ser global. No basta con marcar cada lane independientemente si la misma librería fue distribuida entre lanes.

Si el pipeline elegido necesita temporal de sort, colocarlo explícitamente en el volumen de datos y monitorizar espacio. Mantener al menos 15–20 GB libres; CRAM puede fallar muy tarde si se llena el disco.

### Tamaño esperado

No asumir exactamente 35 GB. Según referencia, calidad, duplicación y nivel de compresión, esperaría aproximadamente 30–50 GB.

Con 85 GB de FASTQ + 30–50 GB de CRAM + temporales, están en el límite. Por eso el procesamiento y borrado validado por lane no es opcional.

## Tiempos realistas

- instalación, referencia y prueba: medio día–1 día;
- alineación completa: 2–4 días;
- merge/markdup/CRAM y QC: 0.5–1.5 días;
- DeepVariant WGS: aproximadamente 0.5–2 días según GPU/CPU;
- Manta/DELLY: horas a aproximadamente 1 día cada uno;
- depth/BAF: horas;
- construcción y validación de simulaciones: 1–3 semanas;
- interpretación, preregistro y redacción: 2–3 semanas.

Ocho semanas alcanzan. El cuello no es compute; es hacer una calibración que sobreviva revisión.

## Camino mínimo al primer resultado

### Día 1

- pre-registro corto;
- liberar ZIPs verificados;
- instalar BWA, mosdepth, Manta, DELLY, WhatsHap, Picard/samtools adecuado;
- benchmark de 10–20 millones de pares;
- fijar referencia.

### Días 2–4

Procesar la primera lane.

Con ella ya pueden obtener:

- insert-size real;
- cobertura y GC bias;
- evidencia física alrededor de BUB1B;
- primera estimación de duplicación y contaminación;
- comparación del GT/AD en las variantes.

Eso produce la primera corrección empírica, aunque no es todavía el análisis final.

### Días 4–8

- completar las cuatro lanes;
- CRAM final;
- QC inter-lane;
- medir phasing;
- ejecutar perfiles de profundidad gruesos;
- correr Manta/DELLY;
- re-calling regional BUB1B y después genome-wide.

`mosdepth` acepta CRAM y puede producir ventanas directamente; su documentación reporta tiempos de minutos para ventanas WGS en datos de referencia, aunque su máquina y CRAM diferirán. [mosdepth](https://github.com/brentp/mosdepth/blob/master/README.md)

### Semanas 2–4

- construir masks;
- BAF desde lista de SNPs común predefinida;
- modelo chromosome-level;
- controles públicos procesados idénticamente;
- inyecciones de trisomía/monosomía;
- null balanceado invisible.

### Semanas 5–6

- congelar resultado;
- adjudicar SV/CNV;
- análisis de sensibilidad;
- figuras;
- revisión adversarial.

### Semanas 7–8

- corregir todos los textos;
- generar PDF final;
- comprobar que no se exponen artefactos genómicos prohibidos;
- dejar margen para una sola nueva presentación de Track 1 si cambia materialmente;
- preparar Track 2 coherente con el resultado.

---

# 5. La frase que podría ganar

Si el resultado es negativo:

> **“We did not merely name BUB1B: we used the raw 40× genome to build and validate the first case-specific measurement of what bulk WGS can—and fundamentally cannot—observe about variegated aneuploidy, showing by read-level spike-ins that recurrent chromosomal clones above X% would have been detected while balanced cell-to-cell aneuploidy is non-identifiable in bulk DNA; we also excluded reportable structural alternatives and measured, rather than assumed, the failure of short-read phasing.”**

Si encuentran señal:

> **“Beyond identifying BUB1B, we recovered the defining genomic consequence of MVA directly from the raw reads: a reproducible chromosome-level dosage/BAF abnormality that survived lane replication, matched read-level simulations, exceeded an empirically calibrated healthy-genome null, and corresponded to an estimated X% mosaic cell fraction.”**

La segunda es más espectacular, pero sólo si satisface todos esos controles. Una señal de 0.7% sin null técnico adecuado sería peor que el negativo riguroso.

El análisis que produce cualquiera de las dos frases es el **ensayo pre-registrado de mosaicismo con simulaciones e identifiabilidad**, complementado por SV y phasing.

---

# 6. Qué no hacer

## No perseguir una “detección” a toda costa

Si prueban 15 tamaños de ventana, 8 normalizaciones, 12 métricas y luego publican la combinación que dio `p < 0.05`, el resultado no vale.

## No usar los 22 cromosomas como 22 controles independientes

Difieren en:

- longitud;
- GC;
- mappability;
- densidad de SNPs;
- repeats;
- sesgos de referencia;
- tolerancia biológica a aneuploidía.

El bootstrap debe respetar bloques y cromosomas.

## No confundir precisión estadística con identificabilidad

Millones de reads pueden medir una media con enorme precisión. No pueden reconstruir la distribución celular que produjo esa media.

## No usar CNVkit flat-reference como prueba definitiva

CNVkit soporta WGS, GC/repeat correction y BAF, pero recomienda referencias construidas con controles comparables. Un flat reference puede servir para exploración, no para la afirmación final. [CNVkit](https://github.com/etal/cnvkit/blob/master/doc/pipeline.rst)

## No ejecutar diez callers

Dos SV callers complementarios, un caller SNV principal y análisis dirigido bastan. Más herramientas multiplican falsos positivos y carga de adjudicación.

## No hacer deep learning con un paciente

No hay labels ni validación. Una red entrenada sobre inyecciones propias aprenderá su simulador, no necesariamente MVA.

## No convertir cada llamada somática de baja VAF en “genomic instability”

A 40×, un supuesto SNV al 2–5% tiene poquísimas lecturas alternativas y es vulnerable a:

- errores de secuenciación;
- strand bias;
- daño;
- mapping;
- clonal hematopoiesis;
- contaminación.

No es un proxy limpio de MVA.

## No dedicar semanas a ΔΔG antes de cerrar los reads

La calibración estructural de p.Asn1002Lys es secundaria frente a mosaicismo, SV y fase.

## No afirmar que el re-caller es independiente

DeepVariant y el VCF original parten de los mismos reads. Es una reanálisis metodológicamente distinto, no validación ortogonal biológica.

## No borrar FASTQ sin una cadena de validación

Checksum, conteos, RG, CRAM quickcheck, índice y regiones causales primero.

## No presentar un SV sin revisión visual y plausibilidad

Los short-read SV callers producen artefactos en repeats y segmental duplications. Concordancia entre herramientas ayuda, pero no reemplaza evidencia de reads.

---

# 7. Razones para no hacerlo o riesgos

## No veo una prohibición contra reprocesar los FASTQ

Al contrario: si fueron distribuidos como datos del reto, analizarlos localmente para el propósito del reto parece estar dentro del uso previsto.

La regla pública que sí importa es privacidad. Sage aclaró que deben eliminar VCF, BAM, CRAM, índices, subconjuntos y tablas genome-wide derivadas; pueden conservar la lista corta de hallazgos, rankings, código e informe. También exige controlar condiciones de servicios externos. [Aclaración oficial de Sage](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/2)

Por tanto:

- procesamiento local: sí;
- subir FASTQ/CRAM a un servicio no aprobado: no;
- publicar ventanas de cobertura genome-wide del niño: probablemente no;
- publicar figuras agregadas y pocos hallazgos adjudicados: sí, según la aclaración;
- guardar pesos o embeddings entrenados en su genoma: deben eliminarse.

## Riesgo para Track 1

El riesgo existe sólo si encuentran algo que cambie el diagnóstico:

- los alelos BUB1B no se reproducen;
- una muestra o build incorrectos;
- evidencia fuerte de cis;
- un SV/CNV que explique mejor el caso;
- contaminación significativa;
- una segunda enfermedad relevante.

Pero descubrirlo antes del cierre es mejor que dejar una afirmación falsa.

No gastaría un nuevo intento de Track 1 por:

- cambiar “no había alignments”;
- añadir insert-size;
- añadir un negativo de mosaicismo;
- reportar concordancia de calling.

Sí consideraría reenvío si:

- cambia una variante;
- cambia la interpretación primaria;
- aparece un hallazgo reportable;
- la fase se resuelve;
- el reporte actualizado forma parte sustantiva de la evaluación y la plataforma permite reemplazarlo.

Tienen cuatro intentos restantes. No es necesario usarlos hasta congelar los resultados.

## Riesgo de tejido

No sabemos por lo expuesto qué tejido originó el WGS. Es crítico.

El mosaicismo MVA puede variar por tejido y por selección celular. Un negativo en sangre no excluye:

- fibroblastos;
- epitelio bucal;
- tejido tumoral;
- otros compartimentos.

El informe debe decir “not detectable in the sequenced specimen”, nunca “absent in the child”.

## Riesgo de controles inadecuados

Un public BAM de otra química no es matched normal. Sirve para sensibilidad y falsos positivos del pipeline, pero la diferencia de batch debe incorporarse explícitamente.

## Coste subestimado

No es alineación ni GPU. Es:

- crear inyecciones biológicamente correctas;
- preservar haplotipos;
- evitar leakage entre calibración y resultado;
- adjudicar SV;
- redactar el límite de inferencia con precisión;
- mantener trazabilidad y borrar los datos a tiempo.

---

# Decisión final

Haría el proyecto.

No porque espere una prueba limpia de MVA en bulk WGS, sino porque la pregunta científicamente correcta es más profunda:

> **¿Qué parte de una enfermedad definida por heterogeneidad cromosómica celular sobrevive al colapso de millones de células en una sola muestra de ADN bulk?**

El raw WGS permite responderla experimentalmente para este caso. Ése es un diferenciador real frente a 52 equipos que sólo nombraron BUB1B.

Pero establezcan desde el principio esta regla de parada:

> Si no aparece un evento reproducible entre lanes, superior al null externo y recuperable en inyecciones predefinidas, el resultado será “no detectable con un límite calibrado”, no una señal rescatada cambiando ventanas o normalizaciones.

Ese resultado negativo, unido a la demostración formal de no identificabilidad de la MVA balanceada, sería bastante más fuerte que la afirmación actual del 14%, y mucho más difícil de refutar.

