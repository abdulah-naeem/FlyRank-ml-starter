# Agent Build Log: News & Research Scout

**Date:** [Current Date]
**Agent Scope:** News & Research Scout (AI in SEO)
**Platform:** n8n

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
