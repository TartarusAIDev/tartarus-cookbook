#!/usr/bin/env bash
# Raw HTTP call. Requires TARTARUS_TOKEN in the environment.
set -euo pipefail

curl https://api.tartarusai.dev/v1/chat/completions \
  -H "Authorization: Bearer ${TARTARUS_TOKEN:?set TARTARUS_TOKEN first}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tartarus-coder",
    "messages": [
      {"role": "user", "content": "Write a bash one-liner to find the 10 largest files under /var."}
    ]
  }'
