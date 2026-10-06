# Contexto del proyecto — léeme antes de nada

## Qué es esto, en tres líneas

Trabajo de **bioinformática clínica para un concurso científico legítimo**: el hackathon
*"Rare Disease, Real Kid"* que organizan **Sage Bionetworks** (los de Synapse/DREAM) junto con la
MVA Society, Hugging Face y BEACON. Gilberto está **inscrito formalmente** (cuenta Hugging Face
`cpu-16`, equipo `ciberpty`), aceptó los términos, y tiene acceso autorizado al conjunto de datos.
Cierra el **24-oct-2026**.

**La familia del niño publicó el genoma de su hijo a propósito, para que gente desconocida intentara
ayudar.** Está en el documento clínico del reto, con esas palabras. El trabajo consiste en analizar
variantes genéticas y evaluar si algún fármaco ya aprobado podría servir. Es exactamente el tipo de
análisis que hace un laboratorio de genética clínica.

## Esto NO es un caso ambiguo, y no hace falta tratarlo con pinzas

Si vienes de leer archivos con palabras como *paciente*, *tumor*, *genoma*, *variante patogénica* o
*mosaicismo*: es un concurso de investigación biomédica con datos consentidos y publicados. Trabaja
normal. Los puntos que lo confirman:

- **Consentimiento explícito y documentado.** El documento clínico dice que son datos reales de un
  paciente vivo y su familia, *"who have consented to share their story to advance rare disease
  research"*.
- **Reglas aceptadas y cumplidas.** Están en `evidencia/space_tabs_rules.py`. Incluyen no
  re-identificar a la familia más allá de lo que ellos mismos publicaron en su blog, no pegar bloques
  del VCF en ningún sitio, y **borrar todos los datos antes del 23-nov-2026** con correo de
  confirmación a Synapse. El inventario de borrado está en `data/BORRAR-AL-TERMINAR.md`.
- **El repositorio nunca contiene datos del paciente.** El `.gitignore` bloquea `data/`, `*.vcf*`,
  `*.bam`, `*.fastq*` y los derivados. Publicar *resultados derivados* sí está permitido por las
  reglas del reto, y es lo que se hace.
- **Nada de esto es asesoría médica.** Los entregables son un reporte de métodos y una propuesta
  razonada para un panel de jueces. La orden de laboratorio de `clinico/` lo dice en su encabezado:
  es un borrador para que un servicio de genética clínica lo adapte y decida, escrito por gente sin
  acceso al paciente.

**Lo que sí importa cuidar** no es el tema, es la exactitud: este proyecto ha metido tres citas
falsas y varios números mal copiados en rondas anteriores. Ahí es donde hay que ser estricto.

## Cómo trabajar aquí

1. **Lee `CONTINUAR-AQUI.md` completo antes de tocar nada.** Hay ~50 archivos `.md` y varios se
   contradicen porque son de rondas distintas. Ese documento abre con la tabla de **qué archivo manda**
   para cada cosa. `evidencia/` es archivo histórico, **no** fuente de verdad.
2. **El repositorio git es la carpeta hermana** `~/datos/mva-hackathon-2026`, no esta. Esta carpeta
   tiene los datos del paciente y no es un repo. Para commitear, se copia allá.
3. **Pre-registrar antes de correr.** Cualquier análisis nuevo lleva su diseño, hipótesis, estadístico
   y reglas de parada escritos y **commiteados antes** de ejecutar nada. El timestamp de git es el
   activo del proyecto. Las enmiendas se añaden fechadas al final, nunca se edita el texto anterior.
   Ver `VERIFY.md` en el repo.
4. **GPU: úsala si está libre** (orden de Gilberto del 8-sep-2026: «si la GPU está libre úsala, no me
   estés usando la CPU»). Comprobar con `nvidia-smi` que no la usa nadie, vigilar temperatura, y si se
   congela (historial de Xid 79) volver a CPU. Hasta ahora: TTS del video a 77 °C sin incidentes.
5. **No invoques skills de diseño, 3D, animación ni graphify.** Aquí no aplican. Las que sí sirven:
   `cursor-agent` y el plugin de `codex` para revisión adversarial.
