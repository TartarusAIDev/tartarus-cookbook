# tartarus-cookbook

Runnable examples for the **Tartarus** uncensored coding API. The API is
OpenAI-compatible, so any OpenAI SDK works: just change the base URL.

- Base URL: `https://api.tartarusai.dev/v1`
- Model: `tartarus-coder`
- Auth: a bearer token from [dash.tartarusai.dev](https://dash.tartarusai.dev)
  (Account to CLI access to Generate)

## Setup

```bash
export TARTARUS_TOKEN="your-token-from-the-dashboard"
```

| Example | Language | Shows |
|---|---|---|
| [python/basic_chat.py](python/basic_chat.py) | Python | one-shot completion |
| [python/streaming.py](python/streaming.py)   | Python | token streaming |
| [python/tool_calling.py](python/tool_calling.py) | Python | function / tool calls |
| [node/basic.mjs](node/basic.mjs) | Node | one-shot completion |
| [curl/chat.sh](curl/chat.sh) | curl | raw HTTP |

## Python

```bash
pip install -r python/requirements.txt
python python/basic_chat.py
```

## Node

```bash
npm install openai
node node/basic.mjs
```

## curl

```bash
bash curl/chat.sh
```

## License

MIT.
