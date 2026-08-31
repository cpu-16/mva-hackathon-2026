# Codex — ¿esto gana? Puntuación con la rúbrica y qué falta

`codex exec`, 30-ago-2026. Cuarta ronda.

No. Con lo que existe hoy tienen una candidatura seria y probablemente finalista, pero no una candidatura que yo llamaría ganadora. Mi estimación honesta es 77–82/100; el techo sin trabajo nuevo es aproximadamente 83. El mayor déficit ya no es Rigor: son los 40 puntos de Impacto y Escalabilidad.

Antes de continuar, hay que corregir dos problemas nuevos en mosaico. Uno es narrativo; el otro afecta la validez de la calibración.

## 1. Puntuación actual

| Paquete | Rigor | Impacto | Innovación | Escalabilidad | Valor competitivo |
|---|---:|---:|---:|---:|---|
| DepMap/PRISM | 30/35 | 7/25 | 14/25 | 7/15 | Excelente falsificación; mata el titular terapéutico actual |
| MVA-Replay | 29/35 | 6/25 | 17/25 | 10/15 | Buen benchmark, pero margen pequeño y tier 30 abierto |
| Fase | 29/35 | 5/25 | 13/25 | 7/15 | Cierra una incertidumbre; no produce solución clínica |
| Mosaicismo | 25/35 hoy | 9/25 | 21/25 | 8/15 | Mejor diferenciador, pero aún tiene control y descripción defectuosos |
| **Paquete integrado** | **30/35** | **13/25** | **21/25** | **10/15** | **≈74–82/100**, según dureza del juez |

No se suman los paquetes: se solapan. La honestidad adversarial ayuda mucho en Rigor, pero no convierte cuatro negativos en impacto clínico.

Mi lectura del techo:

- Corrigiendo textos, cerrando tier 30 y controlando κ: aproximadamente 83–85.
- Añadiendo solo otra validación estadística: quizá 86.
- Añadiendo un artefacto clínico real y uno reutilizable: 88–91.
- “Ganar” depende del campo, pero por debajo de ~88 yo no apostaría a ello.

La adición individual de mayor rendimiento no es otro análisis de Rigor. Es un producto clínico de vigilancia respaldado por datos que pueda entregarse al equipo tratante. El segundo mayor rendimiento es convertir el método en software ejecutable.

## 2. Las contradicciones que encontré

### La tabla 100% a 2% no corresponde al detector final

El reporte combina:

- 100% de detección direccional a 2% procedente de la calibración analítica del promedio firmado cromosómico;
- un LOD de 2.07% central y 2.95% con κ=4 para el detector final Ψ de ventanas.

No son el mismo detector. A un LOD definido como 80% de potencia, el detector final no puede tener simultáneamente 100% a 2% bajo κ=2–4.

La variegación balanceada sí seguirá siendo invisible con Ψ: si el ADN agregado tiene CN=2 y BAF=0.5 exactamente, elevar promedios firmados al cuadrado no recupera información celular que ya se perdió. El problema no es esa conclusión; es que la tabla compara dos detectores sin rotularlos.

Acción: retirar la fila “directional 100%” del resultado final o regenerarla con exactamente Ψ, W=125, el mismo FWER, κ y número de réplicas.

### La calibración no corrió “sobre siete GIAB”

Esto es más serio. Los scripts muestran que:

- `01_calibracion.py` carga `mosaico/sitios/chr*.tsv.gz`;
- esos sitios y DP proceden del VCF del probando;
- `05_mc_gpu.py` también usa el N y DP del probando;
- `06_ventana.py` usa N=148,048 y `INV=0.02359` fijados, más la tasa de switch del trío;
- los conteos alternativos son sintéticos, no observaciones de siete genomas GIAB.

Lo público es la tasa/distribución de switches del trío. El sustrato de cobertura y número de sitios es el probando. Por tanto, son falsas las frases “injection runs on public data” y “calibrated on seven GIAB genomes”.

Eso no destruye la simulación: usar la cobertura objetivo es razonable para calcular un LOD aplicable al paciente. Pero debe llamarse:

> Simulación paramétrica condicionada al número de sitios y distribución de profundidad del probando, con tasa de switch estimada independientemente en un trío GIAB.

