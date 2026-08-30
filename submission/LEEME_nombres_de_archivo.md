# Archivos con el nombre exacto que pide el Space

El Space pide que el nombre del archivo lleve el nombre del equipo. Estos ya lo llevan y son copias
al día de los originales — **no editar aquí, editar el original y volver a copiar.**

| Archivo | Original | Para |
|---|---|---|
| `ciberpty_convergent-hpo-genomewide-and-panel.csv` | `entrega/convergent-hpo-genomewide-and-panel.csv` | Track 1 ✅ enviado |
| `ciberpty_track1_report.pdf` | `entrega/methods_track1.pdf` | Track 1 ✅ enviado (envío 2, corregido) |
| `ciberpty_track2_report.pdf` | `track2/REPORT_track2.pdf` | Track 2 ⛔ **sin enviar** |

**Track 2 además exige una URL de video de YouTube/Vimeo** (`submit_track2.py:92-94`); sin ella el
formulario rechaza el envío. Subir `video/pitch_MVA2026.mp4` (versión v3, 2:59.0) — **no la vieja**.

Flujo de envío: `brave-cdp` → login HF (cpu-16) → pestaña Submit → `tools/fill_form_space.py`.
Ese script abre **una sola** sesión CDP por websocket: los `nodeId` de `DOM.querySelectorAll` no
sobreviven entre llamadas separadas de `chrome-agent`, y `DOM.setFileInputFiles` falla con
"Could not find node". En Gradio los textboxes ignoran el setter nativo; hay que hacer `focus()` +
`Input.insertText`.
