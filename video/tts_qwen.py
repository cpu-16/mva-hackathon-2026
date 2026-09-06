"""Synthesise the pitch narration with Qwen3-TTS VoiceDesign, on CPU.

Run with the dedicated venv:  ~/qween/.venv-tts/bin/python video/tts_qwen.py [S1 S2 ...]
Writes audio/S*.wav at 24 kHz. Verify afterwards with tts_verify.py (Qwen3-ASR), which is the
control that catches the failure mode that matters here: an LLM-based TTS silently dropping or
inventing words. ponytail: no batching, no streaming — 8 clips, run it once.
"""
import json, sys, time
from pathlib import Path
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

HERE = Path(__file__).resolve().parent
MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"

# The panel includes clinicians and patient advocates: credible and warm, never salesy.
INSTRUCT = (
    "A male documentary narrator in his forties, neutral international English. Warm, calm and "
    "measured, with the unhurried authority of a science broadcaster. Clear articulation, natural "
    "sentence rhythm, small pauses at commas and full stops. Serious and sincere, never dramatic, "
    "never cheerful, never salesy. Speak at a steady moderate pace."
)

def main(argv):
    script = json.loads((HERE / "narracion.json").read_text(encoding="utf-8"))
    keys = argv or sorted(script)
    print(f"loading {MODEL} on cpu", flush=True)
    t0 = time.time()
    model = Qwen3TTSModel.from_pretrained(MODEL, device_map="cpu", dtype=torch.float32)
    print(f"loaded in {time.time()-t0:.0f}s", flush=True)

    (HERE / "audio").mkdir(exist_ok=True)
    for k in keys:
        text = script[k]
        t1 = time.time()
        wavs, sr = model.generate_voice_design(text=text, instruct=INSTRUCT, language="English")
        w = np.asarray(wavs[0], dtype=np.float32)
        peak = float(np.max(np.abs(w))) or 1.0
        w = w / peak * 0.89                      # headroom, so the mux does not clip
        out = HERE / "audio" / f"{k}.wav"
        sf.write(out, w, sr)
        print(f"{k}: {len(text.split())} words -> {len(w)/sr:.2f}s audio in {time.time()-t1:.0f}s", flush=True)
    print("done", flush=True)

if __name__ == "__main__":
    main(sys.argv[1:])
