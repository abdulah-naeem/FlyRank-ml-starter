# Vercel Deployment Guide ("Empty but Live" Milestone)

This guide walks you through deploying your portfolio to **Vercel's global edge network** for free in under two minutes.

---

### Method: Deploy via GitHub on Vercel (Recommended & Auto-Updating)

Since your project already lives in GitHub at `abdulah-naeem/FlyRank-ml-starter`, connecting it to Vercel means any future edits in `work/portfolio` will automatically redeploy!

#### Step 1: Open Vercel
1. Go to **[vercel.com/new](https://vercel.com/new)**.
2. Sign in with your **GitHub** account (free Hobby plan).

---

#### Step 2: Import Repository
1. Under **"Import Git Repository"**, find:
   ```
   abdulah-naeem/FlyRank-ml-starter
   ```
   *(If you don't see it immediately, click "Adjust GitHub App Permissions" and allow access to this repo).*
2. Click **Import**.

---

#### Step 3: Configure Root Directory (Crucial Step!)
Because your portfolio lives inside the `work/portfolio` folder of the repo, configure this setting before clicking deploy:

1. Look for **Root Directory**.
2. Click the **Edit** button next to `./`.
3. Select or enter:
   ```
   work/portfolio
   ```
4. Click **Continue**.
5. Ensure **Framework Preset** is set to:
   ```
   Other
   ```
6. Set **Project Name** to:
   ```
   abdullah-naeem-ml
   ```
   *(This gives you the clean URL `https://abdullah-naeem-ml.vercel.app`).*

---

#### Step 4: Click Deploy!
1. Hit **Deploy**.
2. In ~15 seconds, your site is live globally on Vercel's edge network!
3. Your public live URL will be:
   👉 **`https://abdullah-naeem-ml.vercel.app`**

---

### Step 5: Verify on a Second Device (Your Phone)
1. Open the URL on your mobile browser:
   `https://abdullah-naeem-ml.vercel.app`
2. Confirm the page loads cleanly, showing:
   - Official monogram logo `AN.`
   - "Machine Learning Engineer"
   - Green pulsing status dot: `● Empty but Live · Week 4 Milestone`
   - Your One-Line Claim & Week 5 Roadmap
3. Take a screenshot on your phone to submit as proof of second-device verification.

---

### Step 6: Claude Project Custom Instructions
In your Claude Project, ensure your **Custom Instructions** are set:
```text
Style Guide: Fonts: Plus Jakarta Sans (Headings), Inter (Body). Palette: #F8FAFC (Bg), #0F172A (Text), #1E293B (Primary), #2563EB (Accent).
Mood: Minimal, high-precision ML engineering notebook — calm slate & sapphire framing clean code, data contracts, and validation metrics without visual clutter.
Target Audience: Senior Data Scientists & ML Engineering Managers hiring technically fluent interns.
Core Claim: "I build mathematically sound, leakage-free machine learning models that solve concrete business problems and deliver production-ready pipelines."
The One Action: Direct conversion to schedule a technical interview.
```
