"""Render deck.html to frames and mux with the narration.

A frame is a pure function of time (deck.html exposes seek(t)), so we only screenshot the moments
that actually move: the scene cross-dissolves and the element build-ins. Everything else is a held
still. That is ~800 screenshots instead of 5,300 for the same 30 fps result.

  python3 render_video.py            # full build
  python3 render_video.py --probe 3  # 3 sample stills per scene, no video

ponytail: no incremental cache, no parallel workers — the whole build is about three minutes.
"""
import argparse, asyncio, json, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAMES = HERE / "_frames"
FPS = 30
XF = 0.55          # must match deck.html
BUILD = 3.1        # motion window at the start of each scene (longest data-in + fade)
SCENES = [f"s{i}" for i in range(1, 9)]


def durations():
    """Scene durations = narration clip durations, read from the WAVs themselves."""
    out = []
    for i in range(1, 9):
        w = HERE / "audio" / f"S{i}.wav"
        d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", str(w)], capture_output=True, text=True).stdout.strip()
        out.append(float(d))
    return out


def cues(durs):
    t, c = 0.0, []
    for sid, d in zip(SCENES, durs):
        c.append({"id": sid, "start": round(t, 4), "dur": round(d, 4)})
        t += d
    return c, t


def moments(c, total):
    """(time, hold_seconds) pairs: dense during motion, one long still otherwise."""
    step = 1.0 / FPS
    out, i = [], 0
    while i < len(c):
        s = c[i]
        m_end = min(s["dur"], BUILD)
        t = s["start"]
        while t < s["start"] + m_end - 1e-6:          # build-in, dense
            out.append((round(t, 4), step)); t += step
        hold_until = s["start"] + s["dur"] - XF
        if hold_until > t:                            # the still, held
            out.append((round(t, 4), round(hold_until - t, 4)))
            t = hold_until
        while t < s["start"] + s["dur"] - 1e-6:       # cross-dissolve out, dense
            out.append((round(t, 4), step)); t += step
        i += 1
    return out


async def shoot(pts, probe=0):
    from playwright.async_api import async_playwright
    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir()
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--force-device-scale-factor=1", "--hide-scrollbars"])
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        await pg.goto(f"file://{HERE}/deck.html")
        await pg.wait_for_timeout(1200)               # fonts + the four PNGs
        await pg.evaluate("c => { window.CUES = c; }", CUES)
        for n, (t, _) in enumerate(pts):
            await pg.evaluate("t => window.seek(t)", t)
            await pg.screenshot(path=str(FRAMES / f"f{n:05d}.png"))
            if probe and n and n % max(1, len(pts) // probe) == 0:
                print(f"  probe {n}/{len(pts)} @ {t:.2f}s", flush=True)
        await b.close()


def encode(pts, out):
    lst = FRAMES / "list.txt"
    lines = []
    for n, (_, hold) in enumerate(pts):
        lines.append(f"file 'f{n:05d}.png'\nduration {hold:.4f}")
    lines.append(f"file 'f{len(pts)-1:05d}.png'")
    lst.write_text("\n".join(lines) + "\n")
    narr = HERE / "narracion.wav"
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(narr)], capture_output=True, text=True).stdout.strip()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error",
                    "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-i", str(narr),
                    "-vf", f"fps={FPS},format=yuv420p",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "19",
                    "-c:a", "aac", "-b:a", "192k", "-t", dur,
                    "-movflags", "+faststart", str(out)], check=True)
    got = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.strip()
    print(f"{out.name}: {float(got):.2f}s")
    assert float(got) <= 180.0, f"OVER THE 180 s LIMIT: {got}"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", type=int, default=0, help="render N sample stills per scene and stop")
    a = ap.parse_args()
    durs = durations()
    CUES, TOTAL = cues(durs)
    print("scenes:", [f"{c['id']} {c['dur']:.1f}s" for c in CUES], f"total {TOTAL:.2f}s")
    if a.probe:
        pts = [(c["start"] + min(c["dur"] - .05, BUILD) * k / max(1, a.probe - 1), 1 / FPS)
               for c in CUES for k in range(a.probe)]
    else:
        pts = moments(CUES, TOTAL)
    print(f"{len(pts)} frames to shoot")
    asyncio.run(shoot(pts, a.probe))
    if a.probe:
        print(f"stills in {FRAMES}")
    else:
        encode(pts, HERE / "pitch_MVA2026.mp4")
