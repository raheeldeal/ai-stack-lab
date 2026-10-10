# ai-stack-lab

Hands-on tour of the AI agent stack: five sprints, ~50 companies, one evolving agent.
Map + per-product notes: [AI Stack Product Playbook](https://claude.ai/artifact/8Ug5YpUm8LpPU7WSgjMqjr)

## How each step works (the learning loop)

1. **Read** the step in the sprint's `LEARN.md`: what block we're adding, and why it exists.
2. **Predict** the answer to the step's question before running anything. Write it down.
3. **Run** the step's command.
4. **Compare** what happened with your prediction. Write one line in `LEARNING-LOG.md`.
5. **Commit.** One commit per step, so `git log` reads as a record of what you learned.

## Sprints

| Sprint | Builds | Products |
| --- | --- | --- |
| [S1](s1-research-agent/LEARN.md) | Research agent | OpenRouter, Deep Cogito, Exa, Parallel, Firecrawl, LangGraph, Mem0, Supermemory, Braintrust, Raindrop |
| S2 | Agent that acts | Composio, Arcade, Browserbase, E2B, Daytona, Straiker |
| S3 | Voice agent | Vapi, Cartesia, Coval, Sesame |
| S4 | Dev loop | CodeRabbit, Greptile, Blacksmith, Meticulous, Warp |
| S5 | Agent economy | Natural, Beltic, Conway, Naive, x402 |

## Setup

```bash
cp .env.example .env   # then paste your keys into .env (never commit it)
uv sync
```
