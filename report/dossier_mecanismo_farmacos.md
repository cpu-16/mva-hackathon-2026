# Dossier de mecanismo y fármacos: MVA1 por BUB1B

**Caso de trabajo.** Heterocigosis compuesta confirmada en `NM_001211.6`: c.2210T>G, p.Leu737Ter (stop-gained; ClinVar P/LP; gnomAD AF 3×10⁻⁵) y c.3006T>G, p.Asn1002Lys (missense; ausente de gnomAD; el mismo cambio proteico por c.3006T>A consta como VUS). Diagnóstico confirmado por el equipo: mosaic variegated aneuploidy tipo 1 (MVA1; OMIM 257300), autosómica recesiva. Los datos de variante y diagnóstico se aceptan como hallazgo confirmado y no se reevalúan aquí.

> **Alcance clínico:** este documento genera hipótesis para investigación y vigilancia multidisciplinaria; no prescribe tratamiento. No existe un fármaco aprobado que corrija BUB1B/MVA1. Cualquier uso propuesto sería *off-label*, experimental y, en este niño, debe subordinarse a oncología pediátrica, genética clínica, nefrología y un protocolo con monitorización.

## 1. Resumen ejecutivo

BubR1 es un componente esencial del mitotic checkpoint complex (MCC) y del control de las uniones cinetocoro–microtúbulo. p.Leu737Ter conserva el extremo N que forma el MCC y el módulo Bub3/KARD, pero corta al inicio del dominio pseudo-quinasa C-terminal; p.Asn1002Lys cae dentro de ese dominio. El alelo nonsense probablemente sufre NMD y, si produce proteína, elimina casi todo el dominio C-terminal; el efecto de Asn1002Lys sigue siendo una pregunta funcional, no un hecho. La combinación truncante + missense encaja con el patrón recurrente de MVA1 viable; dos pérdidas completas parecen difícilmente compatibles con vida, pero no permite pronosticar un tumor concreto. La asociación de MVA1 con rabdomiosarcoma embrionario y tumor de Wilms es real, aunque no hay una correlación alelo-tumor validada para estos dos cambios. Ningún candidato farmacológico tiene evidencia clínica en MVA1. Entre medicamentos aprobados, metformina/hidroxicloroquina reproducen sólo de modo indirecto señales del cribado de aneuploidía; everolimus/sirolimus tienen una justificación aún más contextual (mTOR/senescencia). Todos quedan como herramientas de validación preclínica, no como profilaxis. La intervención de mayor solidez clínica es vigilancia tumoral estrecha y adaptación individual de quimioterapia: la deficiencia del checkpoint puede agravar toxicidad de venenos mitóticos.

## 2. Sección 1: mecanismo molecular de los alelos

### 2.1 Mapa funcional de BubR1