No “calibración empírica en siete genomas sanos”.

Además, en `07_probando.py`, `v_s` se estima usando la varianza del propio `dev` observado. Deben demostrar por simulación que esa autoestimación no absorbe señal ni distorsiona el nulo. El control 1000G es la forma correcta de reemplazarla.

### Otras contradicciones importantes

- “ClinVar solo cuesta 0.0128” oculta que 0.0128 es aproximadamente 51% del margen observado de 0.025. El ranking persiste, pero ClinVar sí aporta sustancialmente a la separación.
- Bortezomib no puede seguir siendo “el superviviente” sin abrir inmediatamente con que DepMap no sostiene la dependencia en tumores sólidos. Ahora es una hipótesis condicionada y debilitada, no la recomendación principal.
- No deben decir “compuesto heterocigoto en trans” ni “bialélico demostrado”. La formulación defendible es “dos variantes heterocigotas compatibles con el diagnóstico recesivo; fase no establecida”.
- “LOD 1.46–2.95%” es el rango de escenarios. Para este espécimen, κ≈2.27 implica una cifra interpolada cercana a 2.2%, pendiente del control empírico.
- Un gradiente continuo entre cromosomas no demuestra por sí mismo que el exceso sea un nuisance técnico. También puede reflejar diferencias sistemáticas por cromosoma, máscaras, densidad de SNP o phasing. Es sugestivo, no diagnóstico.

## 3. Control 1000G preciso

### Cohorte inicial

Usaría 192 individuos no emparentados:

- 96 de la superpoblación más cercana al probando, si la ascendencia puede inferirse lícitamente;
- 96 balanceados entre las demás superpoblaciones;
- sexos balanceados, aunque el endpoint use autosomas;
- excluir tríos relacionados, duplicados, contaminación conocida y muestras con cobertura atípica.

Después ampliaría a 384 solo si el paciente queda cerca del percentil 95–99. Con 192 se estima bien el cuerpo del nulo; con 384 se caracteriza mejor la cola. No hace falta empezar con 3,202.

### Cromosomas

Primera pasada: chr1, chr6, chr7, chr9, chr17 y chr22.

- chr17: mayor señal observada.
- chr6/7/9: siguientes señales.
- chr1: cromosoma grande y rico en sitios.
- chr22: pequeño, útil para comprobar dependencia con N y longitud.

Si la implementación funciona, ejecutar los 22 autosomas. La conclusión final necesita los 22; el subconjunto solo es piloto técnico.

### Universo y filtros

Aplicar exactamente a cada control:

- SNP bialélico;
- variante común del panel, MAF 0.01–0.99;
- GT heterocigoto;
- GQ≥30;
- máscara idéntica de mappability, segmental duplications, centromeros, baja complejidad y regiones problemáticas;
- mismo phasing/panel;
- ventanas de 125 sitios;
- mismo tratamiento de ventanas incompletas.

No compararía sin más el raw callset 1000G con los sitios PASS del probando. Deben construir un universo externo de loci de alta calidad —por ejemplo, el callset filtrado/phased— y usar el raw callset solo para recuperar AD en esos loci.

### Profundidad

La comparación directa 44× contra 30× no es válida sin normalización.

Haría tres análisis predeclarados:

1. Reducir estocásticamente los AD del probando a 30× mediante muestreo hipergeométrico.
2. Reducir controles y probando a profundidades comunes de 20×, 25× y 30×.
3. Modelar explícitamente la varianza esperada por sitio usando DP, conservando por separado el residuo correlacionado.

La reducción de profundidad añade ruido binomial, pero no elimina sesgos de mapping ya presentes. Precisamente por eso debe repetirse en varios targets y reportarse la estabilidad.

### Endpoints

Por individuo:

- κ global y por cromosoma;
- Ψ por cromosoma;
- máximo estadístico entre los 22 autosomas;
- autocorrelación/variograma de residuos por distancia física;
- distribución de tamaños físicos de las ventanas de 125 sitios;
- correlación de Ψ con GC, mappability, DP, densidad de heterocigotos y longitud del cromosoma.

El umbral final debe ser empírico:

> Percentil del máximo cromosómico del probando dentro de la distribución de máximos de controles.

