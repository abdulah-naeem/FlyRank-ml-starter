# Building The News & Research Scout Agent in n8n

Here is the exact step-by-step blueprint to build your agent in your local n8n instance (at `https://noncontinuable-gertie-isostatic.ngrok-free.dev/`). 

Follow these steps to build the workflow manually, connect your tools, and capture your 2-minute video run for the Capstone!

## Step 1: The Trigger
Every agent needs to know when to wake up. 
1. Open n8n and create a new workflow.
2. Add a **Schedule Trigger** node (so it can run daily).
3. Add a **Manual Trigger** node (so you can test it on demand).
4. Connect both triggers to your next node.

## Step 2: The Data Source (RSS)
We need to fetch the raw news feed.
1. Add an **RSS Read** node.
2. Set the URL to: `https://searchengineland.com/feed` (or `https://www.kdnuggets.com/feed`).
3. Set the maximum number of items to `3` (to save API costs during testing).

## Step 3: The Web Scraper (HTTP + HTML Extract)
RSS feeds only give us the headline and a tiny snippet. We need the agent to read the *full* article.
1. Add an **HTTP Request** node.
2. Set the Method to `GET`.
3. Set the URL to the expression: `{{ $json.link }}`. (This dynamically fetches the link from the RSS node).
4. **Guardrail:** Go to the node Settings and enable "Continue On Fail". (If a site blocks the scraper, we want the agent to skip it, not crash the whole workflow!)
5. Add an **HTML Extract** node.
6. Set the CSS selector to `article, body` and extract the `text`. 

## Step 4: The Brain (Groq LLM)
Now we send the raw text to the LLM to score it and extract insights. Since we are using free Groq, we will use a standard HTTP request to their API (just like Week 4).
1. Add an **HTTP Request** node.
2. Method: `POST`
3. URL: `https://api.groq.com/openai/v1/chat/completions`
4. **Headers:**
   - `Authorization`: `Bearer YOUR_GROQ_API_KEY`
   - `Content-Type`: `application/json`
5. **Body (JSON):**
```json
{
  "model": "llama3-8b-8192",
  "response_format": {"type": "json_object"},
  "messages": [
    {
      "role": "system",
      "content": "You are an AI research scout. Read the provided article text. Score relevance to 'AI in SEO' from 1-10. If relevance >= 7, extract 'problem', 'solution', and 'takeaway'. Output ONLY valid JSON with keys: relevance_score (number), problem (string), solution (string), takeaway (string)."
    },
    {
      "role": "user",
      "content": "{{ $json.text }}"
    }
  ]
}
```

## Step 5: The Filter (Guardrail)
We only want the good stuff in our final brief.
1. Add an **IF** node.
2. For the condition, add a Number condition.
3. Value 1: `{{ JSON.parse($json.choices[0].message.content).relevance_score }}`
4. Operation: `Larger or Equal`
5. Value 2: `7`

## Step 6: The Final Delivery
1. Connect the **True** output of the IF node to a **Code** node (or an Aggregate Node).
2. The Code node should extract the `takeaway` and `solution` strings from the LLM's JSON and format them nicely.
3. Connect that to a final **Discord**, **Slack**, or **Google Docs** node to output the final brief!

> [!IMPORTANT]
> **To record your deliverable:**
> 1. Start your screen recorder.
> 2. Open this complete workflow in your n8n UI.
> 3. Click **"Test Workflow"** (or execute the manual trigger).
> 4. Record as the green checkmarks appear on each node from left to right.
> 5. Click on the final node to show the extracted, filtered insights. 
> 6. Stop recording! (This is your 2-minute raw capture).
