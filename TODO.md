## Done

- create the repo structure
- choose CAISO demand data as the first source
- define input and output schemas with Pydantic
- implement one analysis tool for CAISO demand metrics
- finish the layer-1 agent flow with structured response output
- set up CLI entrypoint in `main.py`
- write analyst-style sample questions for validation
- add baseline evaluation harness and expected checks
- add unit tests for analyzer and agent contract
- add regression test to keep eval baseline stable

## In Progress

- decide whether to keep CLI-only for now or add FastAPI endpoint next
- tighten test coverage for edge cases and malformed data

## Next

- add logging
- add a second tool for price or net demand analysis
- extend evals with intentionally failing future-scope cases
- add run-result logging for eval history

## Later

- build the evaluation layer
- add UI
- move one serving or tool component to Go
- expand toward forecasting or reliability analysis if the MVP is stable