Eso reemplaza el frágil `|z|≥3` y controla multiplicidad con el pipeline completo.

### Qué falsifica cada explicación

Origen técnico favorecido si:

- las mismas ventanas son ruidosas recurrentemente en controles;
- el exceso se asocia con GC, mappability, DP o densidad de SNP;
- κ≈2.27 es común en 1000G;
- desaparece tras estandarización locus por locus;
- cambia sustancialmente con profundidad o filtros;
- el patrón se replica como propiedad de determinados cromosomas en sanos.

Origen técnico falsificado parcialmente si el probando es un outlier extremo después de toda esa normalización.

Origen biológico favorecido si:

- el exceso es específico del probando;
- se reproduce independientemente en las cuatro lanes;
- forma un evento cromosómico coherente;
- BAF y profundidad total concuerdan en dirección y amplitud;
- es estable frente a máscaras y profundidad;
- no coincide con contaminación o artefactos recurrentes.

Pero hay una tercera categoría: muestra biológicamente anómala sin ser MVA. Contaminación, clonalidad hematopoyética y mezcla tisular pueden producir señal real en la muestra. Un control sano no distingue automáticamente “técnico” de “MVA”.

Y ningún control de bulk resuelve variegación perfectamente balanceada: esa arquitectura sigue siendo no identificable.

### Confusor GATK

Sí, puede invalidar una comparación ingenua. Influyen:

- versión de HaplotypeCaller;
- joint calling;
- VQSR frente a PASS;
- comportamiento de AD en regiones realineadas;
- plataforma, read length y duplicación;
- pipeline de alineamiento;
- profundidad y reglas de emisión del gVCF.

La mitigación mínima es el análisis de sensibilidad por profundidad y loci externos de alta confianza. Si el probando sigue siendo outlier, entonces recurrir a 24–48 CRAM públicos y volver a producir AD con el mismo caller/configuración usada para el probando en intervalos seleccionados. No hace falta realinear 1000G.

El control podrá decir si el paciente es anómalo bajo un pipeline próximo; no autoriza a etiquetar causalmente el exceso como técnico.

## 4. Trabajo real para Impacto y Escalabilidad

### Impacto: artefacto de vigilancia

El mejor producto no es otra candidatura farmacológica. Es:

- dataset versionado de todos los casos publicados de BUB1B/MVA con edad, genotipo, tumor, edad tumoral, localización y vigilancia conocida;
- script reproducible;
- curva de incidencia acumulada o, si el denominador y censura son demasiado malos, una tabla descriptiva honesta;
- análisis de cuántos tumores quedarían fuera de vigilancia a los 7, 10, 12, 15 y 18 años;
- cálculo de ecografías adicionales por tumor potencialmente cubierto;
- hoja clínica de una página específica para este niño: qué recomienda el consenso, qué no cubre, qué debe discutirse con genética/oncología.

Costo: 5–10 días de extracción doble y verificación. El punto crítico es no fabricar una Kaplan–Meier si los reportes carecen de seguimiento negativo y censura. En ese caso, usar denominadores explícitos y análisis de escenarios.

Impacto real máximo requeriría que un clínico revise o adopte la hoja. Sin esa revisión sigue siendo evidencia potencial, no cambio de cuidado consumado.

### Escalabilidad: herramienta ejecutable

Artefacto:

```text
mva-audit run --vcf sample.vcf.gz --hpo phenotypes.txt --out report/
```

Debe producir:

- control de calidad;
- ranking y sensibilidad a ClinVar/fenotipo;
- advertencia sobre fase;
- Ψ con nulo empírico;
- aplicación estructurada de los cinco filtros terapéuticos;
- reporte HTML/JSON;
- provenance y versiones;
- ejemplo público;
- tests;
- runtime, RAM y costo estimado para 1, 100 y 1,000 genomas.

Costo: 7–14 días si reutilizan los scripts existentes. No intentaría convertirlo en plataforma web.

La pieza reutilizable más fuerte es probablemente un módulo independiente de “mosaic dosage audit” con el nulo 1000G, no todo Exomiser envuelto en un CLI.

## 5. ¿Vale alinear los reads?

Sí, pero no el genoma completo como primera prioridad.

### Lo que sí justifica ahora

