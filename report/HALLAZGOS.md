# Hallazgo Track 1 — variante causal candidata

Análisis del 28-ago-2026. Datos: WGS singleton `EX2312012`, GRCh38, GATK 4.2.4.0 (DNAnexus, feb-2025),
4,740,790 variantes PASS.

## Resultado

**BUB1B — heterocigoto compuesto** (MVA1, OMIM 257300, autosómico recesivo)

| # | Variante (GRCh38) | HGVS | Consecuencia | GT | DP | gnomAD AF | ClinVar |
|---|---|---|---|---|---|---|---|
| 1 | chr15:40209701 T>G | `NM_001211.6:c.2210T>G` `p.Leu737Ter` | **stop_gained** (HIGH) | 0/1 | 46 | 0.00003 | **Pathogenic/Likely pathogenic** (2024-10-09) |
| 2 | chr15:40220612 T>G | `NM_001211.6:c.3006T>G` `p.Asn1002Lys` | missense (MODERATE) | 0/1 | 28 | ausente | VUS — ClinVar tiene `c.3006T>A`, mismo cambio proteico (2025-09-19) |

## Cómo se llegó (sin asumir la respuesta)

1. Panel de 11 genes de MVA y fenocopias, coordenadas obtenidas de **Ensembl REST** (no de memoria):
   BUB1B, CEP57, TRIP13, CENATAC, MAD1L1, MAD2L1BP, CEP192, BUB1, SMC5, TRIM37, CENPE. Padding 5 kb.
2. 1,532 variantes PASS en esas regiones → anotación con **Ensembl VEP REST**.
3. Filtro: impacto HIGH/MODERATE en transcrito canónico **y** gnomAD AF < 1% o ausente.
4. Sobrevivieron **3 variantes**:

| Gen | Variante | Impacto | gnomAD | ¿Explica un fenotipo AR? |
|---|---|---|---|---|
| BUB1B | p.Leu737Ter | HIGH | 0.00003 | ✅ junto con la #2 |
| BUB1B | p.Asn1002Lys | MODERATE | ausente | ✅ junto con la #1 |
| MAD1L1 | p.Arg59Cys | MODERATE | 0.00297 | ❌ alelo único, no bialélico |

**BUB1B es el único gen del panel con dos alelos raros afectados.** Patrón clásico de MVA1: un alelo
truncante + un alelo missense.

## Confirmación independiente: Exomiser genome-wide, sin panel

El apartado anterior parte de un panel de 11 genes, así que arrastra un sesgo: buscamos donde ya
sospechábamos. Para eliminarlo se repitió el análisis **sin ninguna restricción de genes**, dejando
que la priorización la hiciera el fenotipo.

- Herramienta: **Exomiser 15.1.0**, bases de datos hg38 + fenotipo release **2602**.
- Entrada: el VCF completo (4,740,790 variantes PASS) y los **8 términos HPO**. Sin panel, sin
  lista de candidatos, sin mencionar MVA ni BUB1B en ninguna parte de la configuración.
- Priorización: `hiPhivePrioritiser` (humano + ratón + pez + PPI) y `omimPrioritiser`.
- Tiempo de ejecución: **53 segundos** (32 CPU, 16 GB de heap).

Embudo: 4,702,177 pasan el filtro de calidad → 277,724 tras efecto → 11,255 tras frecuencia →
9,935 tras herencia, repartidas en 3,139 genes.

**Resultado del ranking:**

| Rank | Gen | Modelo | Score combinado | Score fenotípico |
|---|---|---|---|---|
| **1** | **BUB1B** | AD | 0.5871 | 0.5635 |
| **2** | **BUB1B** | **AR** | 0.5538 | **0.7920** |
| 3 | FANCD2 | — | 0.2137 | 0.6605 |
| 4 | LZTR1 | — | 0.1470 | 0.5098 |

**BUB1B ocupa los dos primeros puestos** de 3,139 genes, con casi cuatro veces el score del tercero.
Y bajo el modelo recesivo —el correcto para MVA1— Exomiser marca **ambas variantes como
contribuyentes**, es decir, reconoce por su cuenta el par heterocigoto compuesto:

| Variante | Clase funcional | Score | ACMG (Exomiser) | Contribuye |
|---|---|---|---|---|
| `c.2210T>G p.(Leu737*)` | stop_gained | 1.0000 | **PATHOGENIC** | ✅ |
| `c.3006T>G p.(Asn1002Lys)` | missense | 0.9229 | UNCERTAIN_SIGNIFICANCE | ✅ |

Las coordenadas y el HGVS coinciden exactamente con los del análisis dirigido, y la clasificación
ACMG automática de Exomiser coincide con ClinVar en ambas variantes.

**Dos métodos ortogonales convergen en la misma respuesta**: uno basado en conocimiento previo de la
enfermedad, otro en similitud fenotípica sin conocimiento previo. Esa convergencia es el argumento
central del write-up.

*Nota de transparencia:* que FANCD2 (anemia de Fanconi) aparezca tercero es una señal sana — el
pipeline recupera la familia correcta de trastornos de inestabilidad genómica, no ruido aleatorio.

### Control de robustez: sin filtro de efecto

La corrida principal descarta variantes intrónicas, upstream/downstream e intergénicas antes de
puntuar. Para verificar que la respuesta no dependa de ese filtro, se repitió el análisis
**eliminándolo por completo**:

| | Corrida principal | Control sin filtro |
|---|---|---|
| Variantes evaluadas | 9,935 | **219,399** (22×) |
| Genes considerados | 3,139 | **13,338** (4×) |
| Tiempo | 53 s | 8 m 27 s |
| **BUB1B rank** | **1 (AD) y 2 (AR)** | **1 (AD) y 2 (AR)** |
| **Score combinado** | 0.5871 / 0.5538 | **0.5871 / 0.5538 (idénticos)** |

El top 10 completo es idéntico en ambas corridas. Evaluar veintidós veces más variantes y cuatro
veces más genes no mueve el resultado ni una posición.

*Limitación que queda:* se omitieron REMM y CADD. Se evaluó incorporar REMM, pero son 15.2 GB de
descarga y la variante causal es codificante, de modo que no alteraría el ranking; SpliceAI, incluido
en el análisis, cubre la clase no codificante clínicamente relevante (splicing). Para un caso con
sospecha de variante reguladora profunda sí haría falta.

## Concordancia con el fenotipo

Los 8 términos HPO del documento clínico encajan con BUB1B:

| HPO | Síntoma | Vínculo con BUB1B |
|---|---|---|
| HP:0002859 | Rabdomiosarcoma | Predisposición tumoral (Wilms/rabdo/leucemia) descrita en MVA1 |
| HP:0001518 | Pequeño para edad gestacional (~1 kg) | Restricción de crecimiento típica |
| HP:0004322 | Talla baja | ídem |
| HP:0001508 / HP:0003202 | Fallo de medro / atrofia muscular | ídem |
| HP:0001622 | Prematuridad (32 sem) | ídem |
| HP:0000121 | Nefrocalcinosis | Anomalía renal descrita en la serie |
| HP:0200067 | Abortos recurrentes de los padres | Señal de inestabilidad cromosómica — el documento lo marca como pista, no como fondo |

## Hallazgos secundarios: dos candidatos, ninguno reportable

Sobre las 12,427 variantes clasificadas por ACMG en el análisis, solo 4 llegaron a
patogénica/probablemente patogénica. Dos están fuera de BUB1B, y ninguna califica como hallazgo
secundario accionable. El razonamiento importa más que la lista:

### FANCD2 chr3:10046723 — `splice_donor_variant`, ACMG PATHOGENIC → **probable artefacto**

Tres señales lo desmienten:

1. **Fracción alélica anómala:** AD 61,28 sobre DP 89 = **0.31**, lejos del 0.5 esperado en una
   heterocigota limpia.
2. **Segunda variante a 2 pb:** hay un `splice_region_variant` en 10046725. Dos cambios contiguos en
   el mismo sitio donador es la firma de un indel mal alineado, no de dos eventos independientes.
3. **Locus con pseudogenes:** FANCD2 tiene pseudogenes con alta identidad de secuencia, y es un caso
   conocido de mapeo erróneo con lecturas cortas.

Y aunque fuera real: la anemia de Fanconi D2 es autosómica recesiva y aquí hay **un solo alelo** —
sería estado de portador, no enfermedad. **Recomendación: validar por Sanger antes de reportar
nada.** Que FANCD2 haya subido al puesto 3 del ranking se explica por su parecido fenotípico con MVA
(inestabilidad genómica, talla baja, predisposición tumoral), no por ser causal.

### GNRHR chr4:67753920 — missense, ACMG LIKELY_PATHOGENIC → **estado de portador**

Heterocigota limpia (AD 28,32 = 0.53, DP 60). GNRHR causa hipogonadismo hipogonadotrópico
normosmico, también **autosómico recesivo**: un alelo no produce enfermedad. No guarda relación con
el fenotipo del probando.

**No es un hallazgo secundario en el sentido de ACMG SF v3.2** — esa lista cubre condiciones
accionables en el propio paciente, no estados de portador. Su única utilidad sería el consejo
genético reproductivo de la familia, y comunicarlo excede el alcance de este hackathon.

### Conclusión

**Cero hallazgos secundarios accionables.** Se documentan los dos candidatos y por qué se descartan,
porque un informe que los presentara como hallazgos sería un falso positivo con consecuencias
clínicas: alarmar a una familia que ya carga bastante.

## Pendiente de verificar

- [ ] **Fase (cis vs trans)**: sin trío no se puede confirmar. Los ~11 kb entre ambas variantes exceden
      el alcance del read-backed phasing con Illumina PE. Argumentar por rareza + patrón AR + ausencia
      de homocigotos en gnomAD.
- [ ] **`c.3006T>G` vs `c.3006T>A`**: ClinVar registra el cambio proteico con la transversión a A.
      Confirmar si nuestra T>G existe como registro propio o es genuinamente nueva.
- [ ] **Análisis genome-wide con Exomiser + los 8 HPO**, sin panel — para poder afirmar en el write-up
      que el pipeline *descubre* la respuesta en lugar de confirmarla.
- [ ] **Hallazgos secundarios/incidentales** (se pueden reportar en la columna `notes`, no penalizan).
- [ ] **Mosaicismo desde los FASTQ** — el ángulo diferenciador; MVA es mosaico por definición.

## Reproducir

```bash
cd ~/datos/HACKATHON-MVA-2026/data
bcftools view -f PASS -r 15:40155984-40226137 WGS_EX2312012_HGWCNDSX7.vcf.gz \
  | bcftools query -f '%POS\t%REF\t%ALT\t[%GT]\t[%DP]\n'
```
