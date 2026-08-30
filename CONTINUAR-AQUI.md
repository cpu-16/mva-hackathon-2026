# 🔄 CONTINUAR AQUÍ — estado del MVA Hackathon 2026

**Última actualización: 30-ago-2026 (tarde).** Documento de traspaso tras un `/clear`.
Léeme completo antes de tocar cualquier otro archivo.

---

## 🗺️ MAPA DE ARCHIVOS — hay 44 `.md` en este proyecto, esto es lo que manda

**Regla: si dos archivos se contradicen, gana el de esta tabla.**

| Necesitas… | El archivo que MANDA | Ojo |
|---|---|---|
| Estado general y qué sigue | **este archivo** | — |
| Reporte Track 1 (enviado) | `entrega/methods_track1.md` + `.pdf` | ⛔ `methods_track1_DRAFT.md` es histórico, NO usar |
| Reporte Track 2 (sin enviar) | `track2/REPORT_track2_EN.md` + `REPORT_track2.pdf` | ⛔ `REPORT_track2_EN_v1_ARCHIVO.md` es viejo, NO usar |
| Formulario de métodos | `entrega/methods_description_form_ciberpty.xlsx` | las dos hojas ya están al día |
| Q2–Q11 del Track 2 en texto | `entrega/methods_track2.md` | espejo del xlsx, mantener sincronizados |
| CSV de predicciones | `entrega/convergent-hpo-genomewide-and-panel.csv` | epcr 0.85, verificado = 100 pts |
| Análisis DepMap (lo nuevo) | `depmap/PREREGISTRO.md` → `depmap/RESULTADOS.md` | leer en ese orden |
| Video | `video/GUION.md` (v3) + `video/README.md` | ⛔ `GUION_v1.md` es histórico |
| Qué se envió y cuándo | `evidencia/registro_envios_track1.md` | — |
| Obligación de borrar datos | `data/BORRAR-AL-TERMINAR.md` | **fecha límite 23-nov-2026** |

**Carpeta `evidencia/`: es archivo histórico, no fuente de verdad.** Son las revisiones de Codex y
Cursor de cada ronda y los abstracts verbatim. Útil para *no repetir* una verificación ya hecha o para
citar de dónde salió una corrección. No tomes decisiones leyendo solo de ahí: varias afirmaciones en
esos archivos fueron *refutadas* en rondas posteriores.

**Archivos de trabajo del Track 2** (`track2/DATOS_CANDIDATO.md`, `dossier_mecanismo_farmacos.md`,
`CANDIDATOS_FARMACOCINETICA.md`, `ESTRATEGIA.md`, `SECCION_FILTRO_PK.md`): son el material crudo del
que salió el reporte. Consúltalos para verificar de dónde salió un número — de hecho **el error más
grave de cada ronda siempre fue una afirmación del reporte que contradecía uno de estos archivos**.

**Superados pero no borrados:** `HALLAZGOS.md`, `RESUMEN-NOCHE.md`, `INFORME.md` (la investigación
inicial de si valía la pena entrar). `MOSAICISMO.md` sigue siendo correcto y es la fuente del §5.

---

## 🧪 DEPMAP — el primer resultado PROPIO del proyecto (30-ago, tarde)

**Motivo:** los dos jueces dijeron lo mismo — *"todo lo que tienen es razonamiento, no produjeron
ningún resultado"*. Esto lo corrige.

**Qué se hizo:** puntuación de aneuploidía por brazo cromosómico para 2.420 líneas de DepMap 24Q4, y
correlación contra sensibilidad a fármacos (PRISM Repurposing) y dependencia genética (CRISPR).
**Todo público, CPU, sin datos del paciente y sin GPU.**

**⚠️ Lo más importante del método: se PRE-REGISTRÓ.** Hipótesis, lista de 7 fármacos, direcciones
predichas, estadístico y reglas de parada se escribieron en `depmap/PREREGISTRO.md` y se commitearon
**antes de correr nada** (commit `4b0b7c2`). Cuando a mitad se descubrió que H2 era imposible de
probar, se anotó como enmienda fechada (`c54e678`) **sin editar el original**. Ese es el activo: el
timestamp de git. No romper esa cadena.

**EL RESULTADO VA EN CONTRA NUESTRA, y eso es lo valioso:**

| Medida | Sólidos | Hematológicas |
|---|---|---|
| Inhibidores del proteasoma (PRISM, n=444) | **ninguno pasa FDR<0.05** | no medible (ver abajo) |
| Dependencia de PSMB5 (CRISPR) | ρ=−0.077, q=0.118 **n.s.** (n=833) | ρ=−0.261, **q=0.042** (n=113) |

**Interacción aneuploidía × linaje: p=0.026.** La asociación es genuinamente más débil en tumores
sólidos, y los sólidos son el grupo *más grande* — es atenuación, no falta de potencia. La ploidía
queda descartada como confusor (p=0.88). El tumor de este niño fue sólido.

