"""One-shot completion against the Tartarus coding API."""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tartarusai.dev/v1",
    api_key=os.environ["TARTARUS_TOKEN"],
)

resp = client.chat.completions.create(
    model="tartarus-coder",
    messages=[
        {"role": "system", "content": "You are a terse senior engineer."},
        {"role": "user", "content": "Write a Python function that validates an IPv4 address without regex."},
    ],
)

print(resp.choices[0].message.content)
