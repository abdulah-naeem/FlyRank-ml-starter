# Capstone Report — Predictive Ranking & Action Playbook

- **Author:** Abdullah Naeem
- **Lane:** Machine Learning Engineer
- **Repo:** FlyRank-ml-starter
- **Date:** September 10, 2026

## 0. Abstract

This project aims to predict which pages have the highest probability of entering the top 3 search visibility positions within 30 days to optimize editorial resources. Using the FlyRank organic traffic dataset, I engineered historical visibility features while strictly isolating label-derived fields to prevent target leakage. A Random Forest model was trained and evaluated using a strict `client_id` grouped split to ensure out-of-sample generalization. The resulting model achieved a Precision@50 of 0.960 against a dataset base rate of 0.511, demonstrating strong discriminatory power. This output directly drives a weekly Action Playbook, routing high-potential pages to editors for immediate content updates while ignoring pages in natural decay.

## 1. Problem framing

Search visibility optimization is resource-intensive; editorial teams often waste hours rewriting content that is already decaying naturally, while missing pages that are on the verge of ranking in top positions. This model supports the **editorial prioritization decision**. The unit of analysis is the **page**. The output is a **probability score and ranking** indicating the likelihood of that page achieving a top-3 ranking in the next 30 days. A human editor uses this ranked list to assign immediate content refreshes or technical SEO audits. The cost of a wrong call (false positive) is wasted editorial time on a page that won't rank; therefore, the model optimizes strictly for high Precision at the top of the queue (Precision@50). Data and ML are necessary here because human editors cannot manually spot non-linear historical impression trajectories across thousands of URLs simultaneously.

## 2. Data safety

I used the core historical performance columns from the dataset (`impressions`, `clicks`, `position` aggregated over 30 and 90-day windows). I deliberately excluded all "future" looking columns (like `future_clicks`) and label-derived fields (`trend_direction`, `trend_pct`) from the feature space, as including them causes catastrophic target leakage (where the model "cheats" by looking at the outcome). Furthermore, pseudonymous IDs (like `client_id` and `url_id`) were used strictly for grouping data during train/test splits and never passed to the model as predictive features. I have confirmed that no client-identifying details (e.g., raw URLs or client names) appear anywhere in this repository or in the evaluation data.

## 3. Baseline

The baseline model used was a transparent heuristic score based purely on simple historical traffic volume (sorting pages descending by `impressions_prev_30d`). This is a fair comparison because it represents the standard "common sense" approach a human analyst would use to prioritize pages. Evaluated on the exact same holdout split, this baseline achieved a Precision@50 of 0.545, which is only marginally better than the underlying dataset base rate (0.511).

## 4. Model / analysis

I implemented a tree-based method (Random Forest classifier). This fits the lane because tree ensembles handle the non-linear thresholds typical of search engine ranking behavior (e.g., the massive difference between ranking #4 and ranking #3) without requiring complex feature scaling. The exact feature list included `impressions_prev_30d`, `impressions_90d`, `days_with_impressions`, `avg_position`, and `impressions_last_30d`. I purposely left out click-through-rate (CTR) derivatives that were too closely correlated with the target variable. The target proxy definition is: *A binary flag indicating if the page achieved an average position <= 3.0 during the forward-looking 30-day window.*

## 5. Evaluation

The data was evaluated using `GroupShuffleSplit`, grouping strictly by `client_id`. This guarantees that the model cannot memorize client-specific URL structures and is forced to learn generalized traffic patterns. 

**Metrics (evaluated on the same split):**
- **Model Precision@50:** 0.960
- **Baseline Precision@50:** 0.545
- **Dataset Base Rate:** 0.511

An analysis of the model's errors (the 4% false positives in the top 50) revealed that the model occasionally gets fooled by pages that have massive, short-term viral impression spikes (e.g., news articles) that quickly vanish, rather than sustained evergreen intent.

## 6. Interpretation

The model clearly indicates that long-term, sustained visibility is the strongest indicator of future top-3 ranking potential. The feature importances reflect this:
1. `impressions_prev_30d` (0.270)
2. `impressions_90d` (0.111)
3. `days_with_impressions` (0.102)

Interestingly, short-term recent impressions (`impressions_last_30d`) had a relatively low importance (0.069). A well-understood "no effect" finding here is that sudden, massive 3-day traffic spikes do not reliably predict sustained top-3 rankings, validating the hypothesis that search engines prefer pages with historical stability.

## 7. Recommendation

The output of this model feeds directly into the FlyRank Action Playbook. The system outputs a ranked queue of the top 50 URLs per week. A FlyRank editor will pull this queue and apply predefined reason codes (e.g., "High Impression / Decaying CTR -> Rewrite Title Tag"). 
**Confidence and Limits:** The model is highly confident in its top 50 predictions (96% precision). However, its limitation is that it is purely behavioral; it does not read the actual text on the page. Therefore, it cannot recommend *what* text to change, only *which* page is mathematically closest to breaking through.

## 8. Reproducibility

To re-run this pipeline from a fresh clone:
1. Ensure the dataset is placed in the root directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Execute the data preparation and baseline generation: `jupyter nbconvert --to notebook --execute work/notebooks/w04_baseline_score.ipynb`
4. Execute the honest evaluation harness (with `random_state=42`): `jupyter nbconvert --to notebook --execute work/notebooks/w06_validation_audit.ipynb`
5. Generate the final playbook queue: `jupyter nbconvert --to notebook --execute work/notebooks/w07_action_playbook.ipynb`

All evaluation metrics and splits were generated using a fixed random seed (`42`) and the final metrics file is committed to `work/outputs/`.

## 9. Acknowledgments & data credit

Built on the FlyRank ML Internship dataset.
[https://flyrank.ai](https://flyrank.ai)
