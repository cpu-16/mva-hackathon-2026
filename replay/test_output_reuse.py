"""Regression checks for stale results; synthetic files, no genomic tools or data."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("mva_replay", Path(__file__).with_name("mva_replay.py"))
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


class OutputReuseTests(unittest.TestCase):
    def test_existing_outputs_rejected_before_any_read_or_write(self):
        for artifact in (".vcf.gz", "_planted.genes.tsv", ".json", "_planted.sample.yml"):
            for dry_run in (False, True):
                with self.subTest(artifact=artifact, dry_run=dry_run), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    bg = root / "background.vcf.gz"
                    bg.touch()
                    out = root / "out"
                    out.mkdir()
                    old = out / ("BUB1B_background" + artifact)
                    old.write_text("previous result\n")
                    args = ["--gene", "BUB1B", "--allele", "chr15:100:A:T",
                            "--allele", "chr15:200:C:G", "--hpo", "HP:9999999",
                            "--background", str(bg), "--out", str(out)]
                    if dry_run:
                        args.append("--dry-run")
                    with patch.object(replay, "sh") as query, patch.object(replay, "run_exomiser") as run:
                        with self.assertRaisesRegex(SystemExit, "Choose a new --name"):
                            replay.main(args)
                        query.assert_not_called()
                        run.assert_not_called()
                    self.assertEqual(old.read_text(), "previous result\n")
                    self.assertEqual(list(out.iterdir()), [old])

    def test_distinct_name_allows_fresh_plan_and_preserves_old_output(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            bg = root / "background.vcf.gz"
            bg.touch()
            out = root / "out"
            out.mkdir()
            old = out / "BUB1B_background.json"
            old.write_text("previous result\n")
            with patch.object(replay, "sh", return_value="PUBLIC_SAMPLE"), \
                 patch.object(replay, "clinvar_status", return_value={}), \
                 patch.object(replay, "ref_ok", return_value=True), \
                 patch.object(replay, "overlaps", return_value=False), \
                 patch.object(replay, "hpo_annotated_to_gene", return_value={}), \
                 patch.object(replay, "run_exomiser") as run, contextlib.redirect_stdout(io.StringIO()) as output:
                replay.main(["--gene", "BUB1B", "--allele", "chr15:100:A:T",
                             "--allele", "chr15:200:C:G", "--hpo", "HP:9999999",
                             "--background", str(bg), "--out", str(out),
                             "--name", "fresh_case", "--dry-run"])
                run.assert_not_called()
            self.assertIn('"name": "fresh_case"', output.getvalue())
            self.assertEqual(len(list(out.glob("fresh_case_*.sample.yml"))), 4)
            self.assertEqual(old.read_text(), "previous result\n")


if __name__ == "__main__":
    unittest.main()
