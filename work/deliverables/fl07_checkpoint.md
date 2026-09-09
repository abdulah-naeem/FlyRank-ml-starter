# FL-07 Checkpoint: News & Research Scout — MVP Agent

**Date:** September 9, 2026  
**Status:** ✅ Complete — Agent runs end-to-end in a single click  
**Platform:** n8n (self-hosted via Docker)  
**LLM Provider:** Groq (free tier) — `openai/gpt-oss-20b`

---

## Agent Summary

The News & Research Scout is an n8n workflow that autonomously fetches industry articles, scrapes their content, uses an LLM to score relevance and extract insights, filters out low-value pieces, and compiles a synthesized daily brief — all in one click.

### Final Pipeline (8 Nodes)

```
Manual Trigger → RSS Read → Remove Duplicates → Limit (3)
    → HTTP Request (scrape) → Basic LLM Chain (Groq)
    → IF (relevance ≥ 7) → Code (format brief)
```

### Sample Output

From the successful run on September 9, 2026:
- **Input:** 10 articles from SearchEngineLand RSS
- **Processed:** 3 articles (after dedup + limit)
- **Filtered:** 2 articles scored 2/10 → dropped | 1 article scored 9/10 → kept
- **Brief Generated:** Markdown report with problem, solution, and actionable takeaway

---

## Deliverable Links

| Deliverable | Path |
|---|---|
| **Build Log** (8 iterations) | [build_log.md](file:///d:/Internships/Internship%20-%20FlyrankAI/Week%201/FlyRank-ml-starter/work/deliverables/build_log.md) |
| **Agent Design Spec** (FL-06) | [capstone_agent_design.md](file:///d:/Internships/Internship%20-%20FlyrankAI/Week%201/FlyRank-ml-starter/work/deliverables/capstone_agent_design.md) |
| **n8n Workflow JSON** (latest) | [rss news parser complete n8n.json](file:///d:/Internships/Internship%20-%20FlyrankAI/Week%201/FlyRank-ml-starter/work/rss%20news%20parser%20complete%20n8n.json) |
| **n8n Setup Guide** | [n8n_setup_guide.md](file:///d:/Internships/Internship%20-%20FlyrankAI/Week%201/FlyRank-ml-starter/work/deliverables/n8n_setup_guide.md) |
| **Run Screenshot (full workflow)** | `n8n rss complete with clean results.png` |
| **Run Screenshot (code output)** | `n8n rss code node.png` |

---

## Spec Compliance Checklist (FL-06 → FL-07)

| FL-06 Spec Requirement | Status | Notes |
|---|---|---|
| Monitors RSS feeds for articles | ✅ | SearchEngineLand RSS feed |
| Scrapes full article content | ✅ | HTTP Request node with truncation |
| LLM scores relevance (1-10) | ✅ | Groq `openai/gpt-oss-20b`, JSON output |
| Filters articles scoring < 7 | ✅ | IF node drops low-relevance articles |
| Compiles synthesized daily brief | ✅ | Code node outputs Markdown report |
| Cron trigger (daily 8 AM) | ⚠️ Deviated | Manual Trigger — Docker can't run 24/7 (documented in Iteration 4) |
| Uses n8n platform | ✅ | Self-hosted n8n via Docker |
| Uses free-tier APIs only | ✅ | Groq free tier, public RSS feeds |
| Continue-on-fail guardrail | ✅ | HTTP Request node has `continueOnFail: true` |
| Never publishes without approval | ✅ | Output stays in n8n — no external publishing |

---

## FL-07 Rubric Mapping

| Criterion | Evidence |
|---|---|
| Agent completes core job end-to-end without hand-editing | Single "Execute Workflow" click runs all 8 nodes to completion |
| At least one live tool/data connection | RSS feed fetch (live HTTP) + Groq API call (live LLM inference) = 2 live connections |
| Matches FL-06 spec or deviations documented | Cron → Manual Trigger deviation documented in build log (Iteration 4) |
| Build log shows real iteration | 8 iterations with real errors, timestamps, and fixes — not a retroactive clean story |
| Run capture shows full loop | Screenshots show: trigger → RSS → scrape → LLM → filter → brief |

---

## How to Run

1. Start Docker Desktop
2. Run n8n container: `docker run -it --rm -p 5678:5678 n8nio/n8n`
3. Open `http://localhost:5678`
4. Import workflow JSON from `work/rss news parser complete n8n.json`
5. Add Groq API credential (Settings → Credentials → Header Auth)
6. Click **"Execute Workflow"**
7. Check the Code node output for the generated brief
