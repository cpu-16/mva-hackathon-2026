# 🔄 CONTINUAR AQUÍ — estado del MVA Hackathon 2026

**Última actualización: 06-sep-2026.** Documento de traspaso tras un `/clear`.
Léeme completo antes de tocar cualquier otro archivo.

---

## 🆕 7/8-SEP-2026, MADRUGADA — RONDA «A GANAR» CON CODEX COMO JUEZ. **Queda 1 envío; NO usado todavía.**

Gilberto: «quiero que tú junto a Codex hagan lo mejor y pongan a prueba sus capacidades para ganar».
Codex (gpt-6-astra) juzgó el PDF enviado con la rúbrica oficial: **72/100 — tercio superior, no podio**
(`evidencia/codex_juez_rubrica_2026-09-07.md`: puntajes por criterio, 5 cambios ordenados por retorno,
estructura de 14 páginas y 26 frases atacables). Lo hecho esta madrugada, todo commiteado y pusheado
(último `5de9c4f`), con el verificador en «todo cuadra»:

1. **Cambio #1 — cada titular reconciliado con la evidencia** (commit `213d6ff`): título y §1 dicen
   «presumed compound heterozygosity; phase not established»; la página familiar ya no convierte una
   objeción de concentración en una de dosis; «clears the pharmacology» → «not excluded by the
   total-plasma peak comparison»; filtro 5 marcado **untested** en la hoja; REVEL/AlphaMissense
   «retrieved, not run»; el fasado por lecturas cortas es imposible por los huecos de 6,8 y 4,1 kb
   (no «no alignments»); Q6/Q7 separan el dataset de acceso controlado; y ~20 matices más.
2. **Cambio #2 — seguimiento DepMap pre-registrado y corrido** (`depmap/PREREGISTRO_SEGUIMIENTO.md`
   commit `ee59c9e` → `05_seguimiento.py` → `RESULTADOS_SEGUIMIENTO.md`, `fig5`). Las 4 predicciones se
   cumplieron. Descubierto de paso: la interacción p = 0,026 y «ploidy p = 0,88» **no tenían script**;
   ahora se reproducen (modelo completo vs. de efectos principales). Nuevo y en contra: los dos
   ensayos comparten 365 modelos y concuerdan entre sí solo a ρ = −0,070 (ya no se dice «two
   independent measurements»); **rabdomiosarcoma casi ausente del cribado** (17 líneas con score, 3
   con PRISM, y esas 3 entre las menos sensibles a 2,5 µM); el score residualizado por ploidía reduce
   la señal de fármaco a más de la mitad. ⚠️ El encabezado del pre-registro dice «8-sep 00:50» por un
   reloj mal leído; **mandan los timestamps de git (7-sep 23:41)**, y está anotado en el propio archivo.
3. **Bortezomib en el tumor que tuvo el niño y en niños** — §4 (Parte II) y §5 (Parte I): Bersani 2008
   (líneas RMS 13–26 nM), PPTP 2008 (actividad in vivo limitada en sólidos), COG ADVL0015 y ADVL0916
   (**sin respuestas objetivas**; dosis pediátrica 1,2 mg/m² dos veces por semana, 2 de cada 3 semanas),
   Maki 2005 (fase II sarcomas, actividad mínima). Abstracts verificados y guardados
   (`evidencia/pubmed_bortezomib_paediatric_2026-09-07.xml`). Nada de eso favorece; se dice.
4. **Cambio #4 — el PDF es ahora un documento de dos partes** (commit `50d41cf`):
   `track2/PART1_decision_document.md` (22 pp. con referencias) + Parte II = el reporte completo con
   encabezados degradados y sin duplicar página familiar/referencias + Apéndice B. **82 páginas en total; la Parte II empieza en la p. 25.** `entrega/build_pdfs.sh` arma las tres
   piezas. Dos lecturas adversariales independientes (Codex + agente) de Parte I contra Parte II:
   2 blockers y ~15 majors, todos aplicados (`5de9c4f`): «shrank» → «reduced the growth», pauta
   pediátrica completa, la regla «materially above the row is not a better result» restaurada, ~30
   matices devueltos.
5. **Cambio #3 (parcial) — tabla de evidencia de exposición** en §3.2 de ambas partes, con la ficha
   SPL de VELCADE bajada de DailyMed (`evidencia/velcade_spl_dailymed_2026-09-07.xml`): unión a
   proteínas 83 % → **el pico libre IV (≈39–53 nM, ≈99 nM con la cifra de 223 ng/mL) queda a 1–2,5× de la cota de
   EC50 (<40 nM), no a 6–8×**. Está en el resumen ejecutivo, las hojas de filtros y el TSV. **#3 completado a las 00:29:**
   `potencia/PREREGISTRO_4P.md` (commit `fa9eaae`, antes del script) → `03_potencia_4p.py` (paralelo en
   32 núcleos, 397 s; enmienda 1 registra que la corrida secuencial se mató sin ver ningún número) →
   `RESULTADOS_4P.md`. **Potencia con n = 3: 0,167, no 0,897**; hacen falta **12 cultivos por brazo** a
   f = 0,30 y 23 a 0,20; sin fallos de ajuste; el costo es la variabilidad biológica (2 de 4
   predicciones falsadas). Las ramas n=3/n=14 están retiradas del §6 de las dos partes; 0,897 queda
   como referencia optimista; el abstract del Track 2 lo dice (496 palabras). Criterio de micronúcleos
   convertido en regla con IC. Anclas nuevas en `verificar_afirmaciones.py`.
6. **Cambio #5 completado** — `track2/candidates.tsv` + `track2/render_candidates.py` (la hoja de
   filtros de las dos partes se genera desde el TSV; `--check` falla si difieren) +
   `entrega/make_track2.sh` (un comando: fig5 y tablas si están los datos DepMap, hoja, verificador,
   PDFs). Corrido desde un checkout limpio del repo: 8 s, 179 MB, nombra el único insumo ausente
   (`evidencia/make_track2_fresh_checkout_2026-09-08.log`). `build_pdfs.sh` funciona en ambos layouts.
7. Arreglo en el tool: `mva_replay.py` nombra el FASTA ausente en la primera corrida y el self-check ya
   no muere con `AssertionError` (22 aserciones; enmienda en `TRANSFER_TRIP13.md`).

**Decisión sobre el tercer y último envío:** NO gastarlo ahora. El envío 2 (7-sep 23:21) ya es un
paquete sólido; el 3 debe ir con todo lo anterior **más** una ronda adversarial completa nueva (Codex
juez otra vez con la rúbrica) y, si da tiempo, lo que falta de #3 y #5. Ventana recomendada:
**13–17 de octubre**, nunca el último día (el Space ya ha estado congelado). Recordar: solo cuenta el
último.

⛔ **Codex se muere en silencio con prompts >~128 KB por argumento**: pasar el prompt por stdin
(`codex exec - < prompt.txt`) y correrlo con `run_in_background` del harness, no con `nohup` (los
`nohup` de esta sesión murieron a mitad). Cursor tiene la autenticación caducada (`agent login`).
⚠️ Y un gotcha propio de esta sesión: el `cd` al repo hermano persiste entre llamadas; un script con
rutas relativas editó el `CONTINUAR-AQUI.md` del repo y la copia posterior lo pisó. Usar rutas absolutas.

## ✅ 7-SEP-2026, 23:21 — **TRACK 2 REENVIADO (envío 2 de 3)** con las mejoras de abajo

Gilberto delegó la decisión («tú eres el experto»). Se reenvió el Track 2 tras dos lecturas
adversariales del material nuevo (agente independiente + Codex gpt-6-astra; ambas encontraron cosas
reales, todas corregidas antes del click). Respuesta: **«Track 2 submission received ✓ — ciberpty
(cpu-16) | Submission: 2»**. Detalle y captura: `entrega/NOTAS_ENVIO.md`,
`evidencia/envio_track2_2026-09-07.png`. Commit enviado: `3821661`. **Queda 1 envío de reserva;
cuenta el último.** El Track 1 no se reenvió a propósito.

## 🆕 7-SEP-2026 — LAS MEJORAS DE LA REVISIÓN, HECHAS

Gilberto pidió revisar si íbamos bien y luego «haz esas mejoras». Todo está en el markdown, los PDF
regenerados (`entrega/build_pdfs.sh`, 23 + 53 pp., guardia de texto retractado en verde), el xlsx
sincronizado, el verificador en «todo cuadra» y el repo pusheado. (Escrito antes del reenvío de las
23:21; ver la sección de arriba.)

1. **Transferencia real de MVA-Replay, pre-registrada y medida — `replay/TRANSFER_TRIP13.md`.**
   Commit del pre-registro `ee7a050` (22:10), corridas 22:11–22:20 desde un **clon limpio** del repo
   en el scratchpad. Gen TRIP13 (MVA3), dos alelos LP de ClinVar elegidos por la regla de pool
   congelada (3910602 + 4070948), seis términos HPO transcritos del abstract de PMID 42595739, fondos
   HG001/HG002/HG005. **Las cuatro predicciones científicas se confirmaron:** rank 1 en 3/3 a
   **0,8332** (idéntico a cuatro decimales), ausente o 0,0 sin sembrar, rank 1/2/3 con fenotipo ajeno
   (0,4240). Whitelist de ClinVar vale 0,0000 aquí (dato no predicho, reportado).
   **Tres de cuatro predicciones operativas fallaron, y eso es lo valioso:** (F1) la prueba de regresión
   que el README decía que corría en un clon limpio **no corría** — `check_resources()` no estaba
   stubbeado; arreglado **solo en la prueba**, `mva_replay.py` intacto. (F3) tres de los cuatro pasos de
   aprovisionamiento no estaban en *Requirements* de `README_TOOL.md` (YAML en `tools/` vs
   `analysis/`, FASTA, fondos GIAB); ahora están con fuentes y comandos. (F2) el self-check muere con
   `AssertionError` pelado si falta el FASTA chr15 — o sea O-2 («nombra todo lo que falta de una vez»)
   también se falsó; la primera redacción la dio por confirmada y un revisor lo atrapó. (F4) el guardia de reutilización casa
   por **prefijo** de nombre; documentado. Tiempos: 30–54 s por llamada, 2,4–2,5 GB, 2:21–3:20 por
   fondo. Salidas en `replay/transfer_trip13/` (JSON + los dos logs con cada comando y su rc).
   Está citado en el Track 2 §9 (bullet nuevo) y en el README del repo (tabla + «Reproducing»).
2. **Trametinib** entró en la tabla del §3.3 del Track 2 como *Not evaluable — the gap most worth
   closing*, con el abstract de PMID 39251587 bajado y guardado
   (`evidencia/pubmed_39251587_2026-09-07.xml`) y el nulo de DepMap que ya existía. Cmax 22,2 ng/mL =
   36,1 nM sale de la SmPC de Mekinist §5.2 vía `track2/CANDIDATOS_FARMACOCINETICA.md` §8 — no se
   verificó contra la ficha original en esta sesión.
