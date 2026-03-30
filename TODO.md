## Now

- lock the layer-1 use case to energy analyst for regional load and pricing trends
- choose the initial dataset or API source
- start with CAISO if possible
- define 5 to 10 analyst-style sample questions
- create the repo structure
- define input and output schema with Pydantic
- implement one tool
- tool goal: load data and calculate basic trend and spike metrics
- implement one agent flow
- flow goal: question -> tool call -> structured response
- test with 5 to 10 sample prompts

## Next

- expose with FastAPI or CLI
- add logging
- add a second tool
- add a basic evaluation harness
- compare structured outputs across a small prompt set

## Later

- build the evaluation layer
- add UI
- move one serving or tool component to Go
- expand toward forecasting or reliability analysis if the MVP is stable
