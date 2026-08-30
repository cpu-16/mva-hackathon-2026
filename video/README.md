# Video de pitch — 3 minutos

**`pitch_MVA2026.mp4`** · **2:59.0** · 1920×1080 · 30 fps · 4.6 MB · audio AAC.
El límite del hackathon es 3:00, así que queda **1.0 s de margen**. Regenerado el 30-ago-2026 (guion v3).

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `pitch_MVA2026.mp4` | **el entregable** |
| `GUION.md` | el guion v2, por secciones y con los tiempos |
| `GUION_v1.md` | la versión anterior, antes de la crítica de Codex y Cursor |
| — | **v3 (30-ago):** S3, S5, S7 y S8 se rehicieron porque contradecían el reporte de la ronda 7 |
| `narracion.json` | el guion extraído, lo que consume el TTS |
| `slides.html` | las 8 slides (un solo archivo, una `<section>` por slide) |
| `slide01..08.png` | las slides renderizadas |
| `render.py` | renderiza el HTML a PNG con Playwright |
| `audio/S1..S8.wav` | la narración, un archivo por slide |
| `narracion.wav` | la narración completa concatenada |

## Cómo está hecho

Voz: **Piper TTS local** (`en_US-ryan-high`), sin servicio en la nube y sin API key.
Modelo en `/tmp/.../scratchpad/voices/` — si se borró, se vuelve a bajar de
`huggingface.co/rhasspy/piper-voices` (`en/en_US/ryan/high/`).

⚠️ **Usar siempre `--length-scale 1.415`.** El Piper instalado habla más rápido que el de la primera
grabación; sin ese factor las secciones nuevas salen 15% más veloces que las viejas y se nota al
cambiar de slide. Calibración: regenerar una sección intacta (p. ej. S1, 15.94 s) y ajustar hasta
reproducir su duración.

⚠️ **Al ensamblar, fijar `-t <duración del narracion.wav>`.** El truco de repetir la última slide en
`slides_list.txt` la duplica (el video salía 23 s más largo), y `-shortest` deja 3 s de padding del
codificador AAC. Con `-t` la duración sale exacta.

Cada slide dura exactamente lo que dura su narración, más 0.75 s de aire. La voz entra 0.35 s después
del cambio de slide para que no pise el corte.

## Cambiar la voz sintética por la tuya

Es lo más fácil de todo, y probablemente valga la pena: un panel con defensores de pacientes
responde distinto a una voz humana.

1. Grábate leyendo `GUION.md` sección por sección, y guarda cada una como `audio/S1.wav` … `audio/S8.wav`.
2. Vuelve a correr el ensamblado:

```bash
cd ~/datos/HACKATHON-MVA-2026/video
ffmpeg -y -f concat -safe 0 -i audio/list.txt -c copy narracion.wav
python3 - <<'EOF'
import subprocess
ds=[float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/S{i}.wav"],capture_output=True,text=True).stdout) for i in range(1,9)]
open('slides_list.txt','w').write("".join(f"file 'slide{i+1:02d}.png'\nduration {d:.3f}\n" for i,d in enumerate(ds))+"file 'slide08.png'\n")
print(f"total {sum(ds):.1f}s")
EOF
A=$(ffprobe -v error -show_entries format=duration -of csv=p=0 narracion.wav)
ffmpeg -y -f concat -safe 0 -i slides_list.txt -i narracion.wav -vf "fps=30,format=yuv420p" \
  -c:v libx264 -preset slow -crf 20 -c:a aac -b:a 192k -t $A -movflags +faststart pitch_MVA2026.mp4
```

**Vigila el total:** si tu lectura pasa de 180 s hay que recortar guion, no acelerar la voz.

## Si editas una slide

Edita `slides.html`, corre `python3 render.py`, y vuelve a ensamblar con el bloque de arriba.
Los tiempos no cambian mientras no toques la narración.

## Dirección de arte

Heredada del informe en PDF, a propósito: Bitstream Charter, fondo hueso `#fcfcfb`, tinta `#2a2724`,
una sola tinta de acento verde-petróleo `#1a9e8f` y terracota `#b8452a` para lo crítico. Cada slide
usa un layout distinto. Sin azul corporativo, sin líneas de acento bajo los títulos.