3. **Menores:** Q11 del Track 1 ya no dice «twelve» (remite a las familias listadas, «about a minute
   per run»); Q3/Q23 declaran «Claude Opus and Claude Fable 5.1»; el Track 2 cita
   `report/TRANSFER_MVA2_MVA3.md` con ruta y la cabecera apunta al Apéndice B /
   `submission/ciberpty_track2_methods.md`. Celdas xlsx tocadas: Track 1 B10 y B18, Track 2 B9.
4. **No se tocó:** la longitud del reporte (53 pp.) — decisión de Gilberto; los abstracts (486/490
   palabras, sin cambios); ningún pre-registro anterior.

⛔ **Lo que queda es de Gilberto:** decidir si reenvía el Track 2 con este paquete
(`entrega/listo-para-enviar/`, `entrega/ENVIAR-PASO-A-PASO.md`), y lo de siempre con fecha: repo
público cuando Sage anuncie, borrar datos antes del 23-nov.

---

## ✅ 6-SEP-2026, NOCHE — **LOS DOS TRACKS ESTÁN ENVIADOS**

Video subido por Gilberto a **https://youtu.be/QGYHK0Ihs1c** (verificado accesible sin sesión). Los
dos formularios se llenaron y enviaron desde `cpu-16`. Detalle campo por campo y capturas de las
confirmaciones: **`entrega/NOTAS_ENVIO.md`** + `evidencia/envio_track{1,2}_2026-09-06.png`.

| | Envío | Respuesta del Space |
|---|---|---|
| **Track 2** | **1 de 3** | «Track 2 submission received ✓ — ciberpty (cpu-16)». Panel humano, ~2-3 meses. **Cuenta el último**, así que se puede mejorar hasta el 24-oct |
| **Track 1** | **3 de 6** | «Submission received ✓» · **Rank points 100.0/100 · F-max 1.000 · Full match at rank 1**. El CSV no cambió; lo que cambió es el write-up |

El PDF del Track 1 lleva en la portada el aviso de que **sustituye a los envíos anteriores** y nombra
los cuatro errores corregidos, porque ese formulario no tiene campo de notas y el hilo #19 avisa que
un reenvío puede dejar dos filas en el leaderboard.

⛔ **Lo único que queda, y tiene fecha:**

1. **Hacer público el repo** cuando Sage anuncie el inicio de la evaluación final (anuncio #10 del
   Space). No antes, y no después.
2. **Borrar los datos del paciente antes del 23-nov-2026** y enviar el correo a
   `RarediseaserealkidMVAhackathon2026@synapse.org`. Inventario y comandos listos en
   `data/BORRAR-AL-TERMINAR.md` (incluye los 20 GB de FASTQ y los 4,6 GB de caché que faltaban).
3. **Opcional, hasta el 24-oct:** mejorar el reporte del Track 2 y reenviarlo. Quedan 2 envíos y solo
   cuenta el último, así que reenviar no arriesga nada.

---


## 🆕 6-SEP-2026 (tarde) — GILBERTO DIJO "ENCÁRGATE DE TODO": LO QUE QUEDÓ HECHO Y LO QUE ES SUYO


**Commits pusheados:** `770c975` (revisión del 6-sep) y `727bef6` (video v4, xlsx, abstracts).
⚠️ Cuando se escribió esta sección todavía no había envíos. **Ya los hay** — ver la sección de arriba.

Hecho en esta ronda:

1. **Video v4 renderizado y medido**: `video/pitch_MVA2026.mp4`, **177,87 s** por ffprobe, 8 slides desde
   `slides.html`, Piper a `--length-scale 1.40`. La slide 3 dice ahora "Score held; rank did not."
   Los WAV de la v3 quedaron en `video/audio_v3_backup/`.
2. **`.xlsx` sincronizado** desde el markdown, las dos hojas, celda por celda (sin `**`). Hallazgo que nadie
   había visto: **los dos abstracts violaban el límite de 500 palabras** (547 y 646). Recortados a
   **486 y 489** sin cambiar ningún número; el Track 1 PDF se regeneró (21 pp.). La plantilla es la vigente
   del Space (mismo blob git `c7b0d295…` que `static/templates/methods_description_form.xlsx`).
