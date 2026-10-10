"""Step 1: one question, three models, through one router (OpenRouter)."""

import os
import sys
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OpenRouter speaks the OpenAI API, so the OpenAI SDK works with a different base_url.
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])

QUESTION = sys.argv[1] if len(sys.argv) > 1 else "In two sentences: what does a vector database do?"

# Change these strings to try any model listed at openrouter.ai/models.
MODELS = [
    "openrouter/auto",              # the router picks for you
    "anthropic/claude-sonnet-5.5",  # a frontier closed model
    "deepseek/deepseek-v4.1-flash", # open weights (Deep Cogito isn't on OpenRouter as of Oct 2026)
]

for model in MODELS:
    start = time.time()
    try:
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": QUESTION}])
    except Exception as e:
        print(f"\n=== {model}: failed ({e}). Check the slug at openrouter.ai/models")
        continue
    print(f"\n=== asked for: {model}  |  answered by: {r.model}  |  {time.time() - start:.1f}s"
          f"  |  tokens in/out: {r.usage.prompt_tokens}/{r.usage.completion_tokens}")
    print(r.choices[0].message.content.strip())