**Controles que se hicieron (no repetirlos, ya están):**
- El score discrimina: MSI/estables 5.0 brazos alterados (DLD1=0) vs CIN 16.5 (HT29=21).
- El pipeline no está ciego: de 6.790 compuestos, 1.1% llegan a p<0.001 vs 0.1% esperado por azar.
- Control negativo declarado (PSMD9): nulo en todas partes.
- Paclitaxel (control citotóxico) va en dirección opuesta → no es confusor de "célula enferma".

**Gotcha que costó tiempo:** los 7 fármacos SOLO existen en el cribado `REP.PRIMARY` de PRISM, que
usó una colección adherente. De 98 líneas hematológicas con score, **cero** tienen dato de bortezomib.
Por eso H2 no se pudo probar con fármacos y hubo que extender a CRISPR. El archivo que sirve es
`Repurposing_Extended_Primary_Matrix.csv`, **no** el `LFC_COLLAPSED` (ese es REP1M/REP300, sin
nuestros fármacos). Y los IDs de la columna `IDs` ya vienen con el prefijo `BRD:` — no duplicarlo.

**Dónde quedó:** integrado en el reporte (resumen ejecutivo, nueva **§3.5** con `fig4_depmap.png`, y
condicionando el §4). Scripts reproducibles en `depmap/01..04_*.py`. Los datos crudos (`depmap/raw/`,
~700 MB) están en `.gitignore`; se rebajan de figshare (DepMap 24Q4 = 27993248, PRISM 24Q2 = 25917643).

---

## 🎬 VIDEO v3 — regrabado el 30-ago (⚠️ el que subiste a YouTube es el VIEJO)

El guion contradecía el reporte de la ronda 7. Se regrabaron S3, S5, S7 y S8:

| Slide | Decía | Dice ahora |
|---|---|---|
| S3 | "once controles… convulsiones, hipoacusia, un defecto cardíaco" como no relacionados | "doce controles… **atrapamos nuestro propio error**" |
| S5 | "muere en el filtro tres… la rechazamos con un número" | "no puede evaluarse en el mecanismo propuesto" |
| S7 | la vigilancia como propuesta nuestra | "**consenso publicado**: ultrasonido renal cada 3 meses, hasta los 7" |
| S8 | "experimento… que podría matarlo" | "un experimento que **podría fallar**" |

`video/pitch_MVA2026.mp4` · **2:59.0** (límite 3:00, margen 1.0 s).

**Dos gotchas documentados en `video/README.md` — leerlos antes de tocar el video:**
1. El Piper instalado habla 15% más rápido que el de la grabación original. **Usar siempre
   `--length-scale 1.415`**, o las secciones nuevas desentonan con las viejas.
2. Al ensamblar hay que fijar **`-t <duración de narracion.wav>`**. El truco de repetir la última
   slide la duplica (salía 3:22) y `-shortest` deja 3 s de padding del AAC (salía 3:02).

**Verificación hecha:** se transcribió el audio final con Whisper local y se comprobaron las dos
direcciones — las frases nuevas están y "seizure", "hearing loss", "heart defect", "eleven controls",
"could kill it" dan **0 ocurrencias**. Transcripción en `evidencia/video_transcripcion_verificacion.txt`.

---

## 🎯 PLAN PARA EL PODIO — hecho con Codex y Cursor, quedan ~8 semanas (cierre 24-oct)

Los dos jueces puntuaron con la rúbrica oficial. **Codex 72→78, Cursor 65→74** tras la ronda 7.
Lo que falta ya no es argumento, es *resultado*. DepMap fue el primero. Lo que sigue, en orden:

| Prioridad | Qué | Días | Estado |
|---|---|---|---|
| ~~1~~ | ~~Prueba pre-registrada DepMap/PRISM~~ | 4–6 | ✅ **HECHO 30-ago** |
| 2 | **MVA-Replay**: 30–50 casos sintéticos sobre un VCF público (GIAB) para medir sensibilidad y tasa de falsos positivos del pipeline del Track 1 | 4–6 | pendiente |
| 3 | **Fase estadística** de las dos variantes BUB1B (Beagle/SHAPEIT contra panel 1000G) | 2–5 | pendiente · los dos agentes avisan que probablemente salga *no concluyente*; reportarlo así si pasa |
| 4 | **Potencia del experimento del §6**: ¿el ensayo en fibroblastos está siquiera en el régimen de efecto correcto? | 2–3 | pendiente |
| 5 | **Calibración del VUS p.Asn1002Lys** (ΔΔG contra set de variantes BUB1B ya clasificadas) | 5–7 | pendiente · **abortar si el pLDDT de AlphaFold en 766–1050 < 70**; un ΔΔG sobre estructura dudosa es teatro |
| 6 | Motor ejecutable de los cinco filtros | 7–10 | solo si algo de lo anterior produce denominadores utilizables |

