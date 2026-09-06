# Registro de envíos — MVA Hackathon 2026

## ✅ 6-SEP-2026 — LOS DOS TRACKS ENVIADOS

Enviados desde la cuenta `cpu-16` en el Space de Sage. Capturas de las dos confirmaciones en
`evidencia/envio_track1_2026-09-06.png` y `evidencia/envio_track2_2026-09-06.png`.

### Track 2 — envío **1 de 3**

| Campo | Valor enviado |
|---|---|
| Team / Display Name | `ciberpty` |
| GitHub repo URL | `https://github.com/cpu-16/mva-hackathon-2026` |
| Pitch video URL | `https://youtu.be/QGYHK0Ihs1c` |
| Report file | `ciberpty_track2_report.pdf` — 53 pp., 922,4 KB, con la descripción de métodos como Apéndice B |
| Notes for judges | los dos párrafos de `entrega/ENVIAR-PASO-A-PASO.md` |

Respuesta del Space: **«Track 2 submission received ✓ — ciberpty (cpu-16) | Submission: 1»**, con el
aviso de que el panel revisa durante ~2-3 meses. **Quedan 2 envíos y cuenta el último**, así que el
reporte se puede seguir mejorando hasta el 24-oct.

### Track 1 — envío **3 de 6**, reenvío del write-up corregido

| Campo | Valor enviado |
|---|---|
| Team / Display Name | `ciberpty` |
| Predictions file | `ciberpty_convergent-hpo-genomewide-and-panel.csv` — **702 B, sin cambios** respecto a los envíos de agosto |
| Report file | `ciberpty_track1_report.pdf` — 23 pp., 135,2 KB, con el aviso de sustitución en la portada |
| GitHub repo URL | `https://github.com/cpu-16/mva-hackathon-2026` |

Puntaje devuelto por el scorer: **Rank points 100.0 / 100 · F-max 1.000 · umbral EPCR 0.85 ·
✅ Full match at rank 1.** Igual que los dos envíos anteriores, como estaba previsto: el CSV no cambió.
Lo que cambió es el write-up, que es lo que lee el panel.

⚠️ **Pendiente de vigilar:** el hilo #19 del foro describe que un reenvío con el mismo CSV puede dejar
**dos filas en el leaderboard** y Sage no ha contestado cuál write-up revisan. Por eso la portada del
PDF dice de forma explícita cuál es el que pedimos que lean.

---

# Notas del envío — Track 1

## ✅ Verificación empírica: el CSV da 100 puntos

Descargué el evaluador real del hackathon (`evaluation.py` del Space) y lo corrí localmente contra
nuestro CSV, usando nuestra propia respuesta como ground truth simulado:

```
proband_id parseado: 'PROBAND01'   filas: 1
  rank=1  epcr=0.95  variantes=[('chr15', 40209701, 'T', 'G'), ('chr15', 40220612, 'T', 'G')]

  rank points : 100.0
  F-max       : 1.0
  match rank  : 1
```

Con dos controles que prueban que el scorer sí discrimina y el 100 no es un artefacto:

| Control | Resultado | Esperado |
|---|---|---|
| Ground truth falso (chr7) | rank_points = 0.0, F-max = 0.0 | ✅ |
| Solo 1 de las 2 variantes correcta | rank_points = 50.0 | ✅ medio crédito |

**El CSV está bien formado y puntuará 100/1.0 si nuestra respuesta es la correcta.**

## ✅ RESUELTO: un `proband_id` incorrecto NO consume cuota

Era el bloqueador principal. Leyendo `tabs/submit_track1.py`, el orden de operaciones es:

1. Valida la URL de GitHub, el reporte y el CSV → `return` temprano, sin guardar nada.
2. `count = submissions_by_user(hf_username)` — cuenta **archivos ya guardados** en el dataset del
   leaderboard.
3. `_score_csv_bytes(csv_bytes)` → **si lanza excepción, hace `return` con el mensaje de error.**
4. El `entry` que se guarda se construye **después**, solo si el scoring tuvo éxito.

Un `proband_id` desconocido revienta en el paso 3, así que nunca se llega a guardar el archivo — y la
cuota se mide contando archivos guardados.

**Conclusión: podemos probar `PROBAND01` sin riesgo.** Si el scorer responde "Unknown proband_id",
reintentamos con `WGS_EX2312012` sin haber gastado nada. Preguntar en el foro deja de ser necesario
(el borrador sigue disponible en `pregunta_foro_BORRADOR.md` si prefieres hacerlo igual, por
visibilidad ante los organizadores).

## ⚠️ El nombre del archivo es PÚBLICO

El envío se guarda como `model{N}_{nombre_de_tu_csv}` y **ese nombre aparece en el leaderboard
público**. Así es exactamente como se filtró la respuesta: 24 de los 53 participantes subieron
archivos llamados `bub1b-compound-het.csv`, `bub1b_pair.csv`, etc.

A estas alturas la respuesta ya es pública de facto, así que ocultarla no aporta. Pero el nombre sí
es una tarjeta de presentación ante quien mire la tabla, incluidos los organizadores. Conviene que
comunique el **método**, no la respuesta.

Sugerencia: `convergent-hpo-genomewide-and-panel.csv` — dice que hubo dos análisis convergentes y uno
genome-wide guiado por fenotipo, que es justo lo que nos distingue de los otros 52.

## Contenido del CSV

Una sola fila `primary`: el par heterocigoto compuesto de BUB1B, EPCR 0.95.

## Por qué NO se incluyen filas `secondary`

El análisis produjo dos variantes ACMG patogénica/probablemente patogénica fuera de BUB1B, ambas
descartadas con razones (detalle en `../HALLAZGOS.md`):

- **FANCD2 chr3:10046723** — probable artefacto: fracción alélica 0.31, segunda variante a 2 pb en el
  mismo sitio de splicing, y locus con pseudogenes de alta identidad. Requiere Sanger.
- **GNRHR chr4:67753920** — estado de portador de un trastorno recesivo. No es hallazgo secundario
  accionable según ACMG SF v3.2.

Incluirlos no penalizaría el score automático, pero un panel clínico lo leería como falta de criterio.
Se documentan en el write-up en lugar de enviarse como predicciones.

## Lo que todavía falta para poder enviar

| Requisito | Estado |
|---|---|
| CSV | ✅ listo y verificado contra el scorer real |
| URL de GitHub (`https://github.com/...`) | ❌ falta crear el repo |
| Reporte (PDF o `.md`) | ⚠️ `methods_track1_DRAFT.md` está escrito; falta cerrar las 3 decisiones marcadas |
| Login con la cuenta de HF en el Space | ✅ `cpu-16` ya tiene acceso |
