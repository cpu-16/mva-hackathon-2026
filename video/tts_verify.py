"""Transcribe each narration clip and diff it against the script.

The control for the failure mode that matters with an LLM-based TTS: silently dropping, duplicating
or inventing words. A clip that reads clean by ear can still have lost a "not".

  python3 video/tts_verify.py            # all sections
  python3 video/tts_verify.py S3 S6      # just these

Exit code 1 if any clip exceeds the threshold, so it can gate a build.
ponytail: difflib and whisper-base.en, not a WER library and not a big model — the number only has
to separate "said the script" from "did not".
"""
import difflib, json, re, sys
from pathlib import Path
from faster_whisper import WhisperModel

HERE = Path(__file__).resolve().parent
MAX_WER = 0.12          # the recogniser is imperfect too; this catches dropped clauses, not plurals

# Representation differences that are not TTS errors: the recogniser writes numbers as digits, uses
# US spelling, and mangles drug names. Normalise both sides the same way; a dropped or invented WORD
# still shows up.
NUMS = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8",
        "nine":"9","ten":"10","eleven":"11","twelve":"12","thirty":"30","thirtyseven":"37",
        "thousand":"1000","hundred":"100"}
SPELL = {"tumours":"tumor","tumour":"tumor","tumors":"tumor","analyses":"analysis",
         "mis":"","missegregation":"missegregation","segregation":"segregation"}
DRUGS = ["bortezomib","metformin","aicar"]

def norm(s):
    s = s.lower()
    s = re.sub(r"\bbub\s*-?\s*(1|one)\s*-?\s*b\b", "bubonebee", s)
    s = re.sub(r"\bthirty[- ]?seven\b", "37", s)
    s = re.sub(r"\bper ?cent\b|\bpercent\b", "%", s)
    s = s.replace("mis-segregation", "missegregation").replace("mis segregation", "missegregation")
    out = []
    for w in re.findall(r"[a-z0-9%]+", s):
        w = NUMS.get(w, SPELL.get(w, w))
        if not w:
            continue
        # a mangled drug name is the recogniser, not a dropped word: snap it back when it is close
        for d in DRUGS:
            if w != d and len(w) > 5 and difflib.SequenceMatcher(None, w, d).ratio() > 0.6:
                w = d
                break
        out.append(w)
    return out

def main(argv):
    script = json.loads((HERE / "narracion.json").read_text(encoding="utf-8"))
    keys = argv or sorted(script)
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    bad = []
    for k in keys:
        segs, _ = model.transcribe(str(HERE / "audio" / f"{k}.wav"), beam_size=5)
        heard = " ".join(s.text for s in segs)
        want, got = norm(script[k]), norm(heard)
        sm = difflib.SequenceMatcher(None, want, got)
        wer = 1 - sm.ratio()
        print(f"{'OK  ' if wer <= MAX_WER else 'FAIL'} {k}  diff={wer:.3f}  script={len(want)}w heard={len(got)}w")
        if wer > MAX_WER:
            bad.append(k)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                print(f"       {tag:8} script[{chr(39)}{chr(32).join(want[i1:i2])}{chr(39)}] -> heard[{chr(39)}{chr(32).join(got[j1:j2])}{chr(39)}]")
    if bad:
        print(f"\nRE-SYNTHESISE: {chr(32).join(bad)}")
        return 1
    print("\nevery clip matches its script")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