Planes completos de cada agente: `evidencia/` (los briefs `brief_*` y las respuestas de esta ronda).

**Ideas que los dos agentes MATARON — no reintentarlas:**
farmacogenómica de bortezomib desde el VCF (no hay regla clínica validada; hay una revisión de 2026,
PMID 42494534, titulada literalmente *por qué fallan* esos biomarcadores), dashboards, más revisión
bibliográfica, predicción aislada con AlphaMissense/SIFT/PolyPhen sin calibrar, y volver a inferir
aneuploidía desde BAF (el límite de detección ya está calculado y es demasiado alto).

---

## ⛔ LO ÚNICO QUE BLOQUEA EL ENVÍO DEL TRACK 2

**La URL del video en YouTube o Vimeo.** `submit_track2.py:92-94` la exige y rechaza el envío sin
ella. Gilberto la sube. **Que suba el video v3, no el viejo.** Cuota Track 2: 3 envíos.
Renombrar el PDF a `ciberpty_track2_report.pdf` (ya está en el scratchpad de envío).

Flujo de envío probado y funcionando: `brave-cdp` → pestaña Submit → `tools/fill_form_space.py`
(CDP por **una sola** sesión websocket; los `nodeId` no sobreviven entre llamadas de `chrome-agent`).

---

## ✅ TRACK 1 REENVIADO CORREGIDO — 30-ago-2026 (envío 2 de 6)

Segundo envío con el reporte corregido: **100/100, F-max 1.000, full match rank 1. Cuota 2/6.**
Motivo del reenvío: el control de "HPOs no relacionados" estaba contaminado — dos de los cinco
términos (convulsiones HP:0001250 y comunicación interauricular HP:0001631) **sí están anotados a
MVA1** en la HPO (verificado en ontology.jax.org, 59 anotaciones). Re-corrí Exomiser con cinco
términos verificados como ausentes (hipoacusia, conjuntivitis, infecciones respiratorias, cefalea,
prurito): **BUB1B sigue rank 1 de 4.565 genes, score 0.4187** vs 0.5506 del contaminado. La
conclusión "variant-driven" se sostiene con control limpio, y el delta cuantifica el aporte del
fenotipo: ~24% del score, sin cambio de rango. Script: `tools/control_hpo_r7.sh`.

⚠️ **El leaderboard público está congelado desde el 26-ago 18:50 UTC** — no muestra ningún envío del
27 al 30, ni el nuestro ni el de nadie. Es del Space (`load_leaderboard` devuelve el caché si
`snapshot_download` falla), no del envío: la cuota (que lista archivos reales) dice 2/6.
Detalle en `evidencia/registro_envios_track1.md`.

## 📊 TRACK 2 revisado a fondo (ronda 7) — LISTO, FALTA EL VIDEO

Dos jueces con la rúbrica oficial (Rigor 35 / Impacto 25 / Innovación 25 / Escalabilidad 15),
dos pasadas cada uno: **Codex 72 → 78, Cursor 65 → 74.**

Evidencia nueva encontrada (toda verificada contra PubMed, autores incluidos):
- **PMID 39264246** (Clin Cancer Res 2024, AACR): consenso **específico de MVA** — "renal ultrasound
  every 3 months from birth until age 7, for all MVA conditions". Nuestro §7 lo presentaba como
  inferencia propia. Era el hueco más grave; ahora se cita como consenso.
- **PMID 42595739** (2026): niña con MVA3, Wilms a los 3 y ERMS orbitario a los **12** — fuera de la
  ventana del consenso y en un sitio que el ultrasonido renal no ve. Es el hueco que aportamos.
- **PMID 42094535** (2026, preprint bioRxiv): cribados CRISPR pareados nombran subunidades del
  proteasoma como dependencia aneuploide-específica → confirmación ortogonal de Ippolito. UBE2H como
  blanco futuro.
- **PMID 42434306** (2026): portadores heterocigotos de BUB1B con PCS elevada y abortos recurrentes →
  ángulo para los padres (HP:0200067 está en el documento clínico). Accionable y barato.
- **PMID 41248159** (2025): carga traduccional → envejecimiento; sostiene la premisa del antagonismo mTOR.

Añadido: página **"Read this first"** en lenguaje llano al inicio del documento, figura del embudo de
cinco filtros (`fig3_funnel.png`), apéndice con hoja de trabajo reutilizable. PDF: 29 páginas.

⛔ **Para enviar el Track 2 falta la URL del video en YouTube/Vimeo** — el formulario la exige y
rechaza el envío sin ella (`submit_track2.py:92-94`). Gilberto lo está subiendo. Cuota Track 2: 3.
Archivo listo: `track2/REPORT_track2.pdf` → renombrar a `ciberpty_track2_report.pdf`.

