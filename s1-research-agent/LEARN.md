# S1 — Research agent

**The point of this sprint:** an agent is a model in a loop with tools. We build it one block at a
time, and at each step swap one block for a competitor so you can see what that layer actually does.

| Step | Block added | Layer on the map | Run |
| --- | --- | --- | --- |
| 1 | OpenRouter | Models and inference | `uv run s1-research-agent/step1_model.py` |
| 2 | Exa vs Parallel vs Firecrawl | Web access | coming |
| 3 | LangGraph | Agent runtime | coming |
| 4 | Mem0 vs Supermemory | Memory | coming |
| 5 | Braintrust | Quality: evals | coming |
| 6 | Raindrop | Quality: production monitoring | coming |

---

## Step 1 — the brain, behind a router

**What OpenRouter is:** one API in front of ~every model. You change models by changing a string,
and it can fail over when a provider is down. JTBD: "let me use the best model for this call without
integrating every lab's SDK."

**Why it's a lego block:** it decouples your app from any one lab. That's why it sits at the bottom
of the map: everything above it just calls "a model."

**Predict first:** we ask the same question 3 ways: `openrouter/auto`, a frontier closed model, and
an open-weights model (DeepSeek). Deep Cogito isn't on OpenRouter as of Oct 2026, which is
itself a lesson: open-weights labs live or die by distribution through routers and inference hosts. Which one will be fastest? Cheapest? Will `auto` pick a big or small model
for an easy question?

**Run:**
```bash
uv run s1-research-agent/step1_model.py
```

**What to notice:** the `model` field in the response (which model `auto` actually chose), latency,
and the token cost. Then ask it something current ("who won yesterday's game?") and see it fail:
a model alone knows nothing after its training cutoff. That gap is why step 2 (web access) exists.
