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

The immediate MVP is a Python-based agent that can answer an energy question, call at least one tool, run simple analysis, and return a structured response.

UI is not required for the first phase. The first interface can be a CLI script or a small API endpoint.

## The Three Layers

### Layer 1: Agent

What it shows:
- building agentic AI systems

Initial capabilities:
- user asks an energy question
- agent calls one or more tools
- tool reads data or performs a calculation
- agent returns insights in a structured format

Example prompt:
- `Analyze CA energy demand trends and summarize key changes.`

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
- one data source
- one tool
- one agent flow
- one structured output schema

Suggested MVP use case:
- analyze regional energy demand or pricing data and return a concise summary with structured metrics

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

- choose the exact layer-1 use case
- choose an initial dataset or API source
- create the repo structure
- define input and output schemas
- implement one tool
- implement one agent flow
- test with 5 to 10 sample prompts

### Next

- expose the agent through `FastAPI` or a CLI
- add logging
- add a second tool
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