---

## ✅ TRACK 1 ENVIADO (envío 1) — 30-ago-2026 ~10:22 (hora Panamá)

Enviado desde el Space con la cuenta HF `cpu-16` (sesión de Brave vía chrome-agent), equipo `ciberpty`.
**Resultado del evaluador: Rank points 100/100 · F-max 1.000 · EPCR threshold 0.85 · Full match at rank 1.**
Cuota: 1/6 usados. Screenshot: `evidencia/envio_track1_2026-08-30.png`.

Archivos enviados (con el nombre de equipo, como pide el Space):
- `ciberpty_convergent-hpo-genomewide-and-panel.csv` (idéntico a `entrega/convergent-hpo-genomewide-and-panel.csv`)
- `ciberpty_track1_report.pdf` (= `entrega/methods_track1.pdf`, 12 pp, regenerado tras la 6ª ronda)
- URL: https://github.com/cpu-16/mva-hackathon-2026

**6ª ronda (30-ago, Codex + Cursor en paralelo, brief en `evidencia/`):** ambos dieron SAFE salvo un
"bloqueador" de Codex (los AD/DP de 4 variantes nombradas) que NO lo es — `rules.py:104` permite publicar
derived outputs; se dejó. Sí se aplicaron 9 correcciones: "Diagnosis… caused by" → "Interpretation…
consistent with… (phase not demonstrated)"; bloque Q23 duplicado borrado; "313 residues before the
kinase domain" → "removes the C-terminal 313 residues, including the kinase domain"; "biallelic null being
lethal" retirado del Track 2 (contradecía el Track 1); 2.75× → 2.59× (el ratio del resultado AR, 2.75×
es el del artefacto AD; el README decía "~4×", también corregido); "Total analysis time 53 s" → "the
genome-wide Exomiser run took 53 s"; encabezado "phenotype-driven" → "genome-wide, phenotype-informed";
tono del abstract Track 2 ("is nothing" → "no disease-modifying drug can be recommended"); mayúscula.
Todo en md + xlsx + PDF + repo.

**El repo estaba desactualizado** (CSV con epcr 0.95, DRAFT, README con datos viejos): sincronizado y
pusheado en dos commits (`38fedbf`, `6f18f70`). Sigue privado; **hacerlo público al cerrar el hackathon**.

### Lo que queda
1. **Track 2**: se envía por la pestaña "Submit - Track 2" (reporte `track2/REPORT_track2.pdf` + formulario).
   Renombrar a `ciberpty_track2_report.pdf`. Mismo flujo con chrome-agent (`fill_form.py` en el scratchpad de
   esa sesión; hay que reescribirlo: CDP por websocket en una sola sesión porque los nodeId no sobreviven
   entre llamadas de chrome-agent).
2. Chequeo de un minuto: compartir datos para entrenamiento en OFF en Anthropic y OpenAI (la Q23 lo afirma).
3. Opcional: regrabar la voz del video.
4. Hacer público el repo al cierre (24-oct-2026).
5. Borrar `data/` antes del **23-nov-2026** + correo a Synapse.

---

## Lo esencial en diez líneas (estado al 29-ago)

- Gilberto **está inscrito** y con acceso al dataset (cuenta HF `cpu-16`). Cierre: **24-oct-2026**.
- **Track 1 resuelto:** BUB1B heterocigoto compuesto → MVA1 (OMIM 257300).
- ~~TODO LISTO PARA ENVIAR. NADA SE HA ENVIADO TODAVÍA~~ **Track 1 ENVIADO el 30-ago** (ver arriba). El envío lo hizo chrome-agent con la sesión HF de Gilberto
  logueado en el Space con su cuenta HF; nadie más puede.
- El CSV está verificado contra el evaluador real del hackathon: **100 pts, F-max 1.0**.
- Un `proband_id` equivocado **no consume cuota** (verificado leyendo su código) → se puede probar sin riesgo.
- **Track 1: el write-up quedó listo** (`entrega/methods_track1.md`, inglés limpio, 3.241 palabras,
  abstract Q12 en 478/500). Los 6 errores numéricos y 3 más están corregidos.
- **Track 2: 24 correcciones aplicadas** tras la tercera revisión de Cursor. PDF de 18 páginas hecho.
  Las dos figuras estaban **en español dentro de un reporte en inglés** — ya traducidas.
