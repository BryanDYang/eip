# Evaluation Folder Guide

Use this folder for machine-checkable validation data and scripts.

## What goes here

- expected_baseline.json: expected outputs/checks for the current baseline dataset.
- future: eval runner scripts and result logs.

## Separation of concerns

- docs/: human-facing intent and design notes.
- evals/: explicit checks and expected values.

## Suggested workflow

1. Pick a question from docs/sample_questions.md.
2. Run main.py and collect the response JSON.
3. Compare the response against the matching case in expected_baseline.json.
4. Mark pass/fail and a short reason.

## Run the baseline checks

1. From the project root, run: `python evals/run_eval.py`
2. Review PASS/FAIL output per case.
3. If a case fails due to scope, keep it as known gap and revisit when adding features.

## Notes

- Keep strict numeric checks only for stable metrics.
- Use qualitative checks for narrative questions.
- When the dataset changes, bump baseline version and update expected values.
