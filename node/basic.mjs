// One-shot completion against the Tartarus coding API.
// npm install openai ; node node/basic.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.tartarusai.dev/v1",
  apiKey: process.env.TARTARUS_TOKEN,
});

const resp = await client.chat.completions.create({
  model: "tartarus-coder",
  messages: [{ role: "user", content: "Write a debounce function in TypeScript with types." }],
});

console.log(resp.choices[0].message.content);