- **5ª ronda: auditoría afirmación↔fuente** (`evidencia/auditoria_claims_r5.md`). Método nuevo: **yo
  bajo los abstracts y se los doy a los agentes emparejados con la afirmación**, en vez de pedirles
  que busquen — antes fallaban por acceso (ver [[feedback-agentes-verificacion]] en memoria).
  9 correcciones más; la peor: usábamos 28553959 para extender la vulnerabilidad proteotóxica a
  CEP57, y **esa misma fuente lo desmiente** ("not associated with embryonal tumors", "minimal SAC
  deficiency"). Dos hallazgos que FORTALECEN: Sieben modeló L1012P+X753, nuestra misma arquitectura
  alélica; y el paper de mTORC1 explica el fracaso de bortezomib en ovario, objeción que ahora
  declaramos nosotros.
- **4ª ronda: verificación numérica desde los datos crudos** (`evidencia/verificacion_numerica_r4.md`).
  3 errores más encontrados y corregidos: los HPOs del control ajeno no eran los declarados
  ("cataratas" nunca se usó), el umbral 0.005 no era "la dispersión medida" (la SD real es 0.0035), y
  el conteo de registros del VCF confundía «cargadas por Exomiser» con «registros del archivo».
  Confirmados: las 9 conversiones farmacológicas, las 1.532 del panel, los 11 controles, chr21 como
  mayor desviación de dosis, el Poisson de 0,03 % y el GC r=0,43.
- `epcr` bajado a **0.85** (decisión de Gilberto, 29-ago).
- Q23 resuelta: Anthropic **Max**, OpenAI **Plus**, Cursor **Pro** (Privacy Mode verificado) + Piper
  TTS local. Equipo: **ciberpty**.
- **Obligación legal:** borrar los datos del paciente antes del **23-nov-2026** + correo a Synapse.

---

## 1. Estado de los tres requisitos para enviar el Track 1

**Nombre del equipo: `ciberpty`** (decisión de Gilberto, 29-ago). Ya está en los dos reportes y en
las dos hojas del formulario.

| Requisito | Estado | Dónde |
|---|---|---|
| CSV de predicciones | ✅ **Listo y verificado** (epcr 0.85, notas corregidas) | `entrega/convergent-hpo-genomewide-and-panel.csv` |
| URL de GitHub | ✅ **Listo** | https://github.com/cpu-16/mva-hackathon-2026 (privado; debe hacerse público al cerrar el hackathon) |
| Reporte Track 1 | ✅ **LISTO** | `entrega/methods_track1.md` + `.pdf` (12 pp) |
| Reporte Track 2 | ✅ **LISTO** | `track2/REPORT_track2.pdf` (18 pp) + `entrega/methods_track2.md` |
| Formulario de métodos | ✅ **LISTO, ambas hojas** | `entrega/methods_description_form_ciberpty.xlsx` |
| Video de 3 minutos | ✅ **LISTO** | `video/pitch_MVA2026.mp4` (2:56.5) |

El envío se hace desde la pestaña "Submit — Track 1" del Space, logueado con la cuenta HF.

---

## 2. ⛔ LO QUE FALTA

### 2.1 La Q23 — ✅ RESUELTA

Declaración cerrada con los planes que dio Gilberto el 29-ago: **Anthropic Max, OpenAI Plus, Cursor
Pro** (Privacy Mode verificado localmente) + Piper TTS local. Está en `entrega/methods_track1.md`
(Q23), en `entrega/methods_track2.md` (Q3) y en las dos hojas del formulario.

**Único chequeo que queda, de un minuto:** confirmar en los ajustes de privacidad de Anthropic y de
OpenAI que el compartir datos para entrenamiento está en OFF. La declaración lo afirma; hay que
poder sostenerlo.

### 2.2 El video de 3 minutos — ✅ HECHO

`video/pitch_MVA2026.mp4` — 2:56.5, 1920×1080, 8 slides, narración con Piper TTS local
(`en_US-ryan-high`). Guion en `video/GUION.md`. Todo documentado en `video/README.md`.

**Vale la pena considerar regrabar la voz con la de Gilberto** — el panel incluye defensores de
pacientes y una voz humana pesa distinto. El README trae el procedimiento: grabar 8 WAV y correr un
bloque de ffmpeg. No hay que tocar las slides.

El guion v2 nació de una crítica cruzada de Codex y Cursor a la v1: cubría bien Rigor (35%) e
Innovación (25%) pero dejaba fuera **Impacto (25%)** —faltaba la vigilancia, que es lo único que
cambia el pronóstico hoy— y **Escalabilidad (15%)**, que no aparecía en absoluto. Ambas ya están.

### 2.3 Opcional: PDF del Track 1

El Track 2 ya tiene su PDF (`track2/REPORT_track2.pdf`, 18 páginas A4). El Track 1 se puede enviar
como `.md`; si se quiere PDF, mismo comando:

```bash
cd track2 && pandoc ../entrega/methods_track1.md -f markdown -t html5 --standalone -o /tmp/t1.html
python3 -c "from weasyprint import HTML,CSS; HTML('/tmp/t1.html', base_url='.').write_pdf('../entrega/methods_track1.pdf',stylesheets=[CSS('report.css')])"
```

**Gotcha:** pandoc duplica el título si se pasa `--metadata title` y el MD ya tiene un H1. Usar uno u
otro. Avisa de `<title>` vacío; es inofensivo.

---

## 3. Hallazgos que NO hay que volver a derivar

### Track 1 — la respuesta

**BUB1B, heterocigoto compuesto** (MVA1, OMIM 257300, autosómico recesivo):

- `chr15:40209701 T>G` · `c.2210T>G` · **p.Leu737Ter** — nonsense. ClinVar 533901 Patogénica.
- `chr15:40220612 T>G` · `c.3006T>G` · **p.Asn1002Lys** — missense. **No está en ClinVar**
  (ClinVar tiene `c.3006T>A`, otro nucleótido con el mismo cambio proteico, VUS — **no transfiere**).

Confirmado por dos métodos: panel dirigido de 11 genes (único gen con dos alelos raros dañinos, de
1.532 variantes solo 3 pasaron) y Exomiser genome-wide (rank 1-2 de 3.139 genes, 53 segundos).

### Los controles de robustez — resultado mixto, reportarlo honestamente

`tools/logs/controles_hpo.log`, 11 corridas de Exomiser:

- **Leave-one-HPO-out (8 corridas): BUB1B rank 1 en TODAS.** Incluso quitando el rabdomiosarcoma
  sube a 0.7503. El hallazgo no depende de ningún síntoma aislado. ✅
- **HPOs completamente ajenos: BUB1B TAMBIÉN sale rank 1.** ⚠️ Los cinco términos reales
  (`tools/control_hpo.sh:68`) son convulsiones HP:0001250, hipoacusia HP:0000365, comunicación
  interauricular HP:0001631, conjuntivitis HP:0000509 e infecciones respiratorias HP:0002205.
  ⛔ **No decir "cataratas"** — no se usó ese término; el reporte lo decía y era falso (corregido 29-ago).

**Consecuencia obligatoria:** no se puede llamar "descubrimiento guiado por fenotipo". La señal viene
de la **variante** (nonsense patogénico con whitelist de ClinVar), no del fenotipo. La formulación
honesta es **"variant-driven, phenotype-consistent"**: el fenotipo sirve para distinguir el modelo de
herencia correcto (AR → MVA) del artefacto (AD → cáncer colorrectal).

Este control nos quita un argumento. Hay que reportarlo igual — un panel lo detectaría.

### Mosaicismo — negativo con límite calculado

`MOSAICISMO.md`. **No** demostramos que no haya mosaicismo (lo hay, por definición diagnóstica).
Demostramos que **este ensayo no puede resolverlo**: límite de detección ~12–15% de células para una
trisomía clonal (la simulación da 14.1%), y la variegación deja cada cromosoma en **1–2% de las
células = 6–15× por debajo**. ⚠️ El "6–14×" de la versión anterior **no salía de ninguna aritmética**
(30%/22 cromosomas = 1.4%, y 12/1.4 = 8.6, 15/1.4 = 10.7). Corregido en ambos reportes.

⚠️ **El argumento de Poisson había que enunciarlo mejor:** el 0.03% es el error de muestreo del test
de *dosis*, mientras el LOD declarado es de |BAF − 0.5| contra el ruido entre cromosomas. Son dos
estadísticos distintos. La forma correcta: la simulación ya resta la línea base binomial a DP 44, así
que el umbral de 0.005 que hay que superar es la **dispersión medida entre cromosomas** (sesgo de
librería), no ruido de conteo. Ambas rutas coinciden en que más profundidad no movería el límite.

*Corrección importante ya aplicada:* la primera versión usaba el % de sitios fuera de 0.38–0.62, un
estadístico dominado por la cola binomial (a 44× y sin mosaicismo, 9.7% cae fuera solo por azar).
No tenía potencia. Ahora usa la media de |BAF − 0.5| con cálculo de potencia por simulación.

### Track 2 — el candidato

**Metformina descartada con un número:** plasma micromolar vs. milimolar necesario para inhibir el
complejo I = **~1000× de déficit** (PMID 37343530, verificado). Es el candidato que van a proponer
los demás equipos.

⚠️ **Declarar qué clase de número es.** Para bortezomib el filtro 3 es un `Cmax/EC50` real contra una
EC50 medida en un modelo estratificado por aneuploidía. Para metformina **no existe esa EC50**: el
1000× compara *rangos de concentración*, no la misma cantidad.

⛔ **NO usar PMID 22890317 como evidencia contra la metformina.** Ese paper es sobre **AICAR** y no
menciona metformina; además muestra que la célula trisómica es **4× MÁS sensible a AICAR**. La fila
de `DATOS_CANDIDATO.md` que se lo atribuía a metformina era falsa y ya está corregida. Verificado
contra el abstract real de PubMed el 29-ago.

**Bortezomib es el candidato que sobrevive:**
- Ippolito 2024, *Cancer Discovery*, **PMID 39247952** (verificado): las células aneuploides dependen
  del proteasoma, y **el nivel de aneuploidía se asoció con la respuesta de pacientes de mieloma a
  inhibidores del proteasoma** — señal clínica humana, no solo cultivo.
- EC50 <40 nM en líneas aneuploides vs Cmax **89–120 ng/mL = 231–312 nM** (1,3 mg/m² IV) =
  **margen 5,8–7,8×**. ⚠️ Antes se citaba solo 312 nM, que es el **techo** del intervalo de la
  etiqueta: escoger el mejor número. Citar el intervalo completo.
- ⚠️ **La vía subcutánea NO pasa el filtro 3.** Su ratio de 1,33 es sobre fármaco *total*, y
  bortezomib está muy unido a proteínas; con corrección por fracción libre no sobrevive. Retirada la
  afirmación de que "el ratio también se sostiene por vía SC".
- **Falla el filtro de seguridad en ESTE niño:** neuropatía en 18% de pacientes pediátricos (8%
  motora) sobre una atrofia muscular preexistente.
- **Pero el filtro es específico del paciente:** para un paciente MVA **con tumor activo** el balance
  se invierte. Ése es el entregable — una respuesta preparada para un posible segundo tumor.

**Antagonismo predicho (no es un hallazgo del paper):** PMID 31530568 muestra que en carcinoma
ovárico con pérdida de PTEN la traducción impulsada por mTORC1 contribuye al estrés proteotóxico, y
que **inhibir la traducción con cicloheximida protege** a las células CIN. De ahí se *predice* que
everolimus/sirolimus antagonizarían al bortezomib. ⚠️ El paper **no** demuestra resistencia adquirida
vía supresión de mTORC1 ni probó rapálogos — no atribuirle eso.

### El marco de los cinco filtros (la contribución transferible)

1. Regulatorio · 2. Mecanístico · 3. **Farmacocinético (Cmax ≥ conc. efectiva)** ·
4. Seguridad en *este* paciente · 5. **Dirección del efecto (no aumentar mis-segregación)**

Los filtros 3 y 5 casi nadie los aplica y son los que más candidatos matan.

---

## 4. Errores ya corregidos (no volver a introducirlos)

| Error | Corrección |
|---|---|
| PMID 17652220 citado como "vigilancia de Wilms" | Es un paper de **acromegalia**. La correcta es **16857697** |
| PMID 28553959 citado para el espectro tumoral de BUB1B | Es de **TRIP13**. Quitado de ese contexto |
| Citas KARD agrupadas bajo una atribución | Separadas: Xu 2013 (PMID 23789096) y Kruse 2013 (PMID 23345399) |
| "El biomarcador que el campo no tiene" | **Sí lo tiene**: micronúcleos = OECD TG 487; scDNA-seq desde Knouse 2014 (PMID 25197050). Reformulado a "cuantificamos cuánto se queda corto el bulk" |
| Dominio pseudoquinasa "~705–1034", luego "~757–1044" | **Ambos mal.** UniProt O60566 anota "Protein kinase" en **766–1050** y **no** lo llama pseudoquinasa (verificado por Codex, 29-ago). Leu737 cae en el *linker* previo; Asn1002 sí cae dentro. Figura y textos ya corregidos |
| "Tang et al. usó **trisomías estables**… no hay trabajo replicando sus hits en células deficientes de BUB1B" | **Falso, y lo contradecía el dossier propio** (`DATOS_CANDIDATO.md:74,82`): la Figura 6 de Tang prueba AICAR y 17-AAG en MEF *Bub1b*^H/H y *Cdc20*^AAA. Lo que **no** se probó en esos modelos es **metformina** |
| FANCD2: "la segunda variante es un SNV a 2 bp" | Es `TAAG>T` = `c.1278+3_1278+5del` (ClinVar 518343, benigna). Y las **tres** variantes están co-fasadas por GATK (`PID=10046720_C_T`) con fracción alélica ≈0.31 — ése es el argumento fuerte, no ClinVar (que tiene 0 estrellas) |
| "Of 12,427 ACMG-classified variants, four reached P/LP" | Son **12.431 filas** variante×modelo, **5.348** con clasificación ACMG, y **3 variantes únicas** P/LP (4 filas: el nonsense sale en AD y en AR) |
| Las dos figuras del Track 2 **en español** dentro de un reporte en inglés | Traducidas y regeneradas (`fig_domains.py`, `fig_detection_limit.py`) |
| Fanconi/Bloom en escalabilidad | Usan otros ensayos (DEB/MMC, SCE). Retirados |
| Control "sin filtro de efecto" presentado como robustez | Era trivial (los causales son codificantes). Sustituido por los controles HPO reales |

---

## 5. Mapa de archivos

```
~/datos/HACKATHON-MVA-2026/
├── CONTINUAR-AQUI.md      ← este archivo
├── RESUMEN-NOCHE.md        estado al cierre del trabajo nocturno
├── HALLAZGOS.md            la variante y los tres métodos  ⚠️ SUPERADO por entrega/methods_track1.md
├── MOSAICISMO.md           v2, con cálculo de potencia — correcto
├── INFORME.md              la investigación inicial de si el hackathon vale la pena
├── entrega/
│   ├── convergent-hpo-genomewide-and-panel.csv   ✅ verificado = 100 pts (epcr 0.85)
│   ├── methods_track1.md                         ✅ EL BUENO — inglés, corregido, solo falta la Q23
│   ├── Q23_NOTA.md                               ✅ qué verificar en cada cuenta de IA
│   ├── methods_track1_DRAFT.md                   histórico, NO usar
│   ├── NOTAS_ENVIO.md                            por qué no hay hallazgos secundarios
│   └── pregunta_foro_BORRADOR.md                 ya no hace falta (se resolvió lo del proband_id)
├── track2/
│   ├── REPORT_track2_EN.md          ✅ v3, 4.716 palabras — el bueno (24 correcciones el 29-ago)
│   ├── REPORT_track2.pdf            ✅ 18 páginas A4, generado con WeasyPrint
│   ├── REPORT_track2_EN.bak         copia previa a las 24 correcciones
│   ├── REPORT_track2_EN_v1_ARCHIVO.md   versión vieja, no usar
│   ├── SECCION_FILTRO_PK.md         el desarrollo del filtro farmacocinético
│   ├── CANDIDATOS_FARMACOCINETICA.md  el análisis de Codex sobre bortezomib
│   ├── ESTRATEGIA.md · dossier_mecanismo_farmacos.md
│   ├── fig1_detection_limit.png · fig2_domains.png   + sus scripts .py
│   └── report.css                   maqueta PDF (Charter, paleta validada)
├── pipeline/               panel BED con procedencia, ClinVar, HPO, triage.sh
├── tools/                  Exomiser 15.1.0 + 55 GB de bases + logs de las 11 corridas
├── data/                   ⚠️ 438 MB de datos del paciente — ver BORRAR-AL-TERMINAR.md
└── evidencia/
    ├── cursor_revision_track1.md    la revisión adversarial (nota estimada: 58/100)
    ├── cursor_revision_track2.md    la del Track 2 (56/100) — 2ª ronda
    ├── cursor_revision_track2_r3.md la 3ª ronda: 21 hallazgos, 24 correcciones aplicadas
    ├── codex_verificacion_track1_r2.md  Codex verificando 7 puntos (1 refutado: el dominio)
    └── codex_verificacion.md        verificación inicial de legitimidad

~/datos/mva-hackathon-2026/          el repo git (carpeta hermana, sin datos del paciente)
```

---

## 6. Cómo trabajar en esto

- **Codex y Cursor:** Gilberto pidió explícitamente apoyarse en ambos. Cursor con
  `agent -p --trust --model cursor-grok-4.6-high --mode ask`; Codex vía el agente `codex:codex-rescue`.
  **Gotcha:** el subagente de Codex hace timeout a los 2 min pero el job sigue vivo en background;
  consultarlo con `node ~/.claude/plugins/cache/openai-codex/codex/1.0.6/scripts/codex-companion.mjs status`.
- **Gotcha de `pkill`/`pgrep`:** nunca poner en el comando el patrón que se va a buscar — el shell se
  mata a sí mismo. Usar PIDs o partir el patrón (`"cursor""-grok"`). Pasó tres veces.
- **No usar la GPU.** Gilberto tiene procesos propios ahí y la RTX 4060 tiene historial de
  congelamientos. Nada de este análisis la necesita.
- **Verificar siempre las citas** contra PubMed antes de usarlas. Ya se colaron tres falsas.
- **No tomar a los agentes al pie de la letra:** Cursor acertó en casi todo pero se equivocó al
  sugerir PMID 22698282 como el Suijkerbuijk de *Dev Cell*.

---

## 7. Perspectiva honesta

52 personas ya tenían BUB1B antes de que empezáramos. **El hallazgo no nos distingue.** Lo que puede
distinguirnos:

1. Los **controles de robustez reales** (11 corridas), incluido el que salió en contra.
2. El **límite de detección calculado** del mosaicismo en vez de un negativo afirmado.
3. **Metformina descartada con farmacocinética** — el candidato que propondrán los demás.
4. **Bortezomib** con evidencia de 2024 y señal clínica humana, más la condición explícita bajo la
   cual sería apropiado.
5. El **marco de cinco filtros**, transferible a cualquier reposicionamiento.

Premio realista: **Innovación o tercer lugar.** El write-up y el video ya están; lo que falta es la
Q23 y darle a enviar. **No hace falta más análisis** — y meter análisis nuevo a estas alturas
reintroduce el riesgo de errores que costó tres rondas de revisión sacar.
