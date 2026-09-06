# Video de pitch — 3 minutos

**`pitch_MVA2026.mp4`** · **2:56.1** · 1920×1080 · 30 fps · 6,6 MB · audio AAC.
Límite del hackathon 3:00, así que quedan **3,9 s de margen**. Regenerado el 6-sep-2026 (guion v4,
deck animado, voz Qwen3-TTS).

## Cómo se construye ahora

```bash
# 1. narración  (venv aparte: transformers de qwen-tts choca con el del sistema)
~/qween/.venv-tts/bin/python video/tts_qwen.py          # o  ... tts_qwen.py S7   para una sola
# 2. control: ¿dice el guion?  Falla si algún clip se desvía
python3 video/tts_verify.py
# 3. concatenar y renderizar el deck animado + mux
cd video && ffmpeg -y -f concat -safe 0 -i audio/list.txt -c copy narracion.wav
python3 render_video.py                                  # --probe 3  para muestras sin video
```

`render_video.py` mide las duraciones **de los propios WAV**, así que los tiempos de cada escena se
recalculan solos cuando cambia la narración. Aborta si el resultado pasa de 180 s.

## Por qué así

- **`deck.html` es la fuente de las 8 escenas.** Un fotograma es una función pura del tiempo
  (`seek(t)`), sin animaciones CSS ni `requestAnimationFrame`, así que el render es determinista y
  se puede muestrear solo donde algo se mueve: **888 fotogramas en vez de 5.300** para el mismo 30 fps.
- **Tres escenas llevan figuras reales del análisis** (`track2/fig2_domains.png`, `fig3_funnel.png`,
  `fig4_depmap.png`), recortadas por CSS para quitarles su propio título y no mezclar tipografías.
  Los PNG no se tocan: son los mismos que van en el reporte.
- **La voz es Qwen3-TTS 1.7B VoiceDesign en CPU** (~50-110 s de cómputo por clip). Sin GPU, por la
  regla del proyecto. La instrucción de voz está en `tts_qwen.py`.
- ⚠️ **`tts_verify.py` no es opcional.** Un TTS basado en LLM se salta palabras sin avisar: en la
  primera pasada se comió el "to" de *"every three months, to age seven"*, y de ahí salió la
  reformulación a *"until he is seven"*. Se detectó con reconocimiento de voz, no de oído.

## Historial

`slides.html` + `render.py` + `slide0*.png` eran el deck **estático** de la v3/v4 y ya **no** se usan;
se eliminaron el 6-sep. `GUION_v3.md` conserva el guion que narraba el mp4 anterior.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `pitch_MVA2026.mp4` | el entregable |
| `deck.html` | las 8 escenas y el motor de animación (`seek(t)`) |
| `render_video.py` | muestrea `deck.html`, encodea y hace el mux |
| `tts_qwen.py` | sintetiza `audio/S1..S8.wav` con Qwen3-TTS |
| `tts_verify.py` | transcribe cada clip y lo diffea contra el guion |
| `GUION.md` | el guion **v4** por secciones |
| `narracion.json` | el guion extraído, lo que consume el TTS |
| `narracion.wav` | la narración completa concatenada |
| `GUION_v3.md`, `GUION_v1.md` | guiones anteriores, archivados |
| `audio_piper_backup/`, `audio_v3_backup/` | narraciones anteriores, por si hay que volver |

## Cambiar la voz sintética por la tuya

Sigue siendo lo más fácil y probablemente valga la pena: un panel con defensores de pacientes responde
distinto a una voz humana. Grábate leyendo `GUION.md` sección por sección, guarda cada una como
`audio/S1.wav` … `audio/S8.wav` (cualquier frecuencia de muestreo, pero **la misma en las ocho**, que
`ffmpeg -c copy` no convierte), y corre los pasos 2 y 3 de arriba. Los tiempos de cada escena se
recalculan solos. Vigila el total: si tu lectura pasa de 180 s hay que recortar guion, no acelerar la voz.

## Si editas una escena

Edita `deck.html` y corre `python3 render_video.py --probe 3` para ver tres muestras por escena sin
generar video. Cuando cuadre, `python3 render_video.py`.

## Dirección de arte

Heredada del informe en PDF, a propósito: Bitstream Charter, fondo hueso `#fcfcfb`, tinta `#2a2724`,
una sola tinta de acento verde-petróleo `#1a9e8f` y terracota `#b8452a` para lo crítico. Cada slide
usa un layout distinto. Sin azul corporativo, sin líneas de acento bajo los títulos.
