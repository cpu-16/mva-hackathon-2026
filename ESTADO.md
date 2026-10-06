# ESTADO — MVA Hackathon 2026 («Rare Disease, Real Kid», Sage Bionetworks + HF)

**Actualizado: 5-oct-2026, noche.** Léeme primero. El historial largo por rondas está en `CONTINUAR-AQUI.md`
(117 KB, intacto, solo se consulta con `rg`); el detalle de cada día va en `BITACORA.md`. Las reglas de envío y
el encuadre del proyecto están en `CLAUDE.md`.

## Foco

**No hay nada que hacer hasta noviembre.** Todo está enviado y el repo es público.

## Hecho (cerrado)

| Pieza | Estado | Dónde |
|---|---|---|
| Track 1 | Enviado 3 de 6, **100/100**, F-max 1.000; no se reenvía | `entrega/NOTAS_ENVIO.md` · bitácora 2026-09-06 |
| Track 2 | **Enviado 3 de 3 el 5-oct** («Submission: 3»); es el que revisa el panel; **no se puede reenviar** | `entrega/NOTAS_ENVIO.md`, `evidencia/envio_track2_2026-10-05*.png` · bitácora 2026-10-05 |
| Video | v5 (corte documental) en YouTube, oculto: https://youtu.be/B41MOaD5LPs | `video/YOUTUBE.md` · bitácora 2026-10-05 |
| Repo | **Público desde el 5-oct** (Gilberto lo pidió; historial verificado sin datos del paciente): https://github.com/cpu-16/mva-hackathon-2026, último commit `885fdad` | bitácora 2026-10-05 |
| Juez Codex (rúbrica) | 72 → 77 → 79 → 82 → 84 → 85 → 86/100 en seis pasadas el 5-oct; «no podio como está» por Innovación (19/25) | `evidencia/codex_juez_rubrica*_2026-10-05.md` |
| Simulación de la regla completa del §6 | Hecha **después** del envío, pre-registrada, en GPU: avance 0,44 en el diseño propuesto, nunca 0,80; falso avance 0,07 con n = 23 (efecto de donante) | `potencia/RESULTADOS_REGLA_COMPLETA.md` · bitácora 2026-10-05 |

## En curso

Nada.

## Bloqueado

Nada. (El tercer envío se gastó el 5-oct sin correr antes la simulación que Codex pedía; ya no hay envío
donde ponerla. El repo público es lo que el panel verá además del PDF.)

## Próximo, con fecha

1. **Cierre del hackathon: 24-oct-2026, 23:59 UTC** (6:59 p. m. Panamá). No hay acción nuestra.
2. **Borrar los datos del paciente antes del 23-nov-2026** y enviar el correo a
   `RarediseaserealkidMVAhackathon2026@synapse.org`. Inventario y comandos: `data/BORRAR-AL-TERMINAR.md`
   (incluye los 20 GB de FASTQ y 4,6 GB de caché). ⚠️ Esta carpeta (`~/datos/HACKATHON-MVA-2026`) contiene
   los datos; el repo (`~/datos/mva-hackathon-2026`) no.
3. **Ganadores: 18-dic-2026** (anuncio #26 del Space, antes era 25-nov).
4. Embargo de publicaciones desde el cierre hasta que Sage publique su informe/preprint.

## Opcional (solo repo, no cambia el envío)

Pre-registrar y evaluar la regla corregida del §6 con la línea como efecto aleatorio (modelo mixto), en
vez de comparaciones Welch por donante. No es necesario para nada de lo anterior.

## Qué archivo manda (cuando dos se contradigan)

- Resultados numéricos: el archivo de resultados del paquete (`depmap/`, `potencia/`, `mosaico/`, `replay/`),
  nunca el reporte. `analysis/verificar_afirmaciones.py` debe dar «todo cuadra».
- Texto del reporte: `track2/PART1_decision_document.md` + `track2/REPORT_track2_EN.md` + `entrega/methods_track2.md`
  (la hoja de filtros se genera desde `track2/candidates.tsv`; no editarla a mano).
- PDF enviado: `entrega/listo-para-enviar/ciberpty_track2_report.pdf` (94 pp., sha256 `fbfd407c…`). **No se regenera**:
  `make_track2.sh` lo sobreescribiría; si hace falta reconstruir para el repo, guardar antes una copia del enviado.
- Reglas del reto: `evidencia/space_tabs_rules.py`, `space_tabs_faq.py`, anuncios #10, #18, #26.
- `evidencia/` es archivo histórico, no fuente de verdad.

## Gotchas que ahorran tiempo

- Codex como juez: pasarle el PDF por stdin con `-C` al proyecto y `-s read-only`; verificar cada hallazgo contra
  el archivo fuente antes de editar; rinde ~+5 la primera pasada y +1–2 después.
- Cursor (`agent -p --mode ask`) se queda mudo con prompts largos; ~20 KB sí.
- WeasyPrint: una `@page` apaisada no reflowea el cuerpo (`margin-left: -47mm` + ancho fijo en `report.css`).
- Gradio del Space esconde pestañas en ventana angosta: `Browser.setWindowBounds` a 1500 px.
- GPU: usarla si está libre (orden del 8-sep); el LM por lotes en PyTorch ajusta 276 k curvas en segundos.
