# Enviar — paso a paso, con los valores exactos de cada campo

Actualizado el 7-sep-2026. Space del reto:
https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026
Cuenta: `cpu-16`. Cuota consumida al 7-sep: **Track 1 · 3 de 6** · **Track 2 · 1 de 3** (el 2 de 3 se
envía el 7-sep con el paquete mejorado; queda 1 de reserva para el cierre).

Los límites salen del `config.py` del Space, leído el 6-sep: `MAX_TRACK1_SUBMISSIONS = 6`,
`MAX_TRACK2_SUBMISSIONS = 3`. La frase de la FAQ que decía "un solo envío del Track 2 por equipo" es
la regla **vieja**: el anuncio #10 del Space dice que subió a 3 y que el panel revisa **solo el
último**. Por eso enviar hoy no gasta nada irreversible.

---

## Paso 1 — subir el video (bloquea el Track 2)

Archivo: `~/datos/HACKATHON-MVA-2026/video/pitch_MVA2026.mp4`
Título, descripción, capítulos y ajustes: **`video/YOUTUBE.md`** — cópialo de ahí.
✅ **Hecho (v5, 5-oct-2026): https://youtu.be/B41MOaD5LPs** — verificado accesible sin sesión (oEmbed). La v4 (QGYHK0Ihs1c) sigue en línea hasta confirmar el envío 3.

---

## Paso 2 — Track 2 (pestaña *Submit Track 2*)

El formulario tiene cinco campos. Estos son los valores:

| Campo del formulario | Qué poner |
|---|---|
| Team / Display Name (optional) | `ciberpty` |
| **GitHub repo URL \*** | `https://github.com/cpu-16/mva-hackathon-2026` |
| **Pitch video URL \*** | `https://youtu.be/B41MOaD5LPs` |
| **Report file (PDF or Markdown) \*** | `entrega/listo-para-enviar/ciberpty_track2_report.pdf` |
| Notes for judges (optional) | el texto de abajo |

El formulario **solo acepta un archivo**, así que la descripción de métodos del Track 2 va **dentro
del PDF, como apéndice**. No hay que subirla aparte.

### Notes for judges — texto para copiar (versión del 5-oct, envío 3 de 3)

```
Two things are worth knowing before you open this.

First, the answer is negative. No disease-modifying drug is supported for this child today, and the
report is the evidence behind that no rather than a candidate we are advocating for. Bortezomib is
carried through the filters as a conditional research candidate — not excluded by a total-plasma
exposure comparison, with free exposure, duration and tumour selectivity in MVA unresolved — and is
stopped by the safety filter for this patient; we state the one setting in which the question would
have to be asked again, and the experiment on his own constitutional cells that would inform it.

Second, eight pre-registrations were committed to git before their analyses ran, and most came back
against us: PRISM did not establish the predicted drug association in solid lines, the mosaicism
control returned not conclusive, and the power analyses showed the assay as first sized to be
underpowered even under its own assumptions. A transfer of our retrieval benchmark tool to a second
MVA gene (TRIP13), run from a fresh clone of the repository, held — and falsified two claims the
repository made about itself, both corrected with the log committed. VERIFY.md explains how to check
the timestamps without trusting us.

This is our third and final Track 2 entry and replaces the second (7 September): same conclusions,
every sentence reconciled against our own results after three further adversarial reads, the
worksheet on readable landscape pages, and a new pitch video. Part I of the PDF is the decision
document; Part II is the full evidence; the methods description form is Appendix B. The repository
is private during the hackathon and will be made public for the final evaluation, per the rules.
```

(El texto del envío 1 del 6-sep está en `NOTAS_ENVIO.md`.)

---

## Paso 3 — Track 1, reenvío (pestaña *Submit Track 1*)

| Campo del formulario | Qué poner |
|---|---|
| Team / Display Name (optional) | `ciberpty` |
| **Predictions file (CSV) \*** | `entrega/listo-para-enviar/ciberpty_convergent-hpo-genomewide-and-panel.csv` — **sin cambios**, es el mismo que ya dio 100/100 |
| **Report file (PDF or Markdown) \*** | `entrega/listo-para-enviar/ciberpty_track1_report.pdf` |
| **GitHub repo URL \*** | `https://github.com/cpu-16/mva-hackathon-2026` |

**Por qué reenviar.** El anuncio #18 del Space dice: *"Your methods write-up counts just as much. Two
perfect scores can look very different once we read how each team got there."* La versión que está
enviada tiene cuatro errores conocidos: el control de fenotipo ajeno contaminado (0.4187 en vez de
0.3965), el porcentaje de contribución del fenotipo que retiramos, la atribución a ClinVar, y el
benchmark de 30 genomas descrito como "todavía corriendo" cuando ya terminó 0 de 30. **El puntaje no
puede bajar**: cuenta el envío de mayor puntaje y sale del CSV, que no cambia.

**El riesgo, y no es cero.** En el hilo #19 del foro otro participante reenvió con el mismo CSV y le
salieron **dos filas en el leaderboard**, y Sage no ha contestado cuál write-up revisan. El formulario
del Track 1 **no tiene campo de notas**, así que el aviso va en la primera página del propio reporte.

---

## Después de enviar

1. Captura de pantalla de las dos confirmaciones, guardarlas en `evidencia/`.
2. Anotar fecha y hora en `entrega/NOTAS_ENVIO.md`.
3. **Hacer público el repo** cuando Sage anuncie el inicio de la evaluación final (anuncio #10). No
   antes, y no después.
4. **Borrar los datos del paciente antes del 23-nov-2026** y avisar por correo a
   `RarediseaserealkidMVAhackathon2026@synapse.org`. Inventario y comandos:
   `data/BORRAR-AL-TERMINAR.md`.