Primero alinearía todas las lanes de forma streaming y conservaría únicamente:

- chr15 alrededor de BUB1B, con mates;
- métricas globales de insert size/alineamiento;
- pequeños intervalos de control.

Esto permite:

- verificar ambas variantes a nivel de reads;
- descartar strand bias, end-of-read bias, paralogía y artefactos locales;
- comprobar p.Asn1002Lys, que tiene DP 28 frente a ~44×;
- medir el insert size real;
- demostrar empíricamente que ningún fragmento enlaza 10,911 bp;
- buscar soft clips o evidencia estructural local.

Es la mejor relación valor/costo del read stage. El VUS p.Asn1002Lys es parte del fundamento diagnóstico; un kill-switch negativo aquí sería más importante que otro decimal en κ.

Costo estimado: 1–3 días de cómputo para streaming de las ocho FASTQ, pocos GB de salida si solo retienen intervalos. No hace falta conservar un BAM completo.

### Alineamiento completo

Solo activarlo si ocurre uno de estos gates:

- el control 1000G deja al probando como outlier;
- aparece una señal cromosómica consistente;
- necesitan separar BAF de profundidad total;
- quieren analizar lane reproducibility en todo el genoma;
- surge sospecha concreta de CNV/SV.

Entonces producir CRAM directamente por lane, validar, fusionar y borrar FASTQ únicamente después de checksums y verificación. El análisis de profundidad independiente sería el compañero apropiado de BAF.

Re-calling genome-wide, DeepVariant, SV callers múltiples y “buscar algo que GATK perdió” son opcionales y de bajo rendimiento sin una hipótesis clínica concreta.

Mi veredicto: el alineamiento local/streaming sí se gana su costo. El CRAM genómico completo todavía no.

## 6. Qué dejaría de hacer

- No seguir defendiendo bortezomib como candidato principal.
- No hacer más predicciones in silico de p.Asn1002Lys sin calibración funcional.
- No reintentar fase estadística.
- No añadir más controles HPO pequeños después del tier 30.
- No hacer re-calling moderno de todo el genoma por curiosidad.
- No abrir SV/CNV genome-wide salvo que el Track 1 o el fenotipo sugieran una pregunta concreta.
- No construir dashboard.
- No usar la GPU para decorar el método.
- No afirmar que la variegación balanceada explica el negativo: es una arquitectura posible no identificable, no una causa demostrada de este resultado.
- No comenzar el motor completo antes de estabilizar y testear el módulo de mosaico.
- No esperar ocho semanas para usar una de las tres oportunidades de Track 2. Una versión corregida y coherente debería enviarse cuando esté lista; conservar dos intentos para mejoras materiales.

## Orden recomendado

1. Corregir inmediatamente las descripciones falsas y separar los detectores.
2. Cerrar el tier de 30 genomas.
3. Pilotar 1000G en seis cromosomas y 24 controles.
4. Si funciona, congelar protocolo y ampliar a 192 controles × 22 cromosomas.
5. En paralelo, hacer alineamiento streaming local de BUB1B.
6. Construir el artefacto clínico de vigilancia.
7. Empaquetar el detector como herramienta reproducible.
8. Solo si 1000G deja una anomalía real, generar CRAM completo y profundidad independiente.

La frase ganadora plausible sería:

> “No nos limitamos a repetir BUB1B: refutamos nuestra propia terapia candidata, medimos qué arquitectura de la enfermedad sí puede observarse en bulk WGS y cuál es matemáticamente invisible, validamos el límite contra cientos de controles procesados de forma comparable, verificamos los alelos a nivel de lectura y convertimos la principal brecha clínica —la vigilancia que termina antes de algunos tumores documentados— en un recurso reproducible y accionable.”

Hoy todavía no pueden decir esa frase.

Como contraste independiente, Claude puntuó el estado actual en 57/100 y un techo de ~82, más duro que mi 77–82 actual. Coincidió en lo esencial: el control 1000G es necesario, el alineamiento completo no debe ser el camino principal, bortezomib debe salir del titular y los mayores retornos están en vigilancia ejecutable y software reutilizable. Su observación más útil fue que 0.0128 equivale a aproximadamente la mitad del margen de 0.025; esa lectura debe incorporarse literalmente al reporte.