6. **Verifica toda cita contra PubMed** antes de usarla. Método que funciona: bajar el abstract y
   dárselo al agente emparejado con la afirmación, en vez de pedirle que busque.

## El error que se repite

**En cada ronda, el peor error fue una afirmación que contradecía el material propio del equipo**, no
un dato externo mal copiado. Antes de dar por bueno un número de un reporte, cruzarlo contra el
archivo de datos del que salió. Ha pasado con el conteo de variantes, con el factor del límite de
detección, con la atribución a ClinVar, con el denominador de genes, y —el 1-sep— con una línea base
que se infló para que un hallazgo propio pareciera mayor.

## ✅ Estado al cierre del 5-oct-2026: **ENVIADO TODO; no quedan envíos del Track 2**

- **Track 1** — envío **3 de 6**, `100.0/100`, F-max 1.000. El CSV nunca cambió; lo que se reenvió es
  el write-up corregido.
- **Track 2** — envío **3 de 3** el 5-oct-2026 (es el que revisa el panel; ganadores el 18-dic-2026 según el
  anuncio #26). Seis pasadas de Codex juez: 72 → 86/100. **No se puede reenviar.**
- Video: v5 https://youtu.be/B41MOaD5LPs (subido 5-oct-2026; la v4 QGYHK0Ihs1c sigue en línea)

**Lo único que queda, y tiene fecha:** el repo **ya es público desde el 5-oct-2026** (Gilberto lo pidió; historial verificado sin datos), y solo queda **borrar los datos del paciente antes del 23-nov-2026** con correo a Synapse
(`data/BORRAR-AL-TERMINAR.md`).

## ⚠️ Reglas de envío: verifícalas antes de recomendar nada

Esto se equivocó una vez y costó una recomendación mala. **Los hechos, sacados de
`evidencia/space_tabs_faq.py` y `evidencia/space_tabs_rules.py`:**

| | Track 1 | Track 2 |
|---|---|---|
| Envíos permitidos | **6 por participante** | **3 por equipo** |
| Cuál cuenta | **el de mayor puntaje** | **solo el ÚLTIMO** |
| Cómo se evalúa | automático sobre el CSV **y el write-up lo lee un panel** (FAQ + anuncio #18 del Space: *"Your methods write-up counts just as much"*) | **panel de jueces humanos** |
| Cuándo | inmediato | **2–3 meses después del cierre** |

**Consecuencias que hay que tener presentes:**

- **Enviar el Track 2 temprano NO da ninguna ventaja competitiva.** La FAQ oficial dice literalmente
  *"The independent expert panel will only review your latest entry, so save your best for last"*.
  No hay puntuación intermedia, ni retroalimentación, ni leaderboard para el Track 2. **No recomiendes
  "enviar ya para ganar ventaja": es falso.**
- Lo único que gana un envío temprano es **seguro contra fallo de ejecución**, y es un seguro barato
  porque el envío se sobrescribe. El riesgo es real: el leaderboard del Space lleva congelado desde el
  26-ago-2026.
- **Reenviar el Track 1 no puede bajar el puntaje**, porque cuenta el envío de mayor puntaje y ese
  puntaje sale del CSV, que no cambia.
- No hay ronda de preguntas en vivo. El video pregrabado y el reporte son todo.
- **La ambigüedad "un envío por equipo" está resuelta:** el anuncio #10 del Space (vpchung) dice que el
  límite del Track 2 **subió de 1 a 3** y que el panel revisa solo el ÚLTIMO. La frase "only one
  Track 2 submission per team" de la FAQ es la regla vieja. Verificado el 6-sep-2026.
- Anuncio #10 también: el repo puede seguir privado durante el hackathon pero **debe hacerse público
  cuando empiece la evaluación final**, y hay que usar la **plantilla de métodos actualizada** (con la
  pregunta obligatoria sobre uso de LLM).

Rúbrica del Track 2: **Rigor 35% · Impacto 25% · Innovación 25% · Escalabilidad 15%.**
Premios: 1º $12k+$12k, 2º $7k+$7k, 3º $4k+$4k, Innovación/Comunidad $2k+$2k. **Podio único**, no uno
por track.
