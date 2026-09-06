# Paquete de envío — estado: **PREPARADO LOCALMENTE, NO ENVIADO**

Actualizado el **6-sep-2026**. Nada de esta carpeta se ha enviado, subido ni publicado en esta ronda.

El Space pide que el nombre del archivo lleve el nombre del equipo. Estos ya lo llevan.
**No editar aquí: editar el original y volver a copiar.**

## ✅ Los dos PDF están regenerados desde el markdown corregido (6-sep-2026, mediodía)

Generados con `pandoc` + WeasyPrint y `track2/report.css`, y comprobados con `pdftotext`: las cifras
corregidas aparecen (0.3965, Δ 0.1906, ranks 1-2-3, 0.5207, 12–16 weeks, "EGFR degradation") y las
viejas ("still running", "about twelve weeks", el título "through AMPK" de la ref. 22, "not optional")
dan cero ocurrencias. `analysis/verificar_afirmaciones.py --paquete` también los recalcula contra los
archivos de resultados.

| Archivo | Original (fuente corregida) | Estado |
|---|---|---|
| `ciberpty_convergent-hpo-genomewide-and-panel.csv` | `entrega/convergent-hpo-genomewide-and-panel.csv` | ✅ al día — **no se ha tocado**. Track 1 ya enviado (2 de 6 envíos usados) |
| `ciberpty_track1_report.pdf` | `entrega/methods_track1.md` | ✅ regenerado 6-sep, 22 páginas A4 |
| `ciberpty_track2_report.pdf` | `track2/REPORT_track2_EN.md` | ✅ regenerado 6-sep, 43 páginas A4 |

Lo que sigue **sin** estar listo: el video (el mp4 es la v3; el guion v4 no se ha grabado) y el `.xlsx`
del formulario (la celda B16 del Track 1 sigue desfasada respecto al markdown).

## Cómo regenerar

```bash
cd track2 && pandoc ../entrega/methods_track1.md -f markdown -t html5 --standalone -o /tmp/t1.html
python3 -c "from weasyprint import HTML,CSS; HTML('/tmp/t1.html', base_url='.').write_pdf('../entrega/methods_track1.pdf',stylesheets=[CSS('report.css')])"
```
Igual para `REPORT_track2_EN.md` → `REPORT_track2.pdf`. Después `pdftotext` como arriba y volver a
copiar los dos PDF a esta carpeta con el nombre del equipo.

## Reglas de envío — verificadas, no asumidas

| | Track 1 | Track 2 |
|---|---|---|
| Envíos | 6 por participante | 3 por equipo |
| Cuál cuenta | el de **mayor** puntaje | **solo el ÚLTIMO** |
| Evaluación | automática sobre el CSV **+ panel humano sobre el write-up** (FAQ) | panel de jueces humanos |
| Cuándo | inmediata | 2–3 meses después del cierre |

⛔ **Enviar el Track 2 temprano no da ventaja competitiva.** La FAQ dice *"The independent expert panel
will only review your latest entry, so save your best for last"*. Reenviar el Track 1 no puede bajar el
puntaje, porque cuenta el mayor y sale del CSV, que no cambia.

El envío del Track 2 exige además una URL de vídeo de YouTube/Vimeo (`submit_track2.py:92-94`); sin
ella el formulario rechaza el envío.