3. **Reglas, verificadas en los anuncios del Space** (no en la FAQ vieja): el límite del Track 2 subió de
   1 a 3 y cuenta el último (#10); el write-up del Track 1 lo lee el panel (#18: *"counts just as much"*);
   el repo debe hacerse público al empezar la evaluación final. **La ambigüedad "un envío por equipo"
   está resuelta.** Hilo #19 (otro participante, sin respuesta de Sage): reenviar el Track 1 con el mismo
   CSV crea una segunda fila "model2" en el leaderboard y no está claro cuál write-up se revisa.
4. **`data/BORRAR-AL-TERMINAR.md` completado** con los ~718 MB que faltaban (fase, sitios, controles) y
   las líneas de `rm` correspondientes. `mosaico/piloto/*.tsv.gz` y `fase/panel_chr15.vcf.gz` se
   comprobaron: son 1000G, no del paciente.
5. `replay/mva_replay.py` falla temprano nombrando el recurso que falta (lo que Codex pidió tras el clon
   limpio); self-check 21/21 y pruebas 2/2 siguen pasando.
6. Revisión adversarial con **Cursor (Grok 4.6)** sobre los dos reportes contra los archivos de
   resultados: ver la sección siguiente cuando exista, o `evidencia/cursor_revision_2026-09-06.md`.

### Ronda adversarial con Cursor (Grok 4.6) — 11 hallazgos, 10 reales, commit `6be35f8`

Informe íntegro + verificación uno a uno: `evidencia/cursor_revision_2026-09-06.md`. Los que importan:

- **La sección de mosaicismo del Track 1 seguía anclada al 14%** — el mismo error que ya se había
  corregido en el Track 2 y nunca se propagó. Ahora lleva el 2,07% calibrado, la no identificabilidad
  y la retirada del resultado del paciente. **Es el patrón de siempre: el reporte por detrás de
  `mosaico/RESULTADOS.md`.**
- **No existe ningún control de fenotipo barajado.** `tools/control_hpo.sh` corre `hpos_barajados` con
  los cinco términos ajenos, o sea es la primera versión del control ajeno con otro nombre. El write-up
  lo contaba como una familia de control aparte. Retirado y declarado.
- El replay r9 plantó la **missense propia del niño** (`chr15:40220612 T>G`, ausente de ClinVar), no
  ClinVar 4600147 (`T>A`). El Track 1 decía lo segundo.
- La lista de contactos a 5 Å saltaba **Asn1004 (3,14 Å)** citando como «los más cercanos» a dos que
  están más lejos. Ahora van los diez por distancia.
- κ del probando en la comparación de controles es **2,74 (chr8) / 4,60 (chr17)**, no el 2,27× que es
  el exceso a escala cromosómica. La conclusión (el más bajo) se sostiene.
- Los «dieciocho brazos» son el extremo alto del rango DepMap, no una medida de las líneas de Ippolito.
- `TRANSFER_MVA2_MVA3.md` §5 y §7 conservaban dos frases de la versión anterior de la hoja («MVA2 muere
  en el filtro 2»). El reporte seguía la versión corregida; los restos estaban en TRANSFER.
- **Un falso positivo, rechazado tras recontar del VCF:** «2,27 M SNV heterocigotos» es exacto
  (2.274.451 bialélicos autosómicos PASS). Los 2.927.826 de `mosaico/` cuentan todas las llamadas
  heterocigotas. Se añadió la aclaración para que nadie lo lea como choque.

### 🔴 AUDITORÍA PRE-ENVÍO (6-sep, tarde) — 183 agentes, 51 hallazgos, **7 blockers reales**

Workflow de 8 dimensiones con verificación adversarial de tres lentes por hallazgo. Brief e informe:
`evidencia/` + commit `5701eac`. **Los siete blockers se verificaron uno a uno contra los datos antes
de tocar nada**, y todos eran ciertos:

| # | Qué estaba mal | Verificado en |
|---|---|---|
| B1 | La frecuencia del hallazgo secundario GNRHR decía **3,3%**; Exomiser emite porcentajes, así que es **0,033%** | `mva-genome-hpo.variants.tsv`: el mismo campo da 0.00998 para el nonsense de BUB1B que el doc cita bien como 9,98×10⁻⁵ |
| B2 | «el modelo dominante gana en TODOS los constructos» | `replay/out/C_hi_*`: con dos alelos truncantes gana el **recesivo**, 0,9332 vs 0,5818, en los tres fondos |
| B3 | Etiquetas ***cis*/*trans* invertidas** — la introduje yo esta misma mañana | `replay/smoke/out/`: trans 0,9339, cis 0,9305 |
| B4 | El haplotipo co-fasado de FANCD2 tiene **cuatro** variantes en **18 bp**, no tres en 5 | VCF, `PID=10046720_C_T`: 10046720, 10046723, 10046725 y **10046738** |
| B5 | El denominador «corregido» seguía mal: **4.570 filas**, no 4.565 | `mva-genome-hpo.genes.tsv`: 4.570 filas, 3.139 genes, 4.262 con score 0 |
| B6 | La slide 3 decía que los dos alelos se sembraron en 37 genomas; solo se sembraron **3** | `replay/PREREGISTRO.md` y `RESULTADOS.md` |
| B7 | «phase is not computable», retractado en `fase/RESULTADO.md`, seguía **tres veces** en el README | `fase/RESULTADO.md`: *"that was too absolute and it is withdrawn"* |

**El ataque más fuerte que un juez podía hacer, ahora respondido en el reporte:** Ippolito corrió su
**propio** cribado de bortezomib (su Fig. 6p, 387 líneas, reversina, p < 0,0001) y salió **positivo**,
mientras nuestro PRISM en sólidos es nulo. El reporte nunca lo mencionaba. Ahora lo reconcilia: mismo
signo (ρ = −0,075, p = 0,11), diseños distintos (ellos **inducen** aneuploidía, nosotros
**correlacionamos**), y lo que nosotros sí añadimos es la división por linaje. **No dice «dirección
opuesta»**, porque eso contradiría nuestra propia tabla.

Otros arreglos de esta ronda: consentimiento, asentimiento y comité de ética **antes** del protocolo
de biopsia, más la ruta regulatoria off-label; agradecimiento y disponibilidad de datos en los tres
entregables (las reglas los exigen); «no GPU» corregido (la calibración de mosaicismo corrió en CUDA);
el reclamo retractado de los 18 brazos que seguía vivo en `TRANSFER_MVA2_MVA3.md`; el calificador
**monoalélico** de la correlación sarcopenia–mTORC1; el inventario de borrado con los **20 GB de FASTQ
crudos** y 4,6 GB de caché que le faltaban; y `entrega/build_pdfs.sh`, que reconstruye los dos PDF y
**aborta si sobrevive alguna frase retractada** (probado con control positivo).

**El video se rehízo dos veces** y quedó en **177,90 s**. Slides 3 y 7 corregidas, narración de la S3
reescrita para no implicar 37 genomas sembrados.

**Paquete final:** Track 1 PDF 23 pp. · Track 2 PDF **53 pp. con la descripción de métodos como
Apéndice B** (el formulario solo acepta un archivo) · xlsx sincronizado · abstracts 486 y 490 palabras.

⚠️ **Un hallazgo que se dejó a propósito:** el conteo de controles de robustez («doce») no se tocó.
Los verificadores dieron tres totales distintos y meter un número nuevo la noche del envío repite
exactamente el error que ese párrafo confiesa.

**Instrucciones de envío con los valores exactos de cada campo: `entrega/ENVIAR-PASO-A-PASO.md`.**
**Título, descripción y capítulos del video: `video/YOUTUBE.md`.**

---

### 🎬 VIDEO REHECHO (6-sep, noche) — deck animado, figuras reales, voz Qwen3 — commit `85291f9`

Gilberto pidió más profesional, con animación, contenido real y su voz Qwen3. Las tres cosas están.

- **`video/deck.html`** es ahora la fuente: 8 escenas con entradas escalonadas y disolvencias. Un
  fotograma es **función pura del tiempo** (`seek(t)`, sin animación CSS ni rAF), así que
  `render_video.py` muestrea **solo donde algo se mueve**: 888 fotogramas en vez de 5.300 a 30 fps.
  Render completo en **1 minuto**.
- **Tres escenas muestran resultados reales en vez de describirlos:** el mapa de dominios de BubR1
  (`fig2`), el embudo de cinco filtros (`fig3`) y el nulo de PRISM de nuestro propio DepMap
  pre-registrado (`fig4`). Recortadas por CSS para quitarles su título propio y no mezclar
  tipografías. **Los PNG no se tocaron**, son los mismos del reporte.
- **La escena 3 ya no esconde el caso como el punto 37.** Ahora los 37 genomas sin sembrar y el caso
  van separados y etiquetados, que es lo que el benchmark hizo de verdad.
- **Voz: Qwen3-TTS 1.7B VoiceDesign en CPU** (los modelos ya estaban en `~/.cache/huggingface`;
  `transformers` del sistema no trae la clase, así que hay un venv aparte en `~/qween/.venv-tts` con
  el paquete `qwen-tts`). Sin GPU, por la regla del proyecto. ~50-110 s de cómputo por clip.
- ⚠️ **`video/tts_verify.py` se ganó el sitio en la primera pasada.** Transcribe cada clip con
  reconocimiento de voz y lo diffea contra el guion: detectó que la S7 **se había comido el "to"** de
  *"every three months, to age seven"*. Es una frase clínica, así que se reformuló a *"until he is
  seven"* y se resintetizó. **Un TTS basado en LLM se salta palabras sin avisar; no lo confíes al
  oído.**
- Duración **176,08 s** medidos (límite 180). `render_video.py` aborta solo si se pasa.
- El deck estático (`slides.html`, `render.py`, `slide0*.png`) **se eliminó** en vez de dejarlo
  contradiciendo la documentación.

`video/YOUTUBE.md` ya trae los capítulos y la huella nuevos.

---

## 🆕 6-SEP-2026 (mediodía, Claude tras Codex) — PDF REGENERADOS, VERIFICADORES EJECUTADOS

Registro: `evidencia/CLAUDE_APLICACION_2026-09-06.md` §8. Codex se quedó sin cuota a mitad de su
revisión; esta sesión terminó lo que dejó abierto. **Sigue sin haber envío, commit ni push**: el repo
hermano tiene 19 archivos modificados/nuevos sin commitear, listos para revisión y commit.

Lo que se cerró:

1. **Los dos PDF están regenerados** desde el markdown corregido (Track 1: 22 páginas; Track 2: 43),
   comprobados con `pdftotext` y copiados al paquete y al repo. `entrega/listo-para-enviar/LEEME.md`
   ya no dice "desactualizado".
2. **Los verificadores corrieron**: `verificar_afirmaciones.py` da "todo cuadra" en `analisis`, `repo`
   y `--paquete`, y su `--control-negativo` falla como debe. `replay/test_output_reuse.py` 2/2;
   `mva_replay.py --self-check` 21/21. Dos bugs del verificador corregidos (regex `[\d.]+` atrapaba el
   punto final; un ancla que la tabla del PDF parte en dos columnas).
3. **PMID 39264246 verificado contra el texto completo** (PMC11705613, `evidencia/consenso_fulltext_2026-09-06.xml`,
   bajado por Codex). Los tres pasajes del §7/§9 son exactos. La nota de procedencia del reporte ya no
   dice "pendiente"; el "not optional" de la tabla de vigilancia se quitó y la ecografía trimestral se
   atribuye a SIOP-Europe con respaldo del AACR, que es lo que dice la fuente.
4. **El sobrealcance que Codex estaba cazando, corregido**: `methods_track1.md` decía *"the score is a
   property of the alleles; the rank is not"*, una frase que `replay/RESULTADOS.md` §1 ya había
   **retractado como exagerada**. Ahora dice lo estrecho: el score es estable en los tres fondos
   probados (una computación determinista tres veces), no independiente del genoma en general. Mismo
   ajuste en el `README.md` del repo.
5. `replay/RESULTADOS.md` tenía el marcador con el control r7 contaminado (0.4187, 1/1/3) y el tier 2
   "pendiente". Se añadió **§9 (enmienda fechada, sin editar lo anterior)**: r9 → P-B2 falsificada 1/3,
   tier 2 → P-A confirmada (0/30, máx 0.5207 CDH1 HG01885), P-A2 confirmada (HG00101 rank 138, 0.0002).
6. Matices de Ippolito que Codex verificó en el texto completo, ya en el reporte: la Fig. 6r llama
   "minimal response" en la leyenda y "progressive disease" en el cuerpo (se reporta la leyenda sin
   resolverlo); y la atenuación en sólidos es sobre líneas DepMap, no ausencia de evidencia externa
   (Ippolito reporta PDX pancreáticos y pediátricos, Suppl. Fig. 8o–r).

⛔ **Lo que sigue pendiente:** el video (mp4 = v3; guion v4 sin grabar), el `.xlsx` (celda B16 del
Track 1 desfasada), la decisión de commit/push, y la ambigüedad de la FAQ sobre "un envío por equipo"
antes del primer envío del Track 2.

---

## 🆕 6-SEP-2026 (tarde) — LA REVISIÓN YA SE APLICÓ A LOS DOCUMENTOS

Registro completo: **`evidencia/CLAUDE_APLICACION_2026-09-06.md`**. Léelo antes que la sección de más
abajo, que describe el diagnóstico y no el estado actual.

**Sigue sin haber ningún envío, ningún push y ninguna publicación.** Los diffs están sin commitear en
`~/datos/mva-hackathon-2026` (13 archivos) para que Codex los revise.

Lo que **ya está corregido en el markdown**: `track2/REPORT_track2_EN.md`, `entrega/methods_track1.md`,
`entrega/methods_track2.md`, `potencia/RESULTADOS.md`, `potencia/RESULTADOS_2_DOSIS.md`,
`mosaico/RESULTADOS.md`, el `README.md` y `VERIFY.md` del repo, `video/GUION.md` (v4) y `slides.html`,
y el `LEEME.md` del paquete de envío. Los pre-registros **no se tocaron**.

⛔ **Lo que sigue pendiente, y por qué** (el entorno tenía denegada la ejecución de intérpretes):

1. **Los dos PDF están desactualizados.** Hay que regenerarlos con pandoc/WeasyPrint desde el markdown
   corregido y volver a copiarlos. Hasta entonces el paquete de `entrega/listo-para-enviar/` **no**
   representa el trabajo actual, y su `LEEME.md` lo dice en la primera línea.
2. **El video sigue siendo la v3.** El guion v4 y las slides están escritos; los PNG y los WAV no se
   regeneraron. **No marcar el video como listo.**
3. **`analysis/verificar_afirmaciones.py` está escrito pero sin ejecutar**, igual que
   `replay/test_output_reuse.py` y el `--self-check` en esta sesión.
4. **PMID 39264246**: sin acceso al texto completo; los tres pasajes que dependen de él quedan marcados
   como pendientes de re-verificación dentro del propio §7 del reporte.
5. **El `.xlsx` no se tocó**, a la espera de la autorización de `openpyxl` que pidió Codex.

**Corrección de puntero encontrada al verificar:** el LOD calibrado (1,46 / 2,07 / 2,95%) sale de
`mosaico/ventana.json` en W = 125, **no** de `lod_montecarlo.json`. Las cifras eran correctas; la
fuente citada no. Anotado y corregido, sin cambiar ningún resultado.

---

## SESIÓN DEL 6-SEP-2026 (mañana) — revisión y corrección de reutilización de resultados

Diagnóstico actualizado: `REVISION-2026-09-06.md`. Resumen alternativo para integrar después:
`entrega/RESUMEN_JURADO_PROPUESTA_2026-09-06.md`. **Los reportes científicos, PDF, formulario y
video siguen pendientes de actualización; no hubo envío ni publicación.**

- **Corrección a la auditoría del 2-sep:** el umbral de `PREREGISTRO_2_DOSIS.md` §4 está fijado para
  **sólidos**. Aplicar el 0.093 de hematológicas como si disparara esa regla pre-registrada cambia
  el estrato después del resultado. Sólidos es no informativo según la cláusula explícita y el JSON;
  hematológicas es evidencia secundaria. El 4× no está validado, pero no puede llamarse refutado como
  EC50 por una regresión CRISPR sin calibración. Tampoco sustituir 14% por 2.1% como negativo del
  paciente: el control externo dejó el resultado retirado; 2.1% es un LOD de simulación condicionado.
- **Fallo nuevo corregido en MVA-Replay:** mismo gen/fondo con HPO/alelos/fase nuevos podía reutilizar
  TSV anteriores. Reproducido con stubs y archivos sintéticos. Ahora aborta ante archivos del mismo
  caso; usar otro `--name` o `--out`, también después de dry-run. Pruebas en
  `replay/test_output_reuse.py`: pasan ambas, incluida matriz de ocho colisiones; self-check: 21/21.
  Código, README de la herramienta y pruebas copiados al repo hermano, sin commit ni push.
- Confirmados en las salidas: HPO r9 0.3965 y ranks 1/2/3; 30 controles 1000G terminados,
  máximo 0.5207 y cero por encima de 0.5871.
- Cinco PMID pendientes y ref. 22 recuperados de NCBI; XML público guardado en
  `evidencia/pubmed_auditoria_2026-09-06.xml`. Ver tabla de alcance en la revisión: el abstract del
  consenso no basta para verificar calendario exacto ni los 15 casos MVA2; falta texto completo.
- Segunda opinión íntegra: `evidencia/claude_revision_2026-09-06.md`. Su comentario sobre el default
  HPO contaminado viene de un README antiguo, no del código vigente. Ese README ya se corrigió.

---

## 🆕 SESIÓN DEL 2-SEP-2026 — auditoría de estado. **No se corrigió nada todavía**

Gilberto preguntó si el proyecto va bien o le falta. Se auditó el **estado real contra los archivos**,
no contra lo declarado. Se acordó **atacar cinco frentes más tarde**; esta sesión solo actualizó este
documento y el `LEEME.md` del paquete de envío. **Ningún reporte fue modificado.**

**El patrón que explica casi todo lo que sigue: el reporte del Track 2 va por detrás de los archivos
de resultados.** Tres de los hallazgos graves son correcciones que el propio equipo escribió en
`potencia/` y `mosaico/` y **nunca propagó al reporte**. Dos de ellas figuran arriba, en la ronda 10,
dentro de "Ocho errores reales encontrados y TODOS corregidos". No lo están.

### ✅ EL PILOTO DE MOSAICISMO TERMINÓ — veredicto: NO CONCLUYENTE

Ya no está corriendo (la sección "⏳ CORRIENDO EN BACKGROUND AL CERRAR" de más abajo está resuelta).
Terminó el 1-sep 19:50; el análisis y su MD son de las 21:42, **posteriores a la última edición del
reporte (18:29) y de este archivo (18:30)**, por eso no aparecían.
Fuente que manda: `mosaico/CONTROL_RESULTADO.md`. Commit `ce94b89`.

Cobertura verificada explícitamente antes de calcular nada (chr8: 995.160 sitios; chr17: 668.916;
hueco mayor ~50 kb en ambos): **PASA**. El gotcha de los truncamientos silenciosos no se repitió.

| | probando | sobre de 10 controles | ¿dentro? |
|---|---:|---|---|
| chr8 σ²_extra | +0,000879 | +0,001471 … +0,004293 | **no — por debajo** |
| chr8 κ_window | 2,74 | 9,52 … 46,04 | **no — por debajo** |
| chr17 σ²_extra | +0,001528 | +0,002115 … +0,003015 | **no — por debajo** |
| chr17 κ_window | 4,60 | 6,05 … 14,97 | **no — por debajo** |

La enmienda 3 preveía dos desenlaces: dentro del sobre (técnico) o fuera **hacia arriba**. *Por
debajo* no estaba entre ellos, así que el veredicto pre-registrado es **no concluyente**, y se
reporta así en vez de inventar después una regla que lo lea como buena noticia.

**El control no falló al correr: falló al ser control.** La causa se declaró ANTES con su dirección
(los controles no llevan filtro GQ, lo que infla su dispersión) y es exactamente la dirección
observada; además el caller no está pareado (GATK singleton del probando contra el joint call de
3.202 muestras del NYGC). Un κ de 46 en un individuo sano no es biología, es cómo se llamaron
esas variantes.

**Lo único que sí queda, y quita una objeción concreta:** contra diez genomas sanos, κ va de 6 a 46,
y el del probando (≈2,3) es **el más bajo de la comparación**. Un κ elevado no es anómalo por sí
mismo. No prueba que el exceso sea técnico —el desajuste ya predecía esa dirección— solo que no es
llamativo en tamaño.

**Lo que lo resolvería:** un control procesado **idénticamente** (genoma público llamado como
singleton con GATK 4.2.4.0, mismos filtros, desde lecturas). Es la única versión que vale la pena
correr. Ampliar la ventana o añadir muestras no sirve, y la enmienda 4 lo prohíbe.

**Enmienda 5, encontrada leyendo la propia salida:** el adelgazamiento binomial no elimina el ruido
original, lo arrastra, así que σ²_extra va sobre el probando **crudo**. Bajo la versión errónea los
dos estadísticos apuntaban en **direcciones opuestas**; corregidos, coinciden.

### ⛔ LOS CINCO FRENTES ACORDADOS — en este orden

| # | Frente | Costo | Por qué primero |
|---|---|---|---|
| 1 | Los tres arreglos graves del Track 2 (§5 y §6) | media jornada, 0 cómputo | Cierra el flanco por donde entra un juez adversarial |
| 2 | Reescribir el `README.md` del repo | ~30 min | Es lo primero que ve un juez y está en la ronda 6 |
| 3 | Verificar contra PubMed los 5 PMID sin abstract guardado | 1–2 h | Es lo único que puede costar credibilidad entera |
| 4 | Reenviar el Track 1 corregido | 1 h | El reenvío no puede bajar el puntaje y la versión corregida es **mejor** para nosotros |
| 5 | Actualizar `data/BORRAR-AL-TERMINAR.md` | 10 min | Única obligación con consecuencia legal |

### 🔴 TRES ERRORES GRAVES EN `track2/REPORT_track2_EN.md` — declarados corregidos y NO lo están

**(1) El §6 sigue anclado a la selectividad 4× que nuestra propia regla pre-registrada mató.**
Reporte L563-564 y L576-578 presentan la potencia 0,897 «at 4× EC50 selectivity» y cierran con *"we
cannot yet say which regime these cells are in"*. Pero `potencia/RESULTADOS_2_DOSIS.md` L70-78 dice
que el pre-registro fijó **|Δ₂|/σ < 0,10 → escenario central no defendible**, que el valor medido es
**0,093**, y que **"Track 2 §6 must say so, and both now do"**. El reporte da los insumos (0,09 vs
0,84 SD residual) y **nunca el veredicto**: convierte una regla que disparó en una incertidumbre
abierta. Agravante: **todo el criterio de avance L613-631 cuelga de ese 4×** (tabla 1,14× / 1,30× /
1,50× / 2,00×, cuyos números sí verifican contra `potencia/resultados.json`).

**(2) El §5 publica el límite de 14 % como "el número que aportamos" y omite el propio 2,1 %.**
Reporte L501, L511, L525. Pero `mosaico/RESULTADOS.md` L74-78 mide **2,07 %** (mejora de 6,8× sobre
lo publicado) y dice que eso **sustituye** al ~14 %. Consecuencia que importa: la frase **"that sits
7–16× below the limit" se invierte** con el número correcto, porque 1–2 % queda **al borde** del
límite alcanzable, no muy por debajo. La conclusión (el bulk no resuelve esto) **sobrevive**, pero
por la **no identificabilidad** de la variegación balanceada (detección 0,1–0,2 % = la tasa de falsos
positivos, incluso al 40 % de células), y ese argumento —el fuerte, el que no depende de ningún
límite— **no aparece en el reporte** (`2.1%`, `Ψ` y `non-identifiab` dan 0 ocurrencias).

**(3) La compuerta del §6 pide el endpoint equivocado.** Reporte L583-585 y L591 piden conteo de
metafases **con scoring de PCS** «to measure the aneuploid cell fraction».
`potencia/RESULTADOS_2_DOSIS.md` L100-104 lo retractó: **PCS y aneuploidía son endpoints distintos**;
hay que contar **células con ≥1 anomalía numérica de cromosoma**, con PCS como acompañante, y
registrar además cuántos cromosomas anormales por célula anormal. Es el punto que decide n=3 / n=14 /
no correr. Figura arriba como error #7 «corregido».

### 🟠 Medios del Track 2

- **L598-600 (y L91, L850): "about twelve weeks" escoge el extremo bajo.** `DATOS_CANDIDATO.md` §7 da
  **4–8 semanas** para establecer los fibroblastos, así que 8+4=12 pero 8+8=**16**. El rango honesto
  es **12–16**, y la misma fila advierte que en MVA1 el crecimiento puede ser más lento. Es el mismo
  error del Cmax de bortezomib, que **sí está bien corregido** ahora (L102 y L868 citan el intervalo
  completo 89–120 ng/mL = 231–312 nM → 5,8–7,8×).
- **L727-732: nos atribuimos un hallazgo que `clinico/` se prohíbe explícitamente.** El reporte dice
  que el conteo de copia única *"was not ceremonial"* porque atrapó un primer par dentro de un *AluY*.
  `clinico/PARENTAL_SEGREGATION_ORDER.md` L109-114 dice que quien lo atrapó fue la exclusión
  RepeatMasker, que el conteo es **confirmación y no filtro**, y que **"we state it that way rather
  than claiming we sifted a bad pair out at the counting step"**.
- **L904: título alterado en la referencia 22 (PMID 22890317).** El reporte pone *"through AMPK"*; el
  título real es *"through **EGFR degradation**"* (`evidencia/fuentes_verbatim.md` L70), y el abstract
  atribuye el efecto a degradación proteasomal de EGFR. La afirmación del cuerpo (4× más sensible a
  AICAR, L266) **sí es exacta**; el error está solo en la referencia.
- **L563: el 0,897 va sin la advertencia de que es cota superior.** `potencia/RESULTADOS.md` §5b:
  el Hill ajusta 2 parámetros donde el pre-registro prometía 4, y el ruido no tiene término de réplica
  biológica. *"0.897 is an upper bound on the power of this design, not an estimate of it."* Error #6
  de la ronda 10, también sin propagar.
- **§3.3 afirma exhaustividad y omite trametinib.** L17 dice *"every candidate the literature points
  to"*; trametinib **no aparece ni una vez** en 909 líneas, pese a estar en
  `CANDIDATOS_FARMACOCINETICA.md` §8 (aprobado, etiqueta pediátrica desde 1 año, PMID 39251587) y a
  ser uno de los 7 fármacos pre-bloqueados en `depmap/PREREGISTRO.md` L60. O entra al embudo, o se
  quita el "every candidate".
- **L503: "no BAM, hence no GC-LOESS".** `mosaico/RESULTADOS.md` L139-141 dice que esa frase está
  **mal dos veces**: el reto sí distribuye las lecturas (84,7 GB de FASTQ) y el análisis que importaba
  no las necesitaba. Ojo: la frase equivalente del §10 (L809, sobre fasado por lecturas) **sí es
  correcta**; el problema es solo el §5.

### 🔴 TRACK 1 — el cuarto error sigue vivo, y corregirlo NOS FAVORECE

Los errores 1, 2 y 3 (el «24 %», la atribución a ClinVar y el denominador 4.565) están **verificados
como corregidos** en `entrega/methods_track1.md`. El cuarto **no**.

**(4) El control de HPO ajenos sigue en su versión contaminada** en md, PDF y xlsx.
Líneas L104-107, L123-124, L149, L270-271 y L471/474/482. El PDF tiene **7 ocurrencias de 0.4187 y
0 de 0.3965**. El set descrito todavía incluye la hipoacusia.

| Dato | El reporte dice | Verificado en crudo |
|---|---|---|
| Set limpio | incluye HP:0000365 | conjuntivitis, infecciones resp., cefalea, prurito, **rash HP:0000988** |
| Score | 0,4187 | **0,3965** (`tools/results/controles/hpos_ajenos_r9_limpios.genes.tsv`) |
| Δ del fenotipo | 0,1684 | **0,1906** |
| Rank en los 3 fondos | "2/3" | **1 / 2 / 3**, o sea rank 1 en **1 de 3** (`replay/out_r9/`) |

**(5) El tier de 30 genomas ya cerró y el reporte dice que sigue corriendo.** L300-304 y L480-481
dicen *"still running at the time of writing"*. `replay/out/` tiene los 30: máximo **0,5207** (CDH1,
HG01885), **0 de 30 superan 0,5871**. Aplica la frase pre-comprometida de `replay/RESULTADOS.md` §8.
Matiz para redactarlo: BUB1B **sí aparece** en HG00101 (rank 138, score 0,0002), así que *"does not
appear in any of them"* vale solo para los 7 GIAB; P-A2 («ausente o < 0,25») sigue confirmada.

**(6) ⚠️ La consecuencia que nadie había visto: corregir el (4) cambia el resultado de una predicción
pre-registrada, y lo cambia A NUESTRO FAVOR.** P-B2 decía *"con fenotipo ajeno, BUB1B plantado sigue
rank 1 en ≥ 2 de 3"*, y el pre-registro añadía: *"**esperamos que nuestro propio pipeline falle
esto**; confirmarlo es una concesión que nos pre-comprometemos a publicar, no una victoria"*
(`replay/PREREGISTRO.md` L147-149). Con el set contaminado salía 3/3 → confirmada. **Con el set
limpio sale 1/3 → falsificada, que es el desenlace que queríamos.** Por tanto L309 («of seven
pre-registered predictions, five are confirmed») pasa a **cuatro confirmadas**, y hay una
falsificación que juega a favor. **El documento enviado se vende por debajo de lo que la evidencia
sostiene, en este punto y en el (5).** Ese es un argumento para reenviar que ninguno de los dos
revisores planteó — distinto del argumento de integridad de Codex.

**(7) La celda B16 del xlsx (Q9, heterocigosis compuesta) está desfasada:** 1.131 caracteres contra
2.909 en el md. Le faltan los tres párrafos de la ronda 8 y cierra con *"Parental testing would
settle it"*. ⛔ La línea de este archivo que dice «las dos hojas ya están al día» es **falsa** para
esa celda. Las 8 celdas del Track 2 sí son idénticas al md.

**(8) Cosmético:** `methods_track1.md` dice «twelve» controles y `entrega/methods_track2.md` L142 dice
«eleven». `entrega/NOTAS_ENVIO.md` L10 y L59 siguen diciendo epcr 0.95 (histórico).

### 🔴 EL README DEL REPO ESTÁ EN LA RONDA 6 — y es lo primero que ve un juez

`~/datos/mva-hackathon-2026/README.md`, último commit `6f18f70` del **30-ago 10:17**, anterior a
DepMap, MVA-Replay, fase, potencia, VUS y el control externo. La URL de GitHub es parte del envío.

- Dice *"the signal comes from the **ClinVar-whitelisted** pathogenic nonsense allele"* — **refutado
  por nuestro propio benchmark**: el whitelist vale 0,0128 en score absoluto y lo que carga es la
  consecuencia nonsense.
- Dice *"Five clinically unrelated HPO terms (1 run): BUB1B **still ranks 1**"* — es el control
  **contaminado**.
- Dice «eleven extra Exomiser runs»; el video v3 ya dice doce.
- **No menciona ninguno de los cinco análisis pre-registrados**, que son justo lo que sube Impacto y
  Escalabilidad. El bloque «Layout» tampoco lista `depmap/`, `replay/`, `fase/`, `hpo/`, `potencia/`,
  `vus/`, `mosaico/` ni `clinico/`, que sí están en el repo.
- La limitación «Phase is not established» quedó blanda: `fase/RESULTADO.md` la cerró con números
  (no es no concluyente, es **no computable**).

### ⚠️ REGLAS: la FAQ dice que el write-up del Track 1 TAMBIÉN lo juzga un panel

`evidencia/space_tabs_faq.py`, respuesta a *"How is Track 1 scored?"*, cierra con:

> *"Your methods write-up is also reviewed by a judging panel for scientific rigor and depth of
> understanding."*

**La tabla de reglas de este archivo y la del `CLAUDE.md` dicen solo «automática, sobre el CSV».
Está incompleta.** `space_tabs_rules.py` L69 solo menciona panel para el Track 2, así que las dos
fuentes oficiales no dicen lo mismo — pero la FAQ es explícita. Esto **desarma el argumento de Cursor**
de no reenviar el Track 1 porque «no diferencia»: los cuatro errores viven en un documento que sí se lee.
(De hecho `evidencia/cursor_revision_track1.md` L1 ya asumía panel: *"no sobreviviría un panel que
busque un motivo para descalificar"*.)

**Segunda ambigüedad, resolver ANTES del primer envío del Track 2.** La FAQ se contradice: en
*"Can I participate as a team?"* dice **"only one Track 2 submission per team is accepted, and
additional submissions from other team members will be ignored"**, y en *"How many submissions"* dice
**"up to 3 submissions per team… only review your latest entry"**. La lectura razonable es que solo
una persona envía en nombre del equipo y esa persona tiene 3 intentos; como el equipo es de una
persona el riesgo práctico es bajo, pero **si la lectura estricta fuera «un envío», reenviar sería
fatal**. Preguntar en el foro antes de gastar el primero.

### ⚖️ CUMPLIMIENTO: el inventario de borrado se quedó corto por ~718 MB

`data/BORRAR-AL-TERMINAR.md` se generó el **29-ago 02:25** y dice «mantener al día». No se mantuvo.
Derivados a escala genómica del paciente creados después y **no listados**:

| Ruta | Qué es | Tamaño |
|---|---|---:|
| `mosaico/fase/probando_chr*.vcf.gz` | 22 VCF del paciente por cromosoma | **653 MB** |
| `mosaico/sitios/chr*.tsv.gz` | sitios del paciente por cromosoma | 15 MB |
| `tools/results/controles/*.genes.tsv` | rankings con variantes del paciente | 50 MB |
| `fase/paciente_chr15_win.vcf.gz`, `fase/prueba.vcf.gz` | ventana del paciente | ~0,3 MB |

Es **más que los 438 MB de `data/`**, que sí está inventariado. Fecha límite **23-nov-2026** + correo
a Synapse. ✅ Comprobado que `replay/` (41 GB) **no** usa datos del paciente: son genomas públicos con
alelos plantados, declarado en `replay/01_run.py` L3 y consistente con el código.

### ⚠️ CITAS: cinco PMID nuevos SIN abstract verbatim guardado

Ninguno de estos cinco tiene copia en `evidencia/fuentes_verbatim.md`; su única procedencia es este
mismo archivo. **Con tres citas falsas en el historial, hay que bajarles el abstract y emparejarlo con
la afirmación** (el método que sí funciona) antes de enviar.

| PMID | Qué sostiene | Usos en el reporte |
|---|---|---:|
| **39264246** | El consenso de vigilancia: ecografía renal cada 3 meses hasta los 7, en todas las MVA; y «ninguno de los 15 MVA2 desarrolló cáncer» | **8 — es el pilar del §7 y del veredicto MVA2** |
| **42595739** | Niña MVA3 con Wilms a los 3 y ERMS orbitario a los 12 | **6 — es "el hueco que aportamos"** |
| 42434306 | Portadores heterocigotos de BUB1B con PCS elevada y abortos recurrentes | §7 + toda la orden clínica |
| 42094535 | Cribados CRISPR pareados; proteasoma como dependencia aneuploide-específica; UBE2H | §3.4 |
| 41248159 | Carga traduccional → envejecimiento prematuro | §4 |

Además: los números de las **cohortes de mieloma** que el reporte atribuye a Ippolito (L304-310:
n=8/50 p=0,014; n=13/14 p=0,038) **no tienen fuente rastreable en el repositorio**. El «EC50 <40 nM» y
el «2,4 nM» sí están respaldados en `CANDIDATOS_FARMACOCINETICA.md`.
✅ Los 20 PMID del grupo con abstract guardado se cruzaron uno a uno y **coinciden**, salvo el título
de la ref. 22 ya señalado.

### ✅ VERIFICADO BIEN — no repetir estas comprobaciones

- **`replay/mva_replay.py --self-check`: 21 asserts, y tiene control positivo real.** Se mutó un valor
  esperado en una copia y el self-check **falló como debe** (exit 1). Los asserts L306-309 incluyen
  control positivo y negativo declarados. (`README_TOOL.md` L29 dice «20 asserts»; son 21. Cosmético.)
- **Paquete de envío íntegro:** los tres archivos de `entrega/listo-para-enviar/` son **byte a byte
  idénticos** a su fuente (sha256 verificados).
- **El CSV está intacto:** una fila, PROBAND01, las dos variantes, **epcr 0.85**. Los 100/100 no
  corren riesgo con un reenvío.
- **Video: 179,000 s exactos** por ffprobe (límite 180). Es la **v3**: contiene las cuatro frases
  nuevas y 0 ocurrencias de las viejas.
- **Repo:** limpio, sincronizado con `origin/main`, **privado** (hacerlo público al cierre). Ningún
  genotipo se coló: `mosaico/probando*.json` son agregados por cromosoma, que las reglas permiten
  publicar explícitamente (*"free to publicly share their code, models, and derived outputs"*).
- **Cadena de pre-registros completa:** los 5 pre-registros tienen su resultado; ninguno quedó huérfano.
- Todos los números de DepMap, potencia, VUS, fase y farmacocinética del reporte **verifican** contra
  sus archivos fuente. Los errores históricos 1, 2 y 3 (filas vs entidades, porcentajes de score,
  atribución a ClinVar) **no reaparecen** en el Track 2.

### 📐 Números mal declarados — corregidos en este archivo

| | Se decía | Real |
|---|---|---|
| PDF Track 2 | 34 y 36 páginas | **37** |
| PDF Track 1 | 12 y 17 páginas | **18** |

`VERIFY.md` lista **5 pares** y le falta el sexto, que es el del control externo (`6405d9e` enmienda 4
→ `138a40f` código → `ce94b89` resultado) — justo el que un juez adversarial querría comprobar,
porque el resultado va en contra nuestra. **Matiz a declarar si se añade:** `138a40f` se commiteó a
las 18:53:39 y `mosaico/piloto/chr8.tsv.gz` ya existía desde las 18:39. `CONTROL_RESULTADO.md` lo dice
con precisión (*"before the **chr17** data existed"*), pero el **mensaje del commit** dice «before the
control data exists», impreciso para chr8. El mensaje no se puede editar; el MD ya lo corrige.

---

## 🆕 SESIÓN DEL 1-SEP-2026 — se atacó el techo: Impacto y Escalabilidad

Los dos revisores dijeron lo mismo: **Rigor saturado (77-82/100), el techo está en Impacto (25%) y
Escalabilidad (15%), que estaban en cero.** Esta sesión construyó los cuatro artefactos que ellos
nombraron, y dos de ellos produjeron hallazgos que van EN CONTRA nuestra.

### Lo que se construyó

| Artefacto | Archivo | Qué es |
|---|---|---|
| **Impacto** — orden clínica de segregación parental | `clinico/PARENTAL_SEGREGATION_ORDER.md` | Una página que un clínico adapta y firma: dos amplicones Sanger con primers **verificados de copia única en todo GRCh38**, y tabla de interpretación escrita ANTES del resultado, con los cinco desenlaces incluidos los dos que refutarían nuestro Track 1 |
| **Impacto** — potencia del §6 | `potencia/PREREGISTRO.md` → `potencia/RESULTADOS.md` | Pre-registrado y commiteado (`aa3143f`) antes de correr |
| **Escalabilidad** — el marco en las otras dos MVA | `track2/TRANSFER_MVA2_MVA3.md` | La hoja de cinco filtros LLENA para MVA2 (CEP57) y MVA3 (TRIP13). Da respuestas **distintas**: bortezomib muere en el filtro 2 para CEP57, queda condicional para TRIP13 |
| **Escalabilidad** — MVA-Replay empaquetado | `replay/mva_replay.py` + `README_TOOL.md` | Un archivo, sin dependencias nuevas, `--self-check` con controles que sí disparan. Otro equipo planta su gen en un genoma público en una tarde |

Todo integrado en `track2/REPORT_track2_EN.md` (§6, §7, §9 y la página "Read this first") y el PDF
regenerado: **34 páginas**, copiado a `entrega/listo-para-enviar/ciberpty_track2_report.pdf`.

### ⛔ CUARTO ERROR EN EL TRACK 1 YA ENVIADO — y lo encontró nuestra propia herramienta

`hpo/RESULTADOS.md`. **HP:0000365 (hipoacusia), uno de los cinco términos "no relacionados" del
control del reporte ENVIADO, está anotado a MVA2 (OMIM:614114), a ORPHA:1052 (MVA genérico) y
directamente a BUB1B, CEP57 y TRIP13.** La corrección de la ronda 7 verificó sólo contra
OMIM:257300. Es el mismo error de la ronda anterior, con una verificación incompleta.

Re-corrido con cinco términos verificados contra TODAS las MVA (`tools/control_hpo_r9.sh`):

| Control | BUB1B rank | score |
|---|---|---|
| r7 (el enviado, contaminado) | 1 | 0.4187 |
| **r9 (limpio)** | **1** | **0.3965** |

⚠️ **Y hay una segunda consecuencia que va en contra nuestra.** Con el set limpio en los tres fondos
GIAB: el **score es 0.3965 en los tres** (la invariancia al genoma se sostiene) pero el **rank es 1,
2 y 3** — BUB1B es desplazado en HG002 y HG005. Con el set contaminado ganaba en los tres. La frase
"incluso con fenotipo ajeno el pipeline pone BUB1B primero" sólo se sostiene **en el genoma del
paciente**. Verificado que no es anotación directa de KRT17/TNF sino similitud de grafo.

**De 13 términos candidatos, 4 salieron contaminados** — fiebre, disnea y dolor abdominal están
anotados a TRIP13. Elegir términos de control a ojo no funciona: es la tercera ronda que falla.

### 🔬 POTENCIA DEL §6 — la regla pre-comprometida se disparó a favor

**El hedge del reporte era un error aritmético NUESTRO.** El §6 decía que el ensayo podía ser ciego
porque "la variegación deja cada cromosoma en 1–2% de las células". Ese 1–2% es **por cromosoma**
(30% repartido entre 22 autosomas); lo que importa para carga proteotóxica es la fracción de células
con **alguna** aneuploidía, que es el 30%.

| Fracción de células aneuploides | Potencia con n=3 |
|---|---|
| 0.02 (la lectura del reporte) | **0.063** — ciego |
| 0.30 (la lectura correcta) | **0.897** |

Se retira "a negative result is ambiguous by design" en lo que respecta a potencia. **Y compra un
cambio de protocolo, no una frase:** la potencia se desploma bajo f≈0.25 y **nadie ha contado
metafases en esos fibroblastos**. Ahora hay una medición de compuerta (conteo de metafases con PCS)
con tres ramas: n=3 si f≥0.25, n=14 si f=0.10, y **no correr el ensayo bulk si f<0.10**.
También: extender el rango de concentraciones a 1.000 nM (a selectividad 10× la EC50 del control
caía justo en el techo de 400 nM).

### ⏳ CORRIENDO EN BACKGROUND AL CERRAR — ✅ **YA TERMINÓ (1-sep 19:50), ver la sesión del 2-sep arriba**

**El piloto del control externo de mosaicismo** (`mosaico/_piloto.sh` → `mosaico/piloto/`).
Enmienda 4 pre-registrada y commiteada (`6405d9e`) ANTES de bajar un solo byte: ventanas **fijas**
chr8:5-25 Mb y chr17:5-25 Mb, regla mecánica, idéntica en ambos. Va por el 11% de chr8 y el ritmo da
**~4 h por cromosoma**, o sea ~8 h en total. Es I/O puro, corre solo.
Al terminar hay que calcular σ²_extra y κ_window y compararlos con el probando adelgazado
binomialmente — todo el diseño está en la enmienda 3 del pre-registro. **Verificar cobertura
explícitamente** (primera y última posición, sin huecos >2 Mb): tres extracciones remotas ya
truncaron en silencio en este proyecto.

### ⚖️ RONDA 10 — los dos jueces volvieron a evaluar (1-sep, tarde)

Se les pasó el brief `evidencia/brief_juez_r10.md` con los cuatro artefactos nuevos.

| Juez | Antes | Ahora | Movimiento |
|---|---|---|---|
| Codex | 78 | **82** | +4 (Impacto +2, Escalabilidad +3, **Rigor −1**) |
| Cursor | 74 | **76** | +2 (Impacto +1.5, Escalabilidad +1.1, Rigor −0.3) |

**Los dos dicen lo mismo: finalista, no ganador — y los dos recomiendan ENVIAR, no analizar más.**
Cursor: *"sentarse en 0 de 3 con ocho semanas es como un 76 pierde contra un 70 que sí se envió"*.

**Ocho errores reales encontrados y TODOS corregidos** (ver los dos archivos `evidencia/*_juez_r10.md`):

1. La orden clínica decía que un resultado en *trans* "confirma el diagnóstico". No: apoya el modelo
   compuesto y añade evidencia tipo PM3, pero no vuelve patogénica una missense VUS.
2. Decía "dos desenlaces refutan el Track 1". Solo el *cis* refuta; los de novo dejan la fase abierta.
3. **El amplicón 1 tenía un defecto de laboratorio real:** 753 pb con la variante a 574 nt del primer
   reverso, más allá de donde la lectura Sanger se mantiene limpia. La secuenciación bidireccional
   era nominal. Rediseñado a 521 pb con la variante a 80–450 nt de ambos primers.
4. **El criterio de avance del §6 era inalcanzable por construcción.** Exigía el contraste de Ippolito,
   que es entre poblaciones homogéneas. Un cultivo mosaico al 30% con selectividad 4× dentro de las
   células aneuploides da un ratio bulk de **1.50×**, no 4×. El experimento habría fallado su propio
   criterio aunque la biología funcionara. Ahora el umbral se lee de una tabla según la *f* medida.
5. MVA2: el filtro 2 decía "rechazado" razonando de "SAC mínimo" a "menos carga proteotóxica". Eso es
   una inferencia; ausencia de medición es **"no evaluable"**. Y la ausencia de cáncer en 15 individuos
   pertenece al filtro 4, no al 2. Corregido — y la demostración queda **más** precisa: los tres
   genotipos fallan por razones distintas.
6. El pre-registro de potencia prometía un Hill de 4 parámetros; el código ajusta 2. Y el ruido no
   tiene término de réplica biológica. Ambos inflan la potencia: **0.897 es una cota superior**.
7. PCS no es lo mismo que contar células aneuploides. La compuerta pedía el endpoint equivocado.
8. **Yo mismo inflé la línea base:** escribí que con el control contaminado BUB1B "ganaba en todos los
   fondos". Nuestro propio benchmark dice 1/1/3. El control limpio mueve **un** fondo, no dos.
   Dramatizar el tamaño del propio error es el mismo fallo que cualquier otra contradicción.

**Y un quinto artefacto propio que salió en contra nuestra** (`potencia/RESULTADOS_2_DOSIS.md`,
pre-registrado en `45c4ed7` antes de correr): la carga proteotóxica es una **dosis**, no un
interruptor. Una célula MVA lleva ~1 cromosoma alterado; las líneas de las que sale la EC50 <40 nM
llevan ~18 brazos. En DepMap, donde la dependencia existe, 2 brazos mueven 0.09 SD residual contra
0.84 de 18 brazos. **La selectividad 4× sobre la que se centró el cálculo de potencia no es
defendible para estas células.**

**`VERIFY.md` (nuevo, en el repo):** un juez no podía verificar los hashes de los pre-registros. Ahora
hay una tabla que empareja cada diseño con su resultado y el comando de un renglón para comprobar el
orden. Un pre-registro vale exactamente el timestamp que lo respalda.

PDF del Track 2: ~~36 páginas~~ **37 páginas** (verificado 2-sep), en `entrega/listo-para-enviar/`.

---

### 🧬 EL VUS — cerrado con un censo (1-sep, noche). Punto 5 del backlog, ya no pendiente

`vus/RESULTADOS.md`. Era "calibrar p.Asn1002Lys contra variantes BUB1B ya clasificadas".
**Fuimos a construir el set de calibración y no existe. Esa ausencia es el resultado.**

| ClinVar 2026-08-28, gen BUB1B | |
|---|---:|
| missense | **1.497** |
| — patogénicas o probablemente patogénicas | **1** (una estrella, un solo submitter) |
| — benignas / probablemente benignas | 35 |
| — **VUS** | **1.426 (95,3%)** |
| pérdida de función | 94, de las cuales **82 son P/LP** |

La evidencia clínica de este gen está construida sobre pérdida de función **82 a 1**. La tasa base
de una missense que llega a P/LP aquí es **1 de 1.497 = 0,07%**. Con un solo positivo no se calibra
ningún predictor, así que la salida honesta es la ausencia con su número, no un score sin calibrar
—que era justo lo que los dos revisores habían prohibido.

**La estructura sí dice algo, y pasa el criterio de aborto fijado de antemano** (era abortar si el
pLDDT medio en 766–1050 < 70; da **81,9**, y **91,5** en 992–1012 contra 63,6 de la proteína entera):
**Asn1002 está enterrado** (RSA 0,162) en un bolsillo hidrofóbico con Trp978, Phe977, Val998, Ile1000,
Leu1001 y Ala1003 a menos de 5 Å. La sustitución mete una cadena más larga y **con carga positiva**
ahí dentro. Se reporta como evidencia sobre la sustitución, **no como clasificación**: sin ΔΔG, sin
predictor y sin reclamar PP3.

⚠️ **El límite que importa:** un censo mide la base de datos, no la biología. Sieben modeló
BUBR1^L1012P, una missense causal suficiente para construir un modelo de ratón, y este snapshot no la
clasifica. Las missense de este gen pueden estar simplemente poco testeadas.

**Para qué sirve:** le da a la orden de segregación parental un número en vez de un adjetivo. La
segregación no es solo la vía más barata para este alelo — es **la única practicable**.

---

### 🔴 DECISIONES QUE LE TOCAN A GILBERTO, NO AL AGENTE

1. **¿Reenviar el Track 1? Los dos jueces se contradicen, y hay que elegir.** Van 2 de 6 envíos.
   Hay cuatro errores conocidos: el "24%" retirado, la atribución a ClinVar, el denominador de 4.565
   filas-vs-genes, y el 0.4187→0.3965 con el matiz del rank. El CSV que da 100/100 **no cambia**.
   - **Codex: reenviar.** Dejar un control que sabemos falso en el paquete que se juzga es un fallo
     de integridad evitable, y los jueces quizá nunca lo descubran.
   - **Cursor: NO reenviar hasta que el Track 2 haya usado un envío.** El Track 1 no diferencia (52 de
     53 equipos tenían la respuesta), y editar el documento que no decide el podio mientras el que sí
     lo decide sigue en 0 de 3 es gastar el esfuerzo donde no cuenta.
   - **Los dos coinciden en el orden: primero el Track 2.**
2. ~~**Subir el video a YouTube**, único bloqueador del Track 2.~~ ✅ **Hecho el 6-sep:**
   https://youtu.be/QGYHK0Ihs1c (deck animado v5, voz Qwen3-TTS, 176,08 s).
3. Chequeo de un minuto: compartir datos para entrenamiento en OFF en Anthropic y OpenAI.

---

---

## ⚠️ REGLAS DE ENVÍO — verificadas contra el reglamento, no las asumas

Esto se recomendó mal una vez (1-sep): dos agentes dijeron "envía ya, te da ventaja" y resultó falso.
**Los hechos salen de `evidencia/space_tabs_faq.py` y `evidencia/space_tabs_rules.py`:**

| | Track 1 | Track 2 |
|---|---|---|
| Envíos | 6 por participante | 3 por equipo |
| Cuál cuenta | **el de MAYOR puntaje** | **solo el ÚLTIMO** |
| Evaluación | automática sobre el CSV **+ el write-up lo revisa un panel** (FAQ, ver 2-sep) | **panel de jueces humanos** |
| Cuándo | inmediata | **2–3 meses DESPUÉS del cierre** |

- ⛔ **Enviar el Track 2 temprano NO da ventaja competitiva.** La FAQ dice literalmente *"The
  independent expert panel will only review your latest entry, so save your best for last"*. No hay
  puntuación intermedia ni retroalimentación. **No volver a recomendar "envía ya para ganar ventaja".**
- Lo único que gana un envío temprano es **seguro contra fallo de ejecución** — y es barato, porque se
  sobrescribe. El riesgo es real: el leaderboard lleva congelado desde el 26-ago.
- **Reenviar el Track 1 no puede bajar el puntaje**: cuenta el mayor, y sale del CSV, que no cambia.
- No hay ronda de preguntas en vivo.

---

## 🗺️ MAPA DE ARCHIVOS — hay ~50 `.md` en este proyecto, esto es lo que manda

**Regla: si dos archivos se contradicen, gana el de esta tabla.**

| Necesitas… | El archivo que MANDA | Ojo |
|---|---|---|
| Estado general y qué sigue | **este archivo** | — |
| Reporte Track 1 (**reenviado 6-sep, 3 de 6**) | `entrega/methods_track1.md` + `.pdf` | ⛔ `methods_track1_DRAFT.md` es histórico, NO usar |
| Reporte Track 2 (**enviado 6-sep, 1 de 3**) | `track2/REPORT_track2_EN.md` + `REPORT_track2.pdf` | ⛔ `REPORT_track2_EN_v1_ARCHIVO.md` es viejo, NO usar. El PDF se construye con `entrega/build_pdfs.sh` y lleva la descripción de métodos como Apéndice B |
| Formulario de métodos | `entrega/methods_description_form_ciberpty.xlsx` | ✅ resincronizado celda por celda desde los `.md` el 6-sep; los dos abstracts caben en las 500 palabras |
| Q2–Q11 del Track 2 en texto | `entrega/methods_track2.md` | espejo del xlsx, mantener sincronizados |
| CSV de predicciones | `entrega/convergent-hpo-genomewide-and-panel.csv` | epcr 0.85, verificado = 100 pts |
| Análisis DepMap | `depmap/PREREGISTRO.md` → `depmap/RESULTADOS.md` | leer en ese orden |
| Benchmark MVA-Replay (lo nuevo) | `replay/PREREGISTRO.md` → `replay/RESULTADOS.md` | el pre-registro trae 3 enmiendas fechadas al final |
| Fase de las dos variantes (lo nuevo) | `fase/RESULTADO.md` + `replay/PILOTO_FASE.md` | cerrado, no reintentar |
| Video (**v5 animado, subido**) | `video/deck.html` (las 8 escenas) + `video/GUION.md` (v4 del guion) + `video/README.md` | Construir con `render_video.py`; voz con `tts_qwen.py` y **verificarla con `tts_verify.py`**. ⛔ `GUION_v1.md` y `GUION_v3.md` son históricos |
| Qué se envió y cuándo | `evidencia/registro_envios_track1.md` | — |
| Control externo de mosaicismo | `mosaico/CONTROL_RESULTADO.md` | lo nuevo (1-sep 21:42); veredicto **no concluyente** |
| Obligación de borrar datos | `data/BORRAR-AL-TERMINAR.md` | ⛔ **desactualizado**, faltan ~718 MB (ver 2-sep) · **fecha límite 23-nov-2026** |
| Archivos listos para subir al Space | `entrega/listo-para-enviar/` | con el nombre exacto que pide; ver su `LEEME.md` |

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

## 🧫 MOSAICISMO + LA PREGUNTA "¿ESTO GANA?" — sesión del 30-ago (noche)

**Veredicto de los dos revisores a la pregunta directa de Gilberto: 77–82 y 78–82 sobre 100.
Finalista, NO ganador.** Y los dos coinciden en dónde está el techo: **no en más Rigor** (ya casi
saturado) sino en **Impacto (25%) y Escalabilidad (15%), que están en cero**.
Análisis completos: `evidencia/codex_ganar.md`, `evidencia/cursor_ganar.md`.

### ✅ P-A RESUELTA — se sostiene

37 genomas sanos con los ocho HPO del niño. **Ninguno supera nuestro 0.5871.**

| Tier | n | máximo | supera 0.5871 |
|---|---|---|---|
| GIAB v4.2.1 | 7 | 0.5619 (GJB2, HG004) | 0 |
| 1000G 30× | 30 | **0.5207** (CDH1, HG01885) | 0 |

Aplica la frase pre-comprometida de `replay/RESULTADOS.md` §8, escrita antes de tener los datos.
⚠️ El margen que manda sigue siendo **0.0252** contra GIAB, y **ClinVar aporta 0.0128 = el 51% de
ese margen**. Sin ClinVar el margen cae a 0.0124. Eso va al reporte tal cual.

### ⛔ MOSAICISMO: resultado RETIRADO, no borrado

Se hizo la calibración (LOD 14% → ~2%), se midió la tasa de switch de Beagle contra el trío GIAB
(0,810%/sitio), se demostró numéricamente la **no identificabilidad** de la variegación balanceada
(detección 0,1–0,2% = la tasa de falsos positivos, incluso al 40% de células) — **eso todo sigue en
pie**. Lo que se cayó es la conclusión sobre el paciente:

1. **Calibré un test y apliqué otro.** El umbral pre-registrado de Ψ lo supera el paciente en **22 de
   22** cromosomas con cualquier κ. Lo que reporté (z robusto entre cromosomas) es otro test, elegido
   después de ver los datos y nunca calibrado.
2. **"El exceso es global y no puede ser mosaicismo"** convierte una varianza en un desplazamiento de
   media. Retirado. Lo que sí queda: la media con signo llega a +0,0018 como máximo → no hay clon
   direccional.
3. **La calibración NO corrió sobre datos públicos**: los N y la distribución de DP salen del VCF del
   paciente. Solo la tasa de switch es del trío.
4. La sobredispersión estaba mal parametrizada: κ por sitio ≈ 1,21, κ por ventana ≈ 2,27 — es
   **correlación espacial**, no ruido i.i.d.

**`mosaico/PREREGISTRO.md` enmienda 3 tiene el diseño exacto del control externo** que lo revive o lo
mata: dos estadísticos sin signo comparables en profundidad, piloto de 10 muestras en chr8 vs chr17
antes del confirmatorio de 30, adelgazamiento binomial del paciente a la profundidad del control, y
reglas de falsificación técnicas/biológicas fijadas de antemano.

### 🔴 EL AGUJERO QUE NADIE HABÍA MIRADO

`data/Challenge_Clinical_Phenotype_1.docx` tiene **407 palabras** y del tumor solo dice
"Rhabdomyosarcoma". **Sin cariotipo, sin CMA, sin ploidía, sin histología.** La respuesta preparada
del Track 2 (bortezomib para un futuro tumor sólido) **no tiene ni una medición del tumor que el niño
sí tuvo** — y DepMap ya nos dijo que la dependencia no se extiende a sólidos. Hay que declararlo antes
de que lo encuentre un juez.

### 🎯 LO QUE SUBE EL TECHO — trabajo real, no prosa (ambos revisores coinciden)

**Impacto:**
- **Página de orden clínica para segregación parental**: dos amplicones Sanger en `chr15:40209701` y
  `40220612` + tabla de interpretación (cada padre con una → trans, diagnóstico se sostiene; uno con
  las dos → cis, el Track 1 está mal) + PCS en linfocitos parentales (PMID 42434306). Es el ÚNICO
  experimento que confirma el diagnóstico, informa un embarazo futuro y explica HP:0200067. **1 día.**
- **Cobrar el CHIP-negativo** que ya tenemos y enterramos: un niño post-ERMS sin lesión clonal
  cromosómica detectable por encima de ~2% de células. **0 de cómputo.** (Pendiente del control.)
- **Cálculo de potencia del §6** (2–3 días, sin FASTQ): si la carga proteotóxica escala con la
  fracción aneuploide, un cultivo de fibroblastos al 1–2% por cromosoma NO son las líneas de Ippolito.

**Escalabilidad:**
- **Empaquetar MVA-Replay** como herramienta: gen candidato + dos alelos + set HPO + VCF de fondo →
  score plantado, rank, contrafactual sin ClinVar, control de HPO ajeno. Ya se corrió 61 veces. Otro
  equipo con otra enfermedad lo usa en una tarde. **3–5 días.**
- **Llenar la hoja de cinco filtros para MVA2 (CEP57) y MVA3 (TRIP13)**: van a dar respuestas
  DISTINTAS (CEP57 no tiene riesgo de tumor embrionario → bortezomib muere en el filtro 2/4). Un marco
  que da lo mismo para tres enfermedades es un eslogan. **2 días, sin cómputo nuevo.**

### ⚠️ GOTCHA NUEVO: los streams remotos mueren en silencio

**Tres truncamientos hoy, ninguno dio error**: panel 1000G chr17 (417 de 862 MB), chr19 (256 de 718),
y la extracción del control (cubrió el **4,9%** de chr21 y `bcftools` reportó éxito). Un panel
truncado no falla: **fasa mal en silencio**. chr17 pasó de 25.829 a 57.063 sitios al reponerlo.
⛔ **Toda extracción remota necesita verificación explícita de cobertura después**, no confiar en el
código de salida.

### Estado de procesos al cerrar

| | |
|---|---|
| Descarga de los 85 GB FASTQ | **PAUSADA** en 2/8 (21 GB). Reanudable: `./_dl_fastq.sh` continúa donde quedó. Los dos revisores dicen que alinear **ya no es el camino principal** — solo si el control deja al paciente fuera del sobre |
| Control sano 1000G | **DETENIDO** — salió truncado, hay que rehacerlo con verificación |
| Benchmark tier 2 | ✅ terminado, 30/30 |
| Disco | 119 GB libres |

---

## 🔬 MVA-REPLAY + FASE — segunda y tercera tanda de resultados propios (30-ago, tarde-noche)

**Mismo método que DepMap: pre-registro commiteado ANTES de correr, timestamp de git como activo.**
Esta vez el pre-registro v1 se mandó **sin correr** a Codex y a Cursor, los dos lo destrozaron en los
mismos cuatro puntos, y el v2 es el resultado. De ~150 corridas bajó a 61.

Archivos: `replay/PREREGISTRO.md` (con 3 enmiendas fechadas) → `replay/RESULTADOS.md`;
`replay/PILOTO_FASE.md`; `fase/RESULTADO.md`. Críticas verbatim en
`evidencia/codex_replay_prereg.md` y `evidencia/cursor_replay_prereg.md`.
Commits: `8086dd4` (pre-registro), `ecfdb39` (enmiendas + centinela), `06859b4` (fase),
`d95dbe7` + `15c8bf8` (resultados).

### ⛔ TRES ERRORES EN EL REPORTE DEL TRACK 1 QUE YA SE ENVIÓ

Los tres los encontró el propio benchmark o la ronda adversarial sobre sus resultados
(`evidencia/codex_replay_resultados.md`, `evidencia/cursor_replay_resultados.md`).

**(a) "the phenotype contributes about 24% of the score".** Par equivocado *y* tipo de número
equivocado. 0.5506 y 0.4187 son los **dos controles de HPO ajenos** (el contaminado y su corrección):
ese delta mide lo que valían los dos términos contaminantes. El par correcto es 0.5871 → 0.4187, pero
**convertirlo a porcentaje es inválido igual**: el combinador de Exomiser no es aditivo y 0.4187 no es
una línea base sin fenotipo. ⛔ **El porcentaje se RETIRA, no se corrige a 28,7%.** Los dos revisores
coincidieron: cambiar 24 por 28,7 es corregir un error de encuadre con un error de redondeo.

**(b) "the ClinVar-whitelisted nonsense allele carries the ranking".** El whitelist vale **0.0128 en score absoluto**, no el ranking. (Y no se expresa como % — es la
misma operación inválida que se retiró para el fenotipo.) Lo que lo carga es la **consecuencia nonsense**. Ver el contrafactual
abajo. El hallazgo es *más* robusto de lo que dijimos —no depende de la base de datos— pero la
atribución del reporte está mal.

**(c) "BUB1B ranked 1 of 4,565 genes".** 4.565 son **filas gen × modo de herencia**, no genes. Esa
corrida tiene **3.139 genes únicos**, de los cuales solo **257 sacan score > 0** y **32** sacan ≥ 0.01;
las otras 4.262 filas están empatadas al fondo con score 0. El denominador está inflado ~15×. El
reporte usa 3.139 correctamente en otros tres sitios, o sea también se contradice. Es el mismo error
de filas-vs-entidades que ya se corrigió una vez para el conteo de variantes.

**Decisión pendiente de Gilberto: reenviar el Track 1 (van 2 de 6) con las tres correcciones más los
resultados de MVA-Replay.** El CSV que da los 100/100 no cambia.

### Lo que midió MVA-Replay

| Resultado | Número |
|---|---|
| **El score no depende del genoma.** Plantando los dos registros ClinVar del Track 1 en tres genomas sanos ajenos | **0.5871 (HPO real) y 0.4187 (HPO ajeno), idénticos a 4 decimales en los tres**. El fondo solo cambia el *rank* |
| Gradiente por arquitectura de alelos (pre-registrado, P-C **confirmada**) | dos P/LP **0.9332** · P/LP+VUS (la del niño) **0.5871** · dos VUS **0.1120**. Caída de 0.8212 (umbral 0.10) |
| ⛔ **Pero la interpretación era falsa.** Escribí "ClinVar vale el 88%" y "sin ClinVar las mismas dos variantes darían 0.1120" — **nunca corrí ese contrafactual**; C-lo usa *otros* alelos. Los dos revisores lo exigieron y se corrió | **Quitar ClinVar entero cuesta 0.0128 en score absoluto.** La arquitectura molecular exacta del niño sin ninguna clasificación ClinVar da **0.5743** y sigue rank 1 en los dos fondos. El gradiente lo manda la **consecuencia**, no la base de datos |
| El registro VUS del missense aporta **0.0000** | plantar el alelo REAL del niño (ausente de ClinVar) en vez del registro VUS da el mismo 0.5871 hasta el cuarto decimal |
| **Escala del 0.5871** en 7 genomas GIAB sanos con nuestros 8 HPO | gen top entre 0.0578 y **0.5619**; nuestro 0.5871 les gana a los 7 pero por **0.025**. BUB1B no aparece en ninguno. **P-A queda ABIERTA, no "se sostiene"**: null sesgado a favor, y HG001+dos tríos son 3 unidades independientes, no 7. ⏳ faltan 30 genomas 1000G · las frases pre-comprometidas para cada desenlace están en `replay/RESULTADOS.md` §8 |
| Los fondos GIAB rankean menos genes | mediana **2.387** vs 4.565 del paciente → el null está sesgado **a nuestro favor**; el endpoint portátil es el *score*, no el rank |
| **Señuelo FANCD2** (P-B3) | rank 1 en 1 de 3 — y ese 1 es HG001, un **fondo inerte** (gen top 0.0578, cualquier cosa >0.06 gana ahí). ⚠️ **No es falsificación limpia**: la enmienda 3 cambió el constructo después de ver los ranks, y el señuelo no está pareado en fuerza de variante. Queda como *post-enmienda exploratorio*. **No cobrarlo como victoria** |
| ⚠️ **El 0.5871 es la fila AD** (modelo dominante, un solo alelo); la fila AR compuesta —la del diagnóstico— da 0.5538. Sumado a que la llamada compuesta es invariante a la fase, la interpretación recesiva la pone el analista, no el pipeline |
| El benchmark se cazó a sí mismo | el assert de ingestión detectó que el pool de FANCD2 aceptó ClinVar 2312080, que es de **FANCD2OS** (Codex lo predijo). Enmienda 3; el arreglo hace al señuelo **más fuerte** |

### 🧬 FASE: no es "no concluyente", es NO COMPUTABLE

Los dos agentes dijeron que era lo más valioso del backlog. Costó 3 consultas y una corrida de 18 s:

- **Por lecturas:** GATK dejó `PGT`/`PID` **vacíos** en las dos variantes; están a **10.911 bp**.
- **Estadística:** dentro del intervalo el niño tiene 3 hets (las dos causales + 40216470) y **las
  tres faltan** en el panel 1000G de 3.202 personas. Beagle conserva 1.391 de 1.452 variantes de la
  ventana y **descarta justo esas tres**.
- **Un panel mayor no arregla nada:** con AF gnomAD 1,0×10⁻⁴ y **9,0×10⁻⁷**, las copias esperadas en
  6.404 haplotipos son 0,64 y **0,006**. Harían falta ~10⁶ haplotipos.
- **Piloto de fase:** Exomiser lee la fase para el ACMG (trans→PM3, cis→BP2) pero **nunca** para el
  modelo compuesto: dos nonsense en cis siguen dando AR_COMP_HET, PATOGÉNICO y rank 1; la penalización
  es **0,34%**. O sea el pipeline es ciego a la fase.
- **Lo que sí lo resolvería:** Sanger a los papás (lo más barato), lectura larga del niño, o
  transcripto alelo-específico. Todo requiere laboratorio nuevo.

⛔ **No reintentar el fasado.** Está cerrado con números.

---

## 🎯 PLAN PARA EL PODIO — hecho con Codex y Cursor, quedan ~8 semanas (cierre 24-oct)

Los dos jueces puntuaron con la rúbrica oficial. **Codex 72→78, Cursor 65→74** tras la ronda 7.
Lo que falta ya no es argumento, es *resultado*. DepMap fue el primero. Lo que sigue, en orden:

| Prioridad | Qué | Días | Estado |
|---|---|---|---|
| ~~1~~ | ~~Prueba pre-registrada DepMap/PRISM~~ | 4–6 | ✅ **HECHO 30-ago** |
| ~~2~~ | ~~MVA-Replay~~ | 4–6 | ✅ **HECHO 30-ago** (rediseñado por Codex+Cursor; 61 corridas, no 150) · ⏳ falta el tier de 30 genomas 1000G |
| ~~3~~ | ~~Fase estadística de las dos variantes BUB1B~~ | 2–5 | ✅ **CERRADO 30-ago** — no es no concluyente, es **no computable**. Ver `fase/RESULTADO.md`. NO reintentar |
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
ella. Gilberto la sube. **Que suba el video v3, no el viejo.** Cuota Track 2: 3 envíos, y **solo cuenta el último** (ver las reglas de envío arriba).
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
rechaza el envío sin ella (`submit_track2.py:92-94`). Gilberto lo está subiendo. Cuota Track 2: 3, **solo cuenta el último**.
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
