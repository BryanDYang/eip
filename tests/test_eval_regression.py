from pathlib import Path
import subprocess
import sys
import unittest


class TestEvalRegression(unittest.TestCase):
    def test_expected_baseline_eval_passes(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        cmd = [sys.executable, "evals/run_eval.py"]

        result = subprocess.run(
            cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            check=False,
        )

        output = (result.stdout or "") + (result.stderr or "")
        self.assertEqual(
            result.returncode,
            0,
            msg=f"Eval regression failed.\nOutput:\n{output}",
        )
        self.assertIn("0 failed", output)


if __name__ == "__main__":
    unittest.main()
