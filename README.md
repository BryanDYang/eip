# Energy Intelligence Platform

An AI energy analysis platform built in three layers:

1. Agent layer
2. Evaluation layer
3. Application layer

The project is designed to show three distinct engineering competencies within one system:

- building agentic AI workflows
- evaluating model quality, latency, and cost
- delivering a production-style application

## Why This Project

This project is intentionally energy-focused rather than generic. It builds on existing domain context while still showing the kind of AI engineering work that maps well to agent systems, LLM evaluation, and real product delivery.

The goal is not to build three disconnected demos. The goal is to build one coherent platform with depth.

## Current Focus

Current focus is `Layer 1: Agent`.

The current implementation is a Python-based CAISO demand analyst. It loads daily demand CSVs, calculates simple peak and summary metrics, and prepares the project for a structured agent response.

UI is not required for the first phase. The first interface can be a CLI script or a small API endpoint.

## Current Status

Implemented so far:

- repo structure for `app/`, `data/`, `docs/`, `evals/`, and `ui/`
- Pydantic schemas for analysis requests and responses
- a CAISO demand analysis tool that computes daily and multi-day metrics

Still in progress:

- wiring the agent flow end to end
- deciding between CLI and FastAPI for the first interface
- adding sample prompts and basic validation

## The Three Layers

### Layer 1: Agent

What it shows:
- building agentic AI systems

Initial capabilities:
- user asks an energy analysis question
- agent calls one or more tools
- tool reads CAISO demand data or performs a calculation
- agent returns insights in a structured format

Example prompt:
- `Analyze CAISO demand trends over the last 7 days and summarize key changes.`

### Layer 2: Evaluation

What it shows:
- understanding LLM performance and tradeoffs

Planned capabilities:
- compare multiple models such as OpenAI, open-source, and watsonx
- score outputs on task quality
- track latency and cost

### Layer 3: Application

What it shows:
- building a production-style AI product

Planned capabilities:
- user-facing interface
- visualizations and result views
- deployment, logging, and monitoring

## MVP Scope

The first version should stay narrow:

- one use case
- one data source: CAISO demand CSVs
- one tool
- one agent flow
- one structured output schema

Suggested MVP use case:
- analyze regional demand data and return a concise summary with structured metrics

Why this use case:
- directly maps to real utility planning and operations concerns
- easier to prototype than outage prediction, pricing forecasting, or DER orchestration
- easy to explain in interviews
- supports later expansion into forecasting, reliability analysis, and evaluation

## Initial Tech Direction

Core stack for early development:

- `Python` for agent logic and experimentation
- `Pydantic` for typed input/output schemas
- `pandas` for data handling
- `FastAPI` or CLI for the first interface
- one model provider to start

Future production direction:

- keep the AI workflow in `Python`
- move a serving or tool component to `Go` later if it adds clear backend value

## Proposed Repo Structure

```text
app/
  agents/
  tools/
  schemas/
  api/
data/
evals/
ui/
docs/
```

## Near-Term Roadmap

### Now

- finish the layer-1 agent flow so it returns a structured response
- decide whether the first interface should be CLI or FastAPI
- define 5 to 10 analyst-style sample questions
- validate the CAISO demand analyzer with a small prompt set

### Next

- expose the agent through `FastAPI` or a CLI
- add logging
- add a second tool for price or net demand analysis
- add a basic evaluation harness

### Later

- build the full evaluation layer
- add the application layer UI
- move one serving or tool component to `Go`

## Constraints

To keep the project focused:

- no UI requirement in layer 1
- no multi-agent setup in the MVP
- no vector database unless the use case actually requires retrieval
- no unnecessary infrastructure before the core agent works

## Layer 1 Questions To Support

The first version should handle simple analyst-style questions such as:

- `Analyze CAISO load trends over the last 7 days.`
- `What were the biggest price spikes and when did they happen?`
- `Summarize peak demand periods for this region.`
- `Return key metrics and a short analyst summary.`

## Layer 1 Output Shape

The initial structured response should include fields such as:

- `region`
- `time_range`
- `peak_demand`
- `average_price`
- `notable_spikes`
- `summary`
- `notes`
