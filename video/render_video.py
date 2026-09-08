"""Render deck.html to frames and mux with the narration (v5, documentary cut).

A frame is a pure function of time (deck.html exposes seek(t)), so the renderer steps time itself.
v5 has continuous motion (slow push-ins on the exhibits, a progress line), so every frame is shot:
about 5,300 screenshots at 30 fps, split across WORKERS Chromium pages (a screenshot is single-threaded;
12 pages keep the 32 cores busy). ponytail: no cache — run it once.

The timeline is narration clips (durations read from the WAVs) interleaved with silent beats
(title, chapter cards, closing hold) whose lengths are fixed here. The same list builds the audio,
so picture and sound cannot drift.

  python3 render_video.py            # full build -> pitch_MVA2026.mp4
  python3 render_video.py --probe 4  # 4 stills per scene, no video
  python3 render_video.py --audio    # only assemble narracion.wav
"""
import argparse, asyncio, json, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAMES = HERE / "_frames"
FPS = 30
LIMIT = 180.0
# (scene id, seconds or "wav")  — order is the film
TIMELINE = [
    ("open", 1.4), ("S1", "wav"),
    ("c1", 1.1), ("S2", "wav"), ("S3", "wav"),
    ("c2", 1.1), ("S4", "wav"), ("S5", "wav"),
    ("c3", 1.1), ("S6", "wav"), ("S7", "wav"), ("S8", "wav"),
    ("c4", 1.1), ("S9", "wav"), ("S10", "wav"),
    ("end", 2.0),
]


def probe(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout)


def cues():
    t, out = 0.0, []
    for sid, d in TIMELINE:
        dur = probe(HERE / "audio" / f"{sid}.wav") if d == "wav" else float(d)
        out.append({"id": sid, "start": round(t, 4), "dur": round(dur, 4)})
        t += dur
    return out, t


def build_audio(c):
    """narracion.wav = clips and silences in timeline order, all 24 kHz mono."""
    parts = []
    for cue in c:
        wav = HERE / "audio" / f"{cue['id']}.wav"
        if wav.exists():
            parts.append(f"file '{wav}'")
        else:
            sil = HERE / "audio" / f"_sil_{cue['id']}.wav"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
                            "-i", f"anullsrc=r=24000:cl=mono", "-t", f"{cue['dur']:.4f}", str(sil)], check=True)
            parts.append(f"file '{sil}'")
    lst = HERE / "audio" / "list.txt"
    lst.write_text("\n".join(parts) + "\n")
    out = HERE / "narracion.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", str(out)], check=True)
    return out


WORKERS = 12          # Chromium pages shooting in parallel; each page renders its own copy of the deck


async def shoot(times, cues_, probe_n=0):
    from playwright.async_api import async_playwright
    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir()
    jobs = list(enumerate(times))
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--force-device-scale-factor=1", "--hide-scrollbars"])

        async def worker(w):
            pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
            await pg.goto(f"file://{HERE}/deck.html")
            await pg.wait_for_timeout(1500)           # fonts + the PNG exhibits
            await pg.evaluate("c => { window.CUES = c; }", cues_)
            for n, t in jobs[w::WORKERS]:
                await pg.evaluate("t => window.seek(t)", t)
                await pg.screenshot(path=str(FRAMES / f"f{n:05d}.png"))
                if w == 0 and n % (WORKERS * 50) == 0:
                    print(f"  ~{n}/{len(times)} @ {t:.1f}s", flush=True)
            await pg.close()

        await asyncio.gather(*(worker(w) for w in range(WORKERS)))
        await b.close()


def encode(nframes, narr, out):
    dur = probe(narr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error",
                    "-framerate", str(FPS), "-i", str(FRAMES / "f%05d.png"),
                    "-i", str(narr),
                    "-vf", "format=yuv420p",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", "-t", f"{dur:.3f}",
                    "-movflags", "+faststart", str(out)], check=True)
    got = probe(out)
    print(f"{out.name}: {got:.2f}s")
    assert got <= LIMIT, f"OVER THE {LIMIT:.0f} s LIMIT: {got}"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", type=int, default=0, help="render N sample stills per scene and stop")
    ap.add_argument("--audio", action="store_true", help="only assemble narracion.wav")
    a = ap.parse_args()
    CUES, TOTAL = cues()
    print("scenes:", " ".join(f"{c['id']}={c['dur']:.1f}" for c in CUES), f"| total {TOTAL:.2f}s")
    assert TOTAL <= LIMIT, f"timeline is {TOTAL:.2f}s, over {LIMIT:.0f}"
    narr = build_audio(CUES)
    if a.audio:
        sys.exit(0)
    if a.probe:
        times = [c["start"] + (c["dur"] - 0.05) * k / max(1, a.probe - 1) for c in CUES for k in range(a.probe)]
    else:
        times = [n / FPS for n in range(int(TOTAL * FPS))]
    print(f"{len(times)} frames to shoot")
    asyncio.run(shoot(times, CUES, a.probe))
    if a.probe:
        print(f"stills in {FRAMES}")
    else:
        encode(len(times), narr, HERE / "pitch_MVA2026.mp4")
