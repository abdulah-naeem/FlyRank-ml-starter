# Capstone Agent Design: The News & Research Scout

## 1. Job to be Done
The agent autonomously monitors specific industry RSS feeds and search queries, extracts full article content, evaluates relevance against a specific rubric (e.g., "AI Engineering & SEO"), and compiles a synthesized daily brief. Instead of just regurgitating headlines, it reads the full text to extract actionable insights and drops fluff/irrelevant pieces.

## 2. User & Usage Frequency
- **User:** Me (The ML/AI Developer).
- **Usage Frequency:** Runs once daily at 8:00 AM automatically via a cron trigger, plus on-demand manual triggering for ad-hoc deep dives when news breaks.

## 3. Tools and Data Needed
- **RSS / Webhook Trigger (n8n):** To pull in daily headlines from sources like KDnuggets, SearchEngineLand, or Google News RSS. *(Access Plan: Free, public XML feeds).*
- **HTTP Request Node:** To scrape the raw HTML of target URLs. *(Access Plan: Free native n8n node).*
- **LLM Node (Groq / Gemini):** To parse messy HTML into clean text, evaluate relevance, and extract insights. *(Access Plan: Free tier API keys already secured and tested in Week 4).*
- **Google Docs / Slack / Markdown Node:** To deliver the final synthesized brief to a readable format. *(Access Plan: Free personal OAuth integration or writing to local file).*

## 4. Draft Instructions (System Prompt)
> "You are an expert AI & SEO research scout. Your job is to read raw text from industry articles and determine if they contain actionable insights regarding LLMs, RAG, or search ranking algorithms. 
> 
> For every article provided:
> 1. Score relevance (1-10). If < 7, discard.
> 2. If >= 7, extract the core problem, the proposed solution, and one actionable takeaway.
> 3. Output strictly in valid JSON format. 
> 
> Never hallucinate facts. If the article is a fluff piece, an advertisement, or unrelated to AI/SEO, score it a 1."

## 5. Five Eval Cases (Pre-build)
To ensure the agent actually works, it must pass these 5 tests before deployment:
1. **High Relevance (The Golden Path):** Input an article about a new Google core update penalizing AI-generated content. *Expected:* Score 9+, with a precise summary of the penalty mechanism.
2. **Low Relevance (The Distractor):** Input an article about a general tech company's stock price or hardware release. *Expected:* Score < 7, successfully discarded from the brief.
3. **Paywall/Scrape Fail (The Error Handle):** Input a URL that returns "Access Denied" or a JS-heavy blank page. *Expected:* The agent gracefully flags the URL as "Unreadable" rather than hallucinating content to fill the void.
4. **Ad-Heavy Fluff (The Noise):** Input a heavily sponsored post masquerading as news (e.g., "Top 10 tools to buy"). *Expected:* Agent recognizes the lack of technical substance and scores < 7.
5. **Synthesis (The Merge):** Input 3 highly relevant articles covering the exact same event. *Expected:* The final synthesis node merges the overlapping concepts into one bullet point instead of printing 3 separate identical takeaways.

## 6. Risks and Guardrails
- **What it must confirm:** If an API quota is reached (e.g., Groq rate limits), the workflow must pause and notify me rather than silently failing and producing empty briefs.
- **What it must never do:** The agent must *never* autonomously publish the brief to a public audience (e.g., a newsletter, blog, or Twitter) without human approval. It must remain a "read-only" research assistant that delivers to a private inbox.

## 7. Platform Choice & Justification
- **Selected Platform:** n8n Agent Workflow.
- **Justification:** n8n provides a perfect hybrid between pure code (Python) and pure prompting (Custom GPTs). Unlike a Custom GPT or Claude Cowork, which are sandboxed and require a $20/mo subscription to run automated scheduling reliably, n8n is entirely free to self-host. It allows us to visually map the flow of data (RSS -> Scrape -> LLM -> Delivery) while still having the power to inject custom logic for data cleaning. Using free inference APIs like Groq keeps the operating cost at $0. This scope is highly achievable within the 10-hour build constraint.
