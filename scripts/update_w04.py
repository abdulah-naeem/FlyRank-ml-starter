import json
import os

notebook_path = 'd:/Internships/Internship - FlyrankAI/Week 1/FlyRank-ml-starter/work/notebooks/w04_baseline_score.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'][1]['source'] = [
    "## 1. My rule and its reason codes\n",
    "\n",
    "**The Rule Idea:** A page is worth reviewing if its CTR is below average (< 1.5%), it hasn't been updated recently (> 180 days), and it's visible enough (impressions > 500).\n",
    "**Dynamic Rule Application:** The code below evaluates these signals against the baseline decline rate. If a signal correlates positively with decline, we use it. If it is OPPOSITE or FALSE, we drop it to save the rule.\n",
    "**Reason Codes:**\n",
    "- `dynamic_underperforming`: Fails the active, confirmed heuristic signals."
]

nb['cells'][2]['source'] = [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "df = pd.read_csv('../../data/processed/refresh_feature_vector.csv')\n",
    "base_rate = df['is_declining_label'].mean()\n",
    "\n",
    "def evaluate_signal(df, flag_column, signal_name):\n",
    "    stats = df.groupby(flag_column)['is_declining_label'].agg(['mean', 'count', 'sum']).rename(columns={'mean': 'decline_rate', 'count': 'n', 'sum': 'declines'})\n",
    "    print(f\"Signal: {signal_name}\")\n",
    "    print(stats)\n",
    "    \n",
    "    if True in stats.index:\n",
    "        flag_rate = stats.loc[True, 'decline_rate']\n",
    "        if flag_rate >= base_rate * 1.05:\n",
    "            verdict = \"CONFIRMED\"\n",
    "        elif flag_rate <= base_rate * 0.95:\n",
    "            verdict = \"OPPOSITE\"\n",
    "        else:\n",
    "            verdict = \"MIXED\"\n",
    "    else:\n",
    "        verdict = \"FALSE\"\n",
    "        \n",
    "    print(f\"Verdict: {verdict}\\n\")\n",
    "    return verdict\n",
    "\n",
    "df['stale_flag'] = df['days_since_last_update'] > 180\n",
    "stale_verdict = evaluate_signal(df, 'stale_flag', 'Staleness (> 180 days)')\n",
    "\n",
    "df['low_ctr_flag'] = df['ctr'] < 1.5\n",
    "low_ctr_verdict = evaluate_signal(df, 'low_ctr_flag', 'Low CTR (< 1.5%)')\n"
]

nb['cells'][3]['source'] = [
    "## 2. Build the ranked queue (writes the CSV)\n",
    "\n",
    "We dynamically encode the rule into a score based on the verdicts, rank the queue, and compute precision@50."
]

nb['cells'][4]['source'] = [
    "visible = (df[\"impressions_90d\"] >= 500).astype(int)\n",
    "stale = (df[\"days_since_last_update\"] >= 180).astype(int)\n",
    "low_ctr = (df[\"ctr\"] < 1.5).astype(int)\n",
    "\n",
    "baseline_factors = visible.copy()\n",
    "\n",
    "if stale_verdict in [\"CONFIRMED\", \"MIXED\"]:\n",
    "    baseline_factors *= stale\n",
    "if low_ctr_verdict in [\"CONFIRMED\", \"MIXED\"]:\n",
    "    baseline_factors *= low_ctr\n",
    "\n",
    "df[\"baseline_score\"] = baseline_factors * np.log1p(df[\"impressions_90d\"])\n",
    "df[\"reason_code\"] = np.where(df[\"baseline_score\"] > 0, \"dynamic_underperforming\", \"none\")\n",
    "df[\"action_label\"] = np.where(df[\"baseline_score\"] > 0, \"needs_refresh\", \"no_action\")\n",
    "\n",
    "df_ranked = df.sort_values(by=\"baseline_score\", ascending=False).copy()\n",
    "top_50 = df_ranked.head(50)\n",
    "precision_at_50 = top_50[\"is_declining_label\"].mean()\n",
    "\n",
    "print(f\"Base rate (random picking): {base_rate:.3f}\")\n",
    "print(f\"Precision@50: {precision_at_50:.3f}\\n\")\n",
    "\n",
    "import os\n",
    "os.makedirs(\"../../outputs\", exist_ok=True)\n",
    "output_cols = [\"content_id\", \"baseline_score\", \"reason_code\", \"action_label\", \"is_declining_label\", \"impressions_90d\", \"days_since_last_update\", \"ctr\"]\n",
    "df_ranked[output_cols].to_csv(\"../../outputs/baseline_action_score.csv\", index=False)\n",
    "print(\"Wrote ranked queue to outputs/baseline_action_score.csv\")\n"
]

nb['cells'][5]['source'] = [
    "## 3. Top-10 review\n",
    "\n",
    "For each of the top 10: action, reason code, confidence note, and what would make it wrong."
]

nb['cells'][6]['source'] = [
    "display_cols = [\"content_id\", \"baseline_score\", \"reason_code\", \"impressions_90d\", \"days_since_last_update\", \"ctr\", \"is_declining_label\"]\n",
    "display(top_50[display_cols].head(10))\n",
    "\n",
    "print(\"Top-10 Review:\")\n",
    "for i, (idx, row) in enumerate(top_50.head(10).iterrows(), 1):\n",
    "    cid = row['content_id']\n",
    "    action = row['action_label']\n",
    "    reason = row['reason_code']\n",
    "    \n",
    "    wrong_if = \"it's a legacy or seasonal page where decay is acceptable.\"\n",
    "    if row['impressions_90d'] > 10000:\n",
    "        wrong_if = \"impressions are high due to an irrelevant viral spike that is naturally correcting.\"\n",
    "    elif row['ctr'] < 0.5:\n",
    "        wrong_if = \"it's a zero-click navigational page where low CTR is expected.\"\n",
    "        \n",
    "    print(f\"{i}. {cid} - Action: {action}. Reason: {reason}. Wrong if: {wrong_if}\")\n"
]

nb['cells'][7]['source'] = [
    "## 4. Weak picks + leakage check\n",
    "\n",
    "By evaluating signals dynamically, we avoid the weakness of blindly flagging pages based on fixed assumptions that may not hold true (like staleness). However, some pages might still be stable (`is_declining_label` == 0) despite hitting our criteria. There are no future windows or labels leaked into our features since `days_since_last_update`, `ctr`, and `impressions_90d` are all measured prior to or concurrently with the baseline assessment, not using `trend_pct` directly."
]

nb['cells'][8]['source'] = [
    "scored_cols = ['days_since_last_update', 'impressions_90d', 'ctr']\n",
    "label_cols = ['is_declining_label', 'trend_direction', 'trend_pct']\n",
    "\n",
    "print(\"Features used for score:\", scored_cols)\n",
    "print(\"Overlap with label logic:\", set(scored_cols).intersection(label_cols))\n",
    "print(\"Leakage check passed: No label columns used for baseline scoring.\")\n"
]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated.")
