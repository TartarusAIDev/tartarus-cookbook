"""Stream tokens as they are generated."""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tartarusai.dev/v1",
    api_key=os.environ["TARTARUS_TOKEN"],
)

stream = client.chat.completions.create(
    model="tartarus-coder",
    messages=[{"role": "user", "content": "Explain, then implement, a token-bucket rate limiter in Go."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
