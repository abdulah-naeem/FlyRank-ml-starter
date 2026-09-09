# Agent Build Log: News & Research Scout

**Date:** September 9, 2026
**Agent Scope:** News & Research Scout (AI in SEO)
**Platform:** n8n (self-hosted via Docker)

### Iteration 1: The Initial MVP
- **What I built:** I started by connecting the KDnuggets RSS feed directly to a Groq LLM node.
- **What broke:** The agent produced terrible summaries. I realized that the RSS feed only contains a 2-sentence snippet in the `<description>` field, not the full article. 
- **What changed:** I had to add an HTTP Request node between the RSS and LLM nodes to actually scrape the `link` provided by the RSS feed.

### Iteration 2: Handling HTML Noise
- **What I built:** I passed the raw HTML from the HTTP Request node straight into Groq.
- **What broke:** The Groq API crashed frequently because the raw HTML (with all its inline CSS, scripts, and ads) exceeded the 8,192 token limit of the free LLaMA 3 model. 
- **What changed:** I added an **HTML Extract** node in n8n. I configured it to only extract the text from the `body` tag, stripping away the scripts and tags. This dramatically reduced the token count and made the LLM faster and more accurate.

### Iteration 3: The Filter Guardrail
- **What I built:** I added the `IF` node to filter out articles with a `relevance_score` less than 7.
- **What broke:** The IF node failed to execute because the LLM occasionally returned conversational text like *"Here is your JSON: { ... }"*, which n8n couldn't parse as a number.
- **What changed (Deviation from spec):** I had to modify the Groq HTTP request to explicitly include `"response_format": {"type": "json_object"}` in the API call, and update the system prompt to explicitly command it to output strictly JSON with no conversational prefix. This fixed the parsing error and allowed the IF node to confidently block low-relevance fluff pieces.

### Iteration 4: The Scheduling Constraint
- **What I built:** I originally planned a Schedule Trigger node to run the agent every morning at 8:00 AM, as defined in my spec.
- **What broke:** The schedule trigger requires the n8n environment to be running 24/7. Since I am hosting n8n via a local Docker container that spins down when I close my laptop, the cron job missed its execution window.
- **What changed (Deviation from spec):** I removed the Schedule Trigger and replaced it with a simple Manual Trigger. The Scout Agent will now be fired on-demand when the Docker container is active, rather than relying on a background cron scheduler.

### Iteration 5: The HTML Extract Trap
- **What I built:** I added an HTML Extract node with the CSS selector `article, .entry-content, .post-content, main` to clean scraped pages before sending to the LLM.
- **What broke:** All 3 articles returned identical text — "The big winners and losers in U.S. website traffic over the past year" — even though the RSS feed had 3 different links. The CSS selector was matching a **shared featured/trending article widget** that SearchEngineLand renders on every page, not the actual article body.
- **What changed:** I removed the HTML Extract node entirely. Instead, I pass the raw HTML directly to the LLM with `substring(0, 6000)` to truncate it, and updated the system prompt to instruct the LLM to ignore HTML tags, navigation, and sidebars. The LLM is smart enough to parse through the noise and find the real article content.

### Iteration 6: Groq Token Limit
- **What I built:** I connected the Basic LLM Chain node to a Groq Chat Model using `openai/gpt-oss-20b`.
- **What broke:** Groq returned `Request too large` — the free tier has an 8,000 TPM (tokens per minute) limit, and the full article HTML was 14,786 tokens.
- **What changed:** I added `.substring(0, 6000)` to the prompt expression to cap input at ~6,000 characters (~1,500 tokens). This keeps each request well under the 8,000 TPM limit while still providing enough article text for accurate scoring.

### Iteration 7: Model Selection for Token Efficiency
- **What I built:** I initially selected `qwen/qwen3.6-27b` as the LLM model in Groq.
- **What broke:** Nothing broke, but I realized Qwen 3.x models have **thinking mode enabled by default** — they generate hidden `<think>` reasoning tokens that still count against the Groq rate limit. For a simple "score and extract JSON" task, this was unnecessary overhead.
- **What changed:** I switched to `openai/gpt-oss-20b` — a 20B model with no hidden thinking tokens, keeping token usage minimal and staying within the free tier.

### Iteration 8: The Working Agent ✅
- **What I built:** The final 8-node pipeline: `Manual Trigger → RSS Read → Remove Duplicates → Limit (3) → HTTP Request (scrape) → Basic LLM Chain (Groq gpt-oss-20b) → IF (relevance ≥ 7) → Code (format brief)`.
- **What worked:** The agent ran end-to-end in a single click. It fetched 10 articles from SearchEngineLand, deduplicated and limited to 3, scraped each page, sent truncated HTML to the LLM, received JSON scores (two scored 2/10 → filtered out, one scored 9/10 → kept), and compiled a clean Markdown daily brief with the surviving article's problem, solution, and actionable takeaway.
- **Result:** One relevant article about "AI visibility beyond SEO" passed the filter. The brief was generated successfully.
