# Video de pitch — 3 minutos

**`pitch_MVA2026.mp4`** · **v5, corte documental, 8-sep-2026** · 1920×1080 · 30 fps · audio AAC.
Límite del hackathon 3:00. **177,03 s por ffprobe (2,9 s de margen) · 34,6 MB · sha256 `6e61c083…76c`** (render final 10:30, tras el recorte limpio del embudo).

**Por qué v5.** La v4 (6-sep) quedó congelada antes de la reconciliación de titulares del 7/8-sep y
decía «Bortezomib clears filter three» e «If that tumour comes, filter four inverts», dos frases que el
reporte retiró a propósito; tampoco llevaba nada del 7/8-sep (margen en fármaco libre, seguimiento
DepMap por linaje, potencia 0,17 con n = 3, transferencia a TRIP13, regeneración en un comando). El
guion v5 se redactó desde la Parte I del documento enviado, Codex (gpt-6-astra) auditó cada frase
contra ese texto (`evidencia/codex_guion_v5_2026-09-08.md`) y las frases del Track 1 se verificaron
contra `submission/ciberpty_track1_report.md`. Estructura: apertura fría → cuatro capítulos con
tarjeta (I La variante · II Cinco filtros · III Contra nosotros · IV Qué ayuda, qué escala) → cierre.

## Cómo se construye ahora

```bash
# 1. narración  (venv aparte: transformers de qwen-tts choca con el del sistema)
~/qween/.venv-tts/bin/python video/tts_qwen.py          # o  ... tts_qwen.py S7   para una sola
# 2. control: ¿dice el guion?  Falla si algún clip se desvía
python3 video/tts_verify.py
# 3. (v5) los clips crudos van a audio_raw_v5/ y se aceleran 6 % para caber en 180 s
for i in $(seq 1 10); do ffmpeg -y -i audio_raw_v5/S$i.wav -af atempo=1.06 audio/S$i.wav; done
# 4. armar la pista (clips + silencios de las tarjetas), renderizar cada fotograma y hacer el mux
cd video && python3 render_video.py                      # --probe 4  para muestras sin video
```

`render_video.py` mide las duraciones **de los propios WAV** y les intercala los silencios fijos de
la apertura, las cuatro tarjetas de capítulo y el cierre (`TIMELINE`); la misma lista construye
`narracion.wav`, así que imagen y sonido no pueden desfasarse. Aborta si el resultado pasa de 180 s.

## Por qué así

- **`deck.html` es la fuente de las 16 escenas** (apertura, 10 narradas, 4 tarjetas, cierre). Un
  fotograma es una función pura del tiempo (`seek(t)`), sin animaciones CSS ni `requestAnimationFrame`,
  así que el render es determinista. En v5 hay movimiento continuo (push-in lento sobre las figuras,
  línea de progreso), por eso se fotografía **cada fotograma** (~5.300 a 30 fps, ~10 min en CPU).
- **Tres escenas llevan figuras reales del análisis como «exhibits»** sobre tarjeta de papel
  (`track2/fig2_domains.png`, `fig3_funnel.png`, `fig5_seguimiento.png`), recortadas por CSS para
  quitarles su propio título. Los PNG no se tocan: son los mismos que van en el reporte.
- **Cada escena narrada lleva una línea de procedencia** abajo (sección del reporte, archivo de
  pre-registro, PMID o etiqueta FDA): es la señal de rigor para el panel, y el mapa para verificar.
- **La voz es Qwen3-TTS 1.7B VoiceDesign en CPU** (~50-110 s de cómputo por clip). Sin GPU, por la
  regla del proyecto. La instrucción de voz está en `tts_qwen.py`.
- ⚠️ **`tts_verify.py` no es opcional.** Un TTS basado en LLM se salta palabras sin avisar: en la
  primera pasada se comió el "to" de *"every three months, to age seven"*, y de ahí salió la
  reformulación a *"until he is seven"*. Se detectó con reconocimiento de voz, no de oído.

## Historial

v5 (8-sep): corte documental, ver arriba; `GUION_v4.md` y `audio_v4_backup/` (incluye `pitch_v4.mp4`)
conservan la versión que sigue en YouTube hasta que se suba la nueva. `slides.html` + `render.py` +
`slide0*.png` eran el deck **estático** de la v3/v4 y se eliminaron el 6-sep.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `pitch_MVA2026.mp4` | el entregable |
| `deck.html` | las 8 escenas y el motor de animación (`seek(t)`) |
| `render_video.py` | muestrea `deck.html`, encodea y hace el mux |
| `tts_qwen.py` | sintetiza `audio/S1..S8.wav` con Qwen3-TTS |
| `tts_verify.py` | transcribe cada clip y lo diffea contra el guion |
| `GUION.md` | el guion **v5** por secciones, con su registro de build |
| `assets/grain.png` | textura de grano (ruido gaussiano, generado con numpy), superpuesta al 7 % |
| `audio_raw_v5/` | los clips tal como salieron del TTS, antes del `atempo` |
| `narracion.json` | el guion extraído, lo que consume el TTS |
| `narracion.wav` | la narración completa concatenada |
| `GUION_v4.md`, `GUION_v3.md`, `GUION_v1.md` | guiones anteriores, archivados |
| `audio_piper_backup/`, `audio_v3_backup/` | narraciones anteriores, por si hay que volver |

## Cambiar la voz sintética por la tuya

Sigue siendo lo más fácil y probablemente valga la pena: un panel con defensores de pacientes responde
distinto a una voz humana. Grábate leyendo `GUION.md` sección por sección, guarda cada una como
`audio/S1.wav` … `audio/S10.wav` a **24 kHz mono** (los silencios de las tarjetas se generan a esa
frecuencia y `ffmpeg -c copy` no convierte), y corre los pasos 2 y 4 de arriba. Los tiempos de cada escena se
recalculan solos. Vigila el total: si tu lectura pasa de 180 s hay que recortar guion, no acelerar la voz.

## Si editas una escena

Edita `deck.html` y corre `python3 render_video.py --probe 3` para ver tres muestras por escena sin
generar video. Cuando cuadre, `python3 render_video.py`.

## Dirección de arte (v5)

**Documental forense.** Fondo carbón `#0f0e0d`, tinta hueso `#ece7de`, los dos acentos del informe
(verde-petróleo `#2fb5a5`, terracota `#d0563a`) y papel `#f7f5f0` para los exhibits. Bitstream Charter
para la voz narrativa, IBM Plex Mono para la procedencia. Grano y viñeta sutiles, sin música: el
silencio de las tarjetas de capítulo es el ritmo. Apertura con texto cinético al paso de la voz.
Cada escena usa un layout distinto. Sin azul corporativo, sin líneas de acento bajo los títulos.