La isoforma codificada por `NM_001211.6` tiene 1.050 aa. Los límites varían algunos residuos según anotación/constructo; por eso se muestran como intervalos funcionales aproximados, no como coordenadas clínicas absolutas. La arquitectura está sustentada por estudios estructurales y funcionales del SAC (PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/), [23789096](https://pubmed.ncbi.nlm.nih.gov/23789096/), [23345399](https://pubmed.ncbi.nlm.nih.gov/23345399/)).

```text
aa 1                                                                    1050
   | KEN1 |--- TPR N-terminal ---| KEN2/ABBA | GLEBS/Bub3 |-- KARD --| pseudo-quinasa |
     ~26       ~50–204              ~304       ~392–426     ~665–682    ~705–1034
                                                                   ↑            ↑
                                                               Leu737Ter    Asn1002Lys
```

- **KEN1/TPR N-terminal:** KEN1 y los TPR permiten la interacción con CDC20/APC/C y KNL1; junto con MAD2, BUB3 y CDC20, BubR1 integra el MCC que frena APC/C hasta que todos los cromosomas estén correctamente unidos (PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/); DOI [10.1074/jbc.M109.082016](https://doi.org/10.1074/jbc.M109.082016)).
- **GLEBS/Bub3-binding:** el motivo GLEBS recluta Bub3 y contribuye a localizar BubR1 en cinetocoros (DOI [10.1016/j.molcel.2012.03.009](https://doi.org/10.1016/j.molcel.2012.03.009)).
- **KARD:** un motivo fosforregulado recluta PP2A-B56, que antagoniza Aurora B y estabiliza uniones cinetocoro–microtúbulo; su alteración causa defectos de congresión también en células MVA (PMID [23789096](https://pubmed.ncbi.nlm.nih.gov/23789096/), [23345399](https://pubmed.ncbi.nlm.nih.gov/23345399/)).
- **Dominio C-terminal:** hoy se considera un **dominio pseudo-quinasa**, importante como andamio/estabilizador y para PP2A-B56, silenciamiento del SAC y alineación cromosómica, no una quinasa convencional fácilmente “activable” con un fármaco (DOI [10.1016/j.molcel.2012.03.009](https://doi.org/10.1016/j.molcel.2012.03.009)).

### 2.2 p.Leu737Ter

**Hecho verificado:** el codón 737 está al comienzo del dominio pseudo-quinasa (~705–1034). Un stop allí elimina aproximadamente 313 aa, incluidos casi todo ese dominio y el extremo C-terminal. Conserva en secuencia KEN/TPR, GLEBS y KARD, pero no debe asumirse que una proteína truncada sea estable o funcional. En un modelo MVA cercano, el alelo humano `2211insGTTA` produjo una proteína truncada X753 inestable; las combinaciones de alelos demostraron efectos que no se explicaban sólo por cantidad proteica o tasa de aneuploidía (PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/), DOI [10.1172/JCI126863](https://doi.org/10.1172/JCI126863)).

**Inferencia propia — NMD:** un codón de terminación prematuro tan anterior al último empalme suele activar nonsense-mediated decay si queda >50–55 nt por delante de la última unión exón–exón. Sin un ensayo de RNA específico del paciente no puede afirmarse el destino del transcrito. La hipótesis principal es **NMD parcial o intenso**; la alternativa es escape parcial con una proteína ~736 aa inestable que conserva el MCC N-terminal pero pierde el pseudo-dominio. Se debe medir, no deducir, mediante RNA-seq/RT-PCR alelo-específica ± inhibición experimental de NMD y western blot.

### 2.3 p.Asn1002Lys

**Hecho verificado:** Asn1002 cae dentro del lóbulo C del dominio pseudo-quinasa, no en KEN, TPR, GLEBS ni KARD. El cambio introduce una carga positiva y podría afectar plegamiento, estabilidad o interfaces C-terminales. Los fibroblastos MVA con mutaciones bialélicas muestran bajo BubR1, checkpoint debilitado y defectos de alineación (PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/)).

**Pregunta abierta:** no encontré un ensayo bioquímico publicado de p.Asn1002Lys. El hecho de que ClinVar contenga p.Asn1002Lys generado por otro cambio nucleotídico como VUS no demuestra patogenicidad ni benignidad de este alelo. **Inferencia propia:** en trans con una pérdida fuerte, podría ser un alelo hipomorfo que aporta suficiente función residual para viabilidad, pero esto exige segregación/fase ya establecida por el equipo y validación celular.

### 2.4 Genotipo–fenotipo y cáncer

**Hecho verificado:** en las primeras familias bialélicas, el patrón recurrente fue un alelo truncante más una sustitución aminoacídica, a menudo en el dominio C-terminal; células de pacientes mostraron reducción global de BubR1 y fallas tanto del SAC como de alineación (PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/)). Los modelos murinos que combinan X753, una sustitución C-terminal y un alelo hipomorfo muestran que identidad y combinación alélica modifican viabilidad, sarcopenia, senescencia y susceptibilidad tumoral; no existe una regla simple “menos proteína = fenotipo más grave” (PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/)). El knockout homocigoto de `Bub1b` es letal embrionario, mientras hipomorfos envejecen precozmente y acumulan aneuploidía (PMID [15208629](https://pubmed.ncbi.nlm.nih.gov/15208629/); [MGI:1333889](https://www.informatics.jax.org/marker/MGI%3A1333889)).

**Inferencia razonada:** dos alelos humanos verdaderamente nulos tenderían a ser más graves o inviables que truncante + hipomorfo, pero “dos truncantes” no equivale siempre a dos nulos: NMD, inicio alternativo, splicing residual y estabilidad cambian el efecto. No se debe convertir esta tendencia en pronóstico individual.

**Cáncer:** MVA/BUB1B predispone sobre todo a tumores embrionarios tempranos, en particular rabdomiosarcoma embrionario y Wilms, además de leucemia (PMID [16182441](https://pubmed.ncbi.nlm.nih.gov/16182441/), [28553959](https://pubmed.ncbi.nlm.nih.gov/28553959/)). Un ERMS de un paciente MVA bialélico mostró ganancias/pérdidas cromosómicas parecidas a ERMS esporádico, y el cribado de tumores esporádicos no halló mutaciones somáticas recurrentes de BUB1B; BUB1B constitucional parece crear el terreno de CIN, no necesariamente el driver somático final (PMID [16182441](https://pubmed.ncbi.nlm.nih.gov/16182441/)).

**Pregunta abierta importante:** no existe una correlación validada entre p.Leu737Ter/p.Asn1002Lys —ni entre “truncante + missense” en general— y riesgo diferencial de ERMS frente a Wilms. El rabdomiosarcoma del niño es coherente con el espectro, pero no prueba la función de Asn1002Lys por sí solo.

## 3. Sección 2: candidatos farmacológicos aprobados

### 3.1 Tabla priorizada

“Aprobado” significa que el principio activo tiene al menos una autorización de mercado; **ninguno está aprobado para MVA1 ni para prevenir sus tumores**.

| Fármaco | Mecanismo de la hipótesis | Evidencia/PMID | Estado regulatorio | Seguridad pediátrica relevante | Riesgos principales | Solidez para MVA1 |
|---|---|---|---|---|---|---|
| **Metformina** | Inhibe complejo I, eleva AMP/activa AMPK y reduce mTORC1; sustituto clínico imperfecto de AICAR para explotar estrés energético de células aneuploides | AICAR fue selectivo para aneuploidía: PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/). No es evidencia directa de metformina en MVA | Aprobada para DM2; no para MVA/cáncer | Etiqueta FDA: eficacia/seguridad desde 10 años en DM2 ([FDA](https://www.accessdata.fda.gov/scripts/sda/sdDetailNavigation.cfm?id=950D3034B923A7D3E053564DA8C07E72&sd=labelingdatabase)) | GI, B12, hipoglucemia rara sola; acidosis láctica en insuficiencia renal/hipoxia; podría perjudicar crecimiento/energía en fallo de medro | **Baja–moderada preclínica**, sólo para ensayo celular |
| **Hidroxicloroquina (HCQ)** | Inhibe acidificación lisosomal/autofagia; extrapolación desde cloroquina, que sensibilizó MEF trisómicos junto a AICAR | Cloroquina, no HCQ, en PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/); ensayo metformina+cloroquina en tumores IDH1 no demostró eficacia y tuvo toxicidad: PMID [34069550](https://pubmed.ncbi.nlm.nih.gov/34069550/) | Aprobada (malaria/lupus/AR); no MVA | Amplia experiencia pediátrica en indicaciones autorizadas, pero no como tratamiento crónico de MVA | Retinopatía acumulativa, QT/cardiomiopatía, hipoglucemia, miopatía; margen estrecho en sobredosis | **Baja**, extrapolativa |
| **Everolimus** | Inhibe mTORC1; podría modular hiperactividad mTORC1/sarcopenia asociada a alelos BubR1 y estrés proteostático | Modelo alélico BubR1: PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/). Sin intervención farmacológica demostrada en MVA humana | Aprobado en cáncer/TSC/trasplante según formulación; no MVA | Aprobación pediátrica en TSC (SEGA ≥1 año; crisis ≥2 años): [FDA](https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=283609) | Inmunosupresión/infección, estomatitis, neumonitis, dislipidemia, citopenia, mala cicatrización; interacciones CYP3A4; crecimiento/puberty a largo plazo inciertos | **Baja**, mecanismo indirecto |
| **Sirolimus** | Inhibe mTORC1; misma lógica contextual, con más experiencia inmunosupresora que evidencia MVA | La asociación BubR1–mTORC1 proviene de PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/), no de un ensayo de sirolimus | Aprobado para trasplante y LAM; no MVA | FDA establece uso pediátrico de trasplante sólo en ≥13 años de riesgo bajo-moderado ([FDA](https://www.accessdata.fda.gov/scripts/sda/sdDetailNavigation.cfm?id=14CE032258581B7DE053564DA8C071F2&rownum=683&sd=labelingdatabase)) | Infección, citopenia, dislipidemia, proteinuria/nefrotoxicidad en combinaciones, neumonitis, mala cicatrización | **Muy baja–baja** |

### 3.2 Metformina: el candidato experimental más defendible, no una terapia

Tang et al. cribaron MEF trisómicos isogénicos y hallaron sensibilidad selectiva a **AICAR**, 17-AAG y cloroquina; AICAR indujo apoptosis dependiente de p53 y AICAR+17-AAG tuvo mayor efecto en líneas CIN que en líneas casi euploides (PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/), DOI [10.1016/j.cell.2011.01.017](https://doi.org/10.1016/j.cell.2011.01.017)). **AICAR no es un medicamento aprobado**, por lo que no cumple la regla.

**Inferencia propia:** metformina es un sustituto farmacológico comercializable que produce estrés energético/AMPK, pero no reproduce AICAR de forma limpia (AICAR también se convierte en ZMP y altera metabolismo de nucleótidos). No encontré evidencia primaria de que metformina reduzca la aneuploidía constitucional, restaure el SAC de BubR1 ni prevenga ERMS/Wilms. Por tanto, sólo merece entrar en el panel *in vitro*. En este niño, nefrocalcinosis, posible compromiso renal y fallo de medro elevan la cautela; una intervención crónica sin beneficio demostrado es injustificable.

### 3.3 Hidroxicloroquina: extrapolación de cloroquina

El resultado directo de Tang es con **cloroquina**; su diferencial fue modesto/contextual y se potenció con AICAR (PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/)). HCQ es un análogo aprobado y más usado crónicamente, pero no debe citarse como si hubiera sido el hit del screen. Un pequeño ensayo fase Ib de metformina+cloroquina en tumores sólidos IDH1-mutados mostró factibilidad limitada, progresión frecuente y abandonos por toxicidad, sin validar la hipótesis en CIN/MVA (PMID [34069550](https://pubmed.ncbi.nlm.nih.gov/34069550/)).

**Conclusión:** HCQ es una sonda comparativa aprobada para el experimento, no profilaxis. La miopatía es especialmente indeseable con atrofia muscular; la retina, ECG/QT, electrolitos y función renal serían barreras obligatorias incluso en un estudio clínico futuro.

### 3.4 Eje BubR1–senescencia: por qué no hay hoy un senolítico aprobado aplicable

Ratones hipomorfos BubR1 acumulan aneuploidía, senescencia y fenotipos progeroides (PMID [15208629](https://pubmed.ncbi.nlm.nih.gov/15208629/)). La eliminación genética inducible de células p16^Ink4a+ en esos ratones retrasó sarcopenia, cataratas y pérdida grasa, demostrando causalidad de esas células en parte del fenotipo (PMID [22048312](https://pubmed.ncbi.nlm.nih.gov/22048312/), DOI [10.1038/nature10600](https://doi.org/10.1038/nature10600)).

**Límite crítico:** INK-ATTAC es un sistema transgénico de suicidio celular, no un fármaco trasladable. No hay ningún medicamento aprobado **con indicación senolítica**, ni evidencia de que dasatinib, quercetina, navitoclax u otros eliminen de forma segura las células relevantes en un niño MVA. Además, la senescencia es barrera antitumoral; eliminarla en un síndrome con cáncer predispuesto podría ser perjudicial. **No propongo senolítico.**

### 3.5 mTOR: everolimus antes que sirolimus sólo como herramienta experimental

En modelos alélicos, susceptibilidad a sarcopenia se correlacionó con hiperactividad mTORC1 (PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/)). Esto apoya medir p-S6/p-4EBP1 y probar reversibilidad, no tratar empíricamente. Everolimus tiene la base pediátrica regulatoria más clara (TSC) y formulación pediátrica; sirolimus tiene menos respaldo en niños pequeños fuera de indicación. Ninguno ha restaurado BubR1, el SAC o la estabilidad cromosómica en pacientes MVA. La inmunosupresión y posible aumento de infecciones son especialmente problemáticos en un superviviente de cáncer; mTOR también participa en crecimiento, reparación y respuesta inmune. **Hipótesis:** si el cultivo muestra mTORC1 elevado y everolimus mejora senescencia/función sin aumentar mis-segregación, podría justificar estudios posteriores; no una administración al paciente.

### 3.6 Otras vulnerabilidades CIN/aneuploidía

El estrés proteotóxico es sólido: 17-AAG inhibió HSP90 y fue selectivo en modelos aneuploides (PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/)). Pero **17-AAG/tanespimycin no alcanzó aprobación comercial** y queda excluido. Inhibir directamente SAC, MPS1/TTK, APC/C o PLK4 aumentaría errores cromosómicos y tiene una ventana especialmente peligrosa en BUB1B deficiente. No encontré en CMap/LINCS, ChEMBL, Open Targets ni ClinicalTrials.gov una pareja fármaco–MVA1 con evidencia clínica que cambie esta conclusión; las interfaces no devolvieron un ensayo terapéutico específico de MVA1. Reactome/KEGG sitúan BUB1B en checkpoint mitótico/APC-C y MGI confirma letalidad del nulo y fenotipos de hipomorfos ([Reactome R-HSA-69618](https://reactome.org/content/detail/R-HSA-69618), [KEGG hsa04110](https://www.genome.jp/pathway/hsa04110), [MGI:1333889](https://www.informatics.jax.org/marker/MGI%3A1333889)).

## 4. Sección 3: advertencia clínica sobre quimioterapia y checkpoint deficiente

**Contraindicación relativa, no absoluta.** Vincristina, taxanos y otros venenos del huso dependen de una respuesta mitótica competente para detener células con microtúbulos alterados. Con BubR1 reducido, el arresto es menos robusto: algunas células escapan (“mitotic slippage”), mueren de forma impredecible o generan más aneuploidía. Esto crea dos riesgos opuestos: toxicidad excesiva en tejidos normales vulnerables y respuesta tumoral distinta; no autoriza a omitir una quimioterapia curativa.

La evidencia clínica específica es escasa pero relevante. Nishitani-Isa et al. publicaron un lactante con ERMS y PCS/MVA tratado con quimioterapia de intensidad reducida (vincristina, dactinomicina y ciclofosfamida); es **un caso**, no una guía ni una estimación de seguridad (PMID [31184400](https://pubmed.ncbi.nlm.nih.gov/31184400/), DOI [10.1111/ped.13849](https://doi.org/10.1111/ped.13849)). El tumor MVA analizado por Hanks et al. compartía cambios cromosómicos con ERMS esporádico, pero ello no demuestra tolerancia normal a quimioterapia (PMID [16182441](https://pubmed.ncbi.nlm.nih.gov/16182441/)).

**Aplicación al niño ya tratado:** recuperar dosis, retrasos, neuropatía, mielosupresión, infecciones, mucositis, cardiotoxicidad, función renal y respuesta tumoral; registrar toxicidad por agente. Para recaída o segundo tumor, discutir en comité de predisposición genética y farmacología clínica: dosis inicial individualizada, escalada por tolerancia, vigilancia hematológica/neurológica/renal estrecha y preferencia por control local o agentes no mitóticos cuando sean oncológicamente equivalentes. Evitar la frase “vincristina contraindicada”: es una **precaución de alto nivel** y una contraindicación relativa que se balancea contra probabilidad de cura.

## 5. Sección 4: protocolo de vigilancia oncológica propuesto

La evidencia específica de MVA es de consenso/casos, no de ensayos. Las recomendaciones británicas incluyen a niños con aneuploidía mosaico o variantes BUB1B y proponen ecografía renal cada 3–4 meses desde el diagnóstico hasta los 5 años, porque casi todos los Wilms descritos en esas series ocurrieron antes de 5 años (PMID [17652220](https://pubmed.ncbi.nlm.nih.gov/17652220/)). La revisión contemporánea de síndromes de inestabilidad genómica insiste en un plan individualizado, reducir radiación ionizante y manejar en centros expertos (DOI [10.1158/1078-0432.CCR-24-1101](https://doi.org/10.1158/1078-0432.CCR-24-1101)).

**Propuesta pragmática para este paciente (inferencia clínica explícita):**

| Edad/periodo | Vigilancia | Frecuencia y propósito |
|---|---|---|
| Desde diagnóstico hasta **7 años** | Ecografía abdominal completa con atención a ambos riñones, hígado, retroperitoneo y pelvis | Cada **3 meses**. Extiendo cautelarmente de 5 a 7 años para cubrir Wilms y masas abdominales; la extensión no está validada específicamente en BUB1B |
| Hasta **10 años** | Examen pediátrico/oncológico completo: abdomen, ganglios, cabeza/cuello, órbita, piel, testículos/genitales y partes blandas; búsqueda de masa/dolor/cojera/sangrado | Cada **3 meses hasta 7 años**, luego cada **6 meses hasta 10**; busca ERMS superficial o sintomático, que una US renal sola no cubre |
| Tras ERMS | Seguimiento de recaída según protocolo del tumor y tratamiento recibido | Mantener calendario oncológico específico; coordinarlo para evitar estudios duplicados. La guía de predisposición no sustituye seguimiento de ERMS |
| Toda la infancia | Hemograma con diferencial | Cada **6 meses** es una opción razonable por leucemia reportada, pero **no hay evidencia de beneficio** ni protocolo MVA validado; hacerlo antes ante fiebre, palidez, sangrado, adenopatías o infecciones |
| Toda la vida | Educación familiar y revisión anual en clínica de predisposición | Consulta urgente por masa, hematuria, distensión abdominal, dolor óseo/muscular persistente, déficit neurológico, sangrado o pérdida ponderal; actualizar literatura y antecedentes de segundo cáncer |

**No propongo** AFP seriada (no hay señal específica de hepatoblastoma BUB1B), CT repetida, PET-CT ni whole-body MRI rutinaria sin síntomas: no se ha demostrado beneficio en MVA y la sedación/falsos positivos/coste —más radiación para CT/PET— pesan. Si la edad actual ya supera 7 años, no “recuperar” ecografías omitidas; hacer evaluación basal y decidir continuidad individual por antecedente de ERMS, anatomía renal/nefromcalcinosis y comité experto. La ecografía debe ser realizada por personal pediátrico y cualquier hallazgo confirmarse con MRI preferentemente a CT cuando sea clínicamente válido.

## 6. Sección 5: experimento de validación propuesto

### Pregunta e hipótesis primaria

**Pregunta:** ¿p.Leu737Ter reduce el transcrito/proteína por NMD y p.Asn1002Lys es un hipomorfo C-terminal que disminuye estabilidad de BubR1/PP2A-B56, debilitando SAC y elevando mis-segregación? **Hipótesis farmacológica secundaria:** las células aneuploides resultantes son selectivamente vulnerables a estrés energético/autofágico (metformina/HCQ), mientras everolimus sólo beneficiará si mTORC1 está hiperactivo.

### Diseño realista

1. **Material y controles.** Fibroblastos dérmicos tempranos del paciente; dos controles sanos emparejados; un control MVA/BUB1B conocido si se consigue. Crear por CRISPR en una línea diploide isogénica los genotipos WT, Leu737Ter/+, Asn1002Lys/+ y compuesto. En paralelo, corregir cada alelo por separado en células del paciente. Usar ≥3 clones independientes y, para evitar artefactos clonales, un pool editado.
2. **Destino de alelos.** RNA-seq de lectura larga o RT-PCR/Sanger alelo-específico; cuantificar razón mutante/WT. Tratar una réplica 4–6 h con inhibidor de NMD sólo como reactivo experimental y observar rescate del transcrito Leu737Ter. Western cuantitativo N- y C-terminal: una banda N+/C− apoyaría truncación; pérdida de ambas, NMD/inestabilidad.
3. **Función molecular.** Co-IP de BubR1–Bub3 y BubR1–B56; inmunofluorescencia en cinetocoros; p-S6 y p-4EBP1 para mTORC1. Con nocodazol a baja dosis, medir tiempo de NEBD a anafase por live imaging H2B-mCherry/tubulina-GFP y mantenimiento de arresto; cuantificar cromosomas desalineados.
4. **Fidelidad cromosómica.** 200 mitosis/condición para lagging chromosomes, puentes y micronúcleos; FISH de 3–5 cromosomas y scDNA-seq de baja cobertura al inicio y tras 20 pases. La literatura de pacientes y modelos justifica estos endpoints (PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/), [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/)).
5. **Rescate causal.** Introducir BUB1B-WT a expresión cercana a endógena (promotor débil/knock-in seguro), no sobreexpresión masiva. La corrección de Asn1002Lys debería recuperar estabilidad/PP2A-B56; la corrección de Leu737Ter debería elevar cantidad total. Rescate convergente valida causalidad.
6. **Mini-screen de medicamentos aprobados.** Matriz de metformina, HCQ y everolimus a exposiciones clínicamente alcanzables, solos y metformina+HCQ; 72 h y 14 días. Medir viabilidad, apoptosis, proliferación, SA-β-gal/p16/p21/SASP, p-AMPK/p-S6 y, crucialmente, tasa de mis-segregación. Incluir cloroquina, AICAR y 17-AAG **sólo como controles mecanísticos no trasladables**, nunca como candidatos del hackathon.
7. **Criterio de avance predefinido.** Un candidato avanza sólo si muestra ventana ≥3 veces entre compuesto/aneuploide y WT/corregido en ≥2 fondos isogénicos, reproduce el efecto en fibroblasto del paciente, no aumenta micronúcleos/mis-segregación en supervivientes y funciona a exposición humana plausible. Everolimus requiere además mTORC1 basal elevada y reversión de ese biomarcador. Replicar por laboratorio independiente antes de cualquier modelo animal.

**Resultado falsador:** si la corrección de Asn1002Lys no rescata BubR1/SAC, o si el compuesto editado no difiere del WT, la hipótesis de hipomorfismo específico queda debilitada. Si metformina/HCQ mata por igual controles y paciente o aumenta CIN residual, se descarta. Esto evita seleccionar un fármaco únicamente porque reduce crecimiento celular.

## 7. Lo que NO propondría y por qué

- **MPS1/TTK inhibitors (incluido reversine):** fármacos experimentales/tool compounds; no aprobados y debilitan directamente un checkpoint ya insuficiente, con riesgo de aumentar CIN.
- **Apcin y proTAME:** herramientas de APC/C, no medicamentos comercialmente aprobados; sin seguridad pediátrica ni evidencia MVA.
- **DCZ0415:** inhibidor experimental de TRIP13; no aprobado y no corrige la deficiencia BUB1B.
- **AICAR:** fue hit real del screen de Tang, pero no es medicamento aprobado. Puede ser control positivo *in vitro*, no candidato (PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/)).
- **17-AAG/tanespimycin:** evidencia preclínica sólida de estrés proteotóxico, pero no consiguió aprobación de mercado; excluido por regla dura (PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/)).
- **Senolíticos (dasatinib+quercetina, navitoclax, fisetina):** ninguno está aprobado con indicación senolítica; evidencia del BubR1 mouse es eliminación genética p16+, no equivalencia farmacológica. Riesgo de citopenia, interacción oncológica y de retirar una barrera antitumoral.
- **Vincristina/taxanos como “terapia de MVA”:** son antineoplásicos, no correctores de MVA; constituyen una precaución/contraindicación relativa por checkpoint deficiente. Sólo pueden usarse para una indicación oncológica con balance de cura y toxicidad.
- **Inhibidores Aurora B/PLK1 o inductores de aneuploidía:** aunque puedan matar tumores CIN, agravan el defecto fundamental y carecen de evidencia de prevención segura en células constitucionalmente afectadas.
- **Metformina, HCQ o rapalogs directamente al paciente fuera de ensayo:** que estén aprobados no elimina el salto entre cultivo y niño; no hay biomarcador validado, dosis MVA ni beneficio clínico.

## 8. Qué no pude verificar

- No encontré publicación funcional específica para **p.Leu737Ter** ni **p.Asn1002Lys**; por ello NMD, estabilidad e impacto de Asn1002Lys se etiquetan como hipótesis y son objetivos experimentales.
- No pude verificar una correlación cuantitativa alelo–tumor (ERMS versus Wilms) para estos cambios ni una comparación clínica robusta “truncante+missense versus dos truncantes”. La literatura y los modelos apoyan heterogeneidad alélica, no predicción individual.
- Open Targets, ChEMBL y CMap/LINCS no ofrecieron una asociación clínica BUB1B–fármaco específica de MVA1 en la búsqueda web accesible; DrugBank no fue accesible en profundidad sin licencia/inicio de sesión. No interpreto ausencia de resultado de interfaz como prueba de ausencia absoluta.
- ClinicalTrials.gov no devolvió un ensayo terapéutico específico de MVA1/BUB1B identificable. No existe, en lo revisado, un ensayo de metformina, HCQ, sirolimus o everolimus en esta enfermedad.
- No pude consultar el texto íntegro del caso PMID 31184400 desde el editor; verifiqué título, autores, revista, DOI, sustancias indexadas y que describe intensidad reducida, pero no reconstruyo dosis ni toxicidades no visibles en el registro.
- Las recomendaciones modernas de AACR para trastornos de inestabilidad genómica incluyen MVA, pero el texto completo quedó bloqueado por el sitio del editor. La pauta renal específica citada procede de la guía publicada (PMID 17652220); extender hasta 7 años y añadir examen/hemograma es una propuesta cautelar explícita, no consenso BUB1B validado.
- OMIM fue identificable como **MVA1 257300**, pero su ficha completa requiere acceso institucional. Reactome, KEGG y MGI sí fueron accesibles. Las etiquetas FDA se verificaron; no se hizo una comparación país por país de autorizaciones EMA/autoridades panameñas.
- No hallé datos que justifiquen prevención farmacológica del segundo cáncer después de ERMS. La recomendación de mayor solidez permanece vigilancia, educación de síntomas y planificación individual de cualquier quimioterapia.

---

### Referencias primarias clave (índice rápido)

1. Hanks S, et al. Constitutional mutations in BUB1B cause MVA and cancer predisposition. *Nat Genet* (2004). PMID [15475955](https://pubmed.ncbi.nlm.nih.gov/15475955/).
2. Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in MVA. *Cancer Res* (2010). PMID [20516114](https://pubmed.ncbi.nlm.nih.gov/20516114/).
3. Hanks S, et al. Childhood cancers associated with MVA. *Cancer Lett* (2006). PMID [16182441](https://pubmed.ncbi.nlm.nih.gov/16182441/).
4. Tang YC, et al. Aneuploidy-selective antiproliferation compounds. *Cell* (2011). PMID [21315436](https://pubmed.ncbi.nlm.nih.gov/21315436/); DOI [10.1016/j.cell.2011.01.017](https://doi.org/10.1016/j.cell.2011.01.017).
5. Baker DJ, et al. BubR1 insufficiency and progeroid phenotypes. *Nat Genet* (2004). PMID [15208629](https://pubmed.ncbi.nlm.nih.gov/15208629/).
6. Baker DJ, et al. Clearance of p16-positive senescent cells. *Nature* (2011). PMID [22048312](https://pubmed.ncbi.nlm.nih.gov/22048312/); DOI [10.1038/nature10600](https://doi.org/10.1038/nature10600).
7. Sieben CJ, et al. BubR1 allelic effects in MVA. *J Clin Invest* (2020). PMID [31738183](https://pubmed.ncbi.nlm.nih.gov/31738183/); DOI [10.1172/JCI126863](https://doi.org/10.1172/JCI126863).
8. Nishitani-Isa M, et al. ERMS with PCS/MVA: reduced-intensity chemotherapy. *Pediatr Int* (2019). PMID [31184400](https://pubmed.ncbi.nlm.nih.gov/31184400/); DOI [10.1111/ped.13849](https://doi.org/10.1111/ped.13849).
9. Scott RH, et al. Wilms surveillance recommendations. *Arch Dis Child* (2006). PMID [17652220](https://pubmed.ncbi.nlm.nih.gov/17652220/).

