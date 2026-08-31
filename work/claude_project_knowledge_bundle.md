# Abdullah Naeem — ML Portfolio Knowledge Bundle for Claude Project

> **Purpose:** Upload or paste this consolidated document directly into your Claude Project Knowledge base (or Project Instructions) to prime Claude with your design system, sitemap, proof statements, and architecture rationale for the Week 5 build phase.

---

## 1. Project System Prompt & Two-Line Style Note

Paste this into the **Custom Instructions** field of your Claude Project:

```text
Style Guide: Fonts: Plus Jakarta Sans (Headings), Inter (Body). Palette: #F8FAFC (Bg), #0F172A (Text), #1E293B (Primary), #2563EB (Accent).
Mood: Minimal, high-precision ML engineering notebook — calm slate & sapphire framing clean code, data contracts, and validation metrics without visual clutter.
Target Audience: Senior Data Scientists & ML Engineering Managers hiring technically fluent interns.
Core Claim: "I build mathematically sound, leakage-free machine learning models that solve concrete business problems and deliver production-ready pipelines."
The One Action: Direct conversion to schedule a technical interview.
```

---

## 2. Identity Kit & Design System Tokens

### Typography
* **Headings:** `Plus Jakarta Sans` (Weights: 600, 700, 800) — Modern geometric sans-serif for sharp hierarchy.
* **Body Text:** `Inter` (Weights: 400, 500, 600) — High legibility for dense technical descriptions and mathematical explanations.
* **Code / Monospace:** `JetBrains Mono` / `SFMono-Regular` — Clean code snippets, metrics receipts, and parameters.

### Color Palette (Tight 4-Color Slate System)
| Token Name | Hex Code | Role & Usage |
| :--- | :--- | :--- |
| **`--bg-primary`** | `#F8FAFC` | Slate 50 canvas background (low glare, soft contrast). |
| **`--text-primary`** | `#0F172A` | Slate 900 typography (sharp, high-contrast, non-harsh black). |
| **`--brand-primary`**| `#1E293B` | Deep Slate for cards, navigation bar, primary action buttons. |
| **`--accent-color`** | `#2563EB` | Sapphire Blue for interactive hover states, metric highlights, and focus borders. |
| **`--border-muted`** | `#E2E8F0` | Slate 200 border dividers and cards. |

### Visual Brand Identity
* **Monogram Mark:** `AN.` in bold Plus Jakarta Sans inside a rounded Deep Slate squircle with a Sapphire Blue dot.
* **Logo String:** `AN. | Abdullah Naeem — MACHINE LEARNING ENGINEER`
* **Favicon:** `favicon.svg` embedded in head.

---

## 3. The One-Line Claim & Proof Statement

* **One-Line Claim:**
  > *"I build mathematically sound, leakage-free machine learning models that solve concrete business problems and deliver production-ready pipelines."*

* **One-Paragraph Proof Statement:**
  > *"I build and debug practical machine learning models that solve concrete business problems, proving my ability to go beyond academic theory into real-world application. This portfolio is built specifically for Senior Data Scientists and ML Engineering Managers who are looking to hire technically fluent interns capable of adding immediate value to their pipelines. My goal is for you to review my case studies, recognize my foundational ML skills, and email me to schedule a technical interview."*

* **The Core Action:**
  All pages funnel directly into **The One Action**: *"Schedule a Technical Interview for an ML Engineer position"* (direct mailto / calendar link).

---

## 4. Portfolio Sitemap & Content Map

```
/ (Home / Hero View)
├── /index.html                    [Hero Claim, Key Receipts Bar, Case Teasers, CTA]
├── /case-studies/
│   ├── flyrank-seo.html           [Flagship Case: Organic Traffic & Ranking Trajectory Model]
│   └── feature-leakage-audit.html [Infrastructure Case: Pre-Split Signal Auditing Framework]
└── /about.html                    [Engineering Philosophy, Workflow Audit, Technical Stack]
```

### Page Breakdown

#### 1. Home / Hero (`/index.html`)
* **Hero Banner:** Monogram `AN.`, One-line claim, primary CTA: *"Schedule a Technical Interview"*, secondary CTA: *"Explore Case Studies ↓"*.
* **Key Receipts Bar:** 3 trust metrics:
  - `0 Target Leakage Verified`
  - `99.2% Data Integrity across 100k+ rows`
  - `2 Production-Grade ML Pipelines Deployed`
* **Lead Work (Case 1):** *FlyRank Organic Search Traffic & Ranking Engine* (framing, baseline score, feature importance, deployed paper link).
* **Secondary Work (Case 2):** *Automated Signal Auditing & Feature Leakage Framework* (temporal split verification, proxy detection).
* **Technical Grounding:** Python, PyTorch, DuckDB, Pandas, Scikit-Learn, LightGBM, Git/CI.
* **Footer:** Closing conversion banner + contact links.

#### 2. Flagship Case Study (`/case-studies/flyrank-seo.html`)
* **Problem & Business Context:** Predicting search traffic changes under algorithmic volatility.
* **Data Contract & Leakage Checks:** Enforcing explicit schema validation and temporal data splits.
* **Baseline vs Model Comparison:** Naive baseline benchmark vs tuned LightGBM/PyTorch pipeline.
* **Failure Modes & Action Playbook:** Handling sudden shifts, confidence calibration, decision thresholds.

#### 3. Infrastructure Case Study (`/case-studies/feature-leakage-audit.html`)
* **Signal Audit:** Identifying subtle target proxies, lookahead bias, and post-event features.
* **Code Receipts:** Verifiable Python validation scripts and automated CI tests.

---

## 5. Technical Architecture & Hosting Stack

* **Chosen Stack:** Vanilla HTML5 + Modern CSS + Lightweight JS (Strictly Zero-Framework).
* **Host:** Vercel (Hobby Tier &bull; Edge Network).
* **Backend:** Strictly **None yet** (Static, instant loading, 100% uptime, zero npm maintenance debt).
* **Repository:** `github.com/abdulah-naeem/FlyRank-ml-starter`

