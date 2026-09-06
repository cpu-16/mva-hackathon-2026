# Enviar — paso a paso, con los valores exactos de cada campo

Actualizado el 6-sep-2026. Space del reto:
https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026
Cuenta: `cpu-16`. Cuota consumida hoy: **Track 1 · 2 de 6** · **Track 2 · 0 de 3**.

Los límites salen del `config.py` del Space, leído el 6-sep: `MAX_TRACK1_SUBMISSIONS = 6`,
`MAX_TRACK2_SUBMISSIONS = 3`. La frase de la FAQ que decía "un solo envío del Track 2 por equipo" es
la regla **vieja**: el anuncio #10 del Space dice que subió a 3 y que el panel revisa **solo el
último**. Por eso enviar hoy no gasta nada irreversible.

---

## Paso 1 — subir el video (bloquea el Track 2)

Archivo: `~/datos/HACKATHON-MVA-2026/video/pitch_MVA2026.mp4`
Título, descripción, capítulos y ajustes: **`video/YOUTUBE.md`** — cópialo de ahí.
Sube como **No listado**. Guarda la URL corta `https://youtu.be/…`.

---

## Paso 2 — Track 2 (pestaña *Submit Track 2*)

El formulario tiene cinco campos. Estos son los valores:

| Campo del formulario | Qué poner |
|---|---|
| Team / Display Name (optional) | `ciberpty` |
| **GitHub repo URL \*** | `https://github.com/cpu-16/mva-hackathon-2026` |
| **Pitch video URL \*** | la URL de YouTube del paso 1 |
| **Report file (PDF or Markdown) \*** | `entrega/listo-para-enviar/ciberpty_track2_report.pdf` |
| Notes for judges (optional) | el texto de abajo |

El formulario **solo acepta un archivo**, así que la descripción de métodos del Track 2 va **dentro
del PDF, como apéndice**. No hay que subirla aparte.

### Notes for judges — texto para copiar

```
Two things are worth knowing before you open this.

First, the answer is negative. No approved drug can be recommended for this child today, and the
report is the evidence behind that no rather than a candidate we are advocating for. Bortezomib is
carried through the filters and then stopped by the safety filter for this patient; we state the one
setting in which that verdict would invert, with the assay that would test it.

Second, five analyses were pre-registered in git before the data was touched, and four of the five
came back against our own argument. All four are in the report, including the DepMap test that
weakened our central mechanism and the mosaicism control that returned not conclusive. The
repository has the pre-registration commits and the timestamps; VERIFY.md explains how to check them
without trusting us.

The methods description form is Appendix B of this PDF. The repository is private during the
hackathon and will be made public for the final evaluation, per the rules.
```

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
