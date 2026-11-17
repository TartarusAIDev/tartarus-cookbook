"""Function / tool calling. Tartarus emits canonical OpenAI tool_calls arrays."""
import json
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tartarusai.dev/v1",
    api_key=os.environ["TARTARUS_TOKEN"],
)

tools = [{
    "type": "function",
    "function": {
        "name": "run_shell",
        "description": "Run a shell command and return its stdout.",
        "parameters": {
            "type": "object",
            "properties": {"cmd": {"type": "string", "description": "the command to run"}},
            "required": ["cmd"],
        },
    },
}]

messages = [{"role": "user", "content": "List the Python files in the current directory using the tool."}]

resp = client.chat.completions.create(
    model="tartarus-coder",
    messages=messages,
    tools=tools,
)

msg = resp.choices[0].message
if msg.tool_calls:
    for call in msg.tool_calls:
        print(f"{call.function.name}({call.function.arguments})")
else:
    print(msg.content)
