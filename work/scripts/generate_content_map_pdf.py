import os
import base64
from playwright.sync_api import sync_playwright

work_dir = os.path.dirname(os.path.abspath(__file__))

def get_base64(filepath):
    if not os.path.exists(filepath):
        return ""
    ext = os.path.splitext(filepath)[1].lower()
    mime = "image/png"
    if ext == ".svg":
        mime = "image/svg+xml"
    elif ext in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    with open(filepath, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

logo_b64 = get_base64(os.path.join(work_dir, "logo.svg"))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>FL-01 Content Map & Through-Line - Abdullah Naeem</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
  
  @page {{
    size: A4;
    margin: 15mm 15mm 15mm 15mm;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #F8FAFC;
    color: #0F172A;
    line-height: 1.5;
    padding: 24px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .container {{
    max-width: 800px;
    margin: 0 auto;
  }}

  header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 16px;
    margin-bottom: 20px;
  }}

  .doc-badge {{
    background-color: #1E293B;
    color: #F8FAFC;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
  }}

  .banner {{
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    color: #F8FAFC;
    padding: 18px 20px;
    border-radius: 12px;
    margin-bottom: 20px;
  }}

  .banner h2 {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18px;
    color: #2563EB;
    margin-bottom: 4px;
  }}

  .banner p {{
    font-size: 13px;
    opacity: 0.9;
  }}

  .section-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    page-break-inside: avoid;
  }}

  .section-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: #1E293B;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .section-title::before {{
    content: '';
    display: inline-block;
    width: 8px;
    height: 18px;
    background-color: #2563EB;
    border-radius: 4px;
  }}

  .claim-box {{
    background-color: #F0F9FF;
    border-left: 4px solid #2563EB;
    padding: 14px 16px;
    border-radius: 0 8px 8px 0;
    font-size: 14px;
    font-weight: 600;
    color: #0F172A;
  }}

  .table-custom {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    font-size: 12px;
  }}

  .table-custom th {{
    background: #1E293B;
    color: #F8FAFC;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
  }}

  .table-custom td {{
    padding: 8px 10px;
    border-bottom: 1px solid #E2E8F0;
  }}

  .checklist {{
    list-style: none;
  }}

  .checklist li {{
    font-size: 13px;
    padding: 5px 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .check-icon {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 18px;
    height: 18px;
    background-color: #2563EB;
    color: #FFFFFF;
    border-radius: 50%;
    font-size: 11px;
    font-weight: bold;
  }}

  footer {{
    text-align: center;
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #E2E8F0;
    font-size: 11px;
    color: #64748B;
  }}
</style>
</head>
<body>
<div class="container">
  <header>
    <div>
      <img src="{logo_b64}" style="height: 44px;" alt="Logo">
    </div>
    <div>
      <span class="doc-badge">FL-01 CONTENT MAP</span>
    </div>
  </header>

  <div class="banner">
    <h2>The Through-Line: Content Map & Evidence Inventory</h2>
    <p>Connecting the one-line claim to an ordered content hierarchy where every call to action ladders up to scheduling a technical interview.</p>
  </div>

  <div class="section-card">
    <div class="section-title">1. The One-Line Claim</div>
    <div class="claim-box">
      "I build mathematically sound, leakage-free machine learning models that solve concrete business problems and deliver production-ready pipelines."
    </div>
  </div>

  <div class="section-card">
    <div class="section-title">2. Content Map (Pages → Ordered Sections → CTAs)</div>
    
    <p style="font-size: 13px; font-weight: 700; color: #1E293B; margin-top: 8px;">Page 1: Home / Hero View (<code>/index.html</code>)</p>
    <table class="table-custom">
      <thead>
        <tr><th>Section</th><th>Content / Case</th><th>Call to Action (CTA)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. Hero</strong></td><td>One-Line Claim & Monogram</td><td><code>"Schedule a Technical Interview"</code></td></tr>
        <tr><td><strong>2. Receipts</strong></td><td>3 Key Metric Indicators</td><td>N/A (Trust anchor)</td></tr>
        <tr><td><strong>3. Lead Work</strong></td><td><strong>Case 1 (Lead):</strong> FlyRank SEO Engine</td><td><code>"Read Full FlyRank Deep-Dive →"</code></td></tr>
        <tr><td><strong>4. Secondary</strong></td><td><strong>Case 2:</strong> Leakage Prevention Framework</td><td><code>"View Leakage Prevention Audit →"</code></td></tr>
        <tr><td><strong>5. Footer CTA</strong></td><td>Conversion Banner</td><td><strong>The One Action:</strong> <code>"Schedule a Technical Interview"</code></td></tr>
      </tbody>
    </table>

    <p style="font-size: 13px; font-weight: 700; color: #1E293B; margin-top: 14px;">Page 2: Case Studies Deep-Dive (<code>/case-studies/flyrank-seo.html</code>)</p>
    <table class="table-custom">
      <thead>
        <tr><th>Section</th><th>Content / Case</th><th>Call to Action (CTA)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. TL;DR Header</strong></td><td>Core business objective & metric lift</td><td><code>"View Live Paper Deployment"</code></td></tr>
        <tr><td><strong>2. Data Contract</strong></td><td>Temporal split & non-null rules</td><td><code>"Inspect Code on GitHub"</code></td></tr>
        <tr><td><strong>3. Benchmark</strong></td><td>Baseline vs LightGBM/XGBoost</td><td>N/A</td></tr>
        <tr><td><strong>4. Case Footer</strong></td><td>Engineering readiness summary</td><td><strong>The One Action:</strong> <code>"Schedule a Technical Interview"</code></td></tr>
      </tbody>
    </table>

    <p style="font-size: 13px; font-weight: 700; color: #1E293B; margin-top: 14px;">Page 3: About & Engineering Principles (<code>/about.html</code>)</p>
    <table class="table-custom">
      <thead>
        <tr><th>Section</th><th>Content / Case</th><th>Call to Action (CTA)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. Bio Header</strong></td><td>Applied ML & clean code philosophy</td><td>N/A</td></tr>
        <tr><td><strong>2. Workflow</strong></td><td>FL-01 15-Task Classification Table</td><td><code>"View Full Workflow Audit"</code></td></tr>
        <tr><td><strong>3. Principles</strong></td><td>3 Rules (Zero leakage, baselines, reproducibility)</td><td>N/A</td></tr>
        <tr><td><strong>4. Footer CTA</strong></td><td>Conversion Banner</td><td><strong>The One Action:</strong> <code>"Schedule a Technical Interview"</code></td></tr>
      </tbody>
    </table>
  </div>

  <div class="section-card">
    <div class="section-title">3. The "Still Need to Gather" List</div>
    <table class="table-custom">
      <thead>
        <tr><th>Evidence Asset</th><th>Type</th><th>Milestone</th><th>Plan</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. Deployed Paper URL</strong></td><td>Live Link</td><td>Week 7 (ML-11)</td><td>Deploy static HTML paper on Vercel/GitHub Pages.</td></tr>
        <tr><td><strong>2. Baseline vs Model Metrics</strong></td><td>Metrics JSON</td><td>Week 5 (ML-08)</td><td>Export LogLoss, ROC-AUC, Rank-IC JSONs.</td></tr>
        <tr><td><strong>3. Architecture Diagram</strong></td><td>PNG/SVG Visual</td><td>Week 4 (ML-06)</td><td>Generate diagram of temporal split pipeline.</td></tr>
        <tr><td><strong>4. GitHub Repo Clean Link</strong></td><td>Repository Link</td><td>Week 7 (ML-12)</td><td>Polish README & reproducibility guidelines.</td></tr>
        <tr><td><strong>5. Manager Testimonial</strong></td><td>Text Quote</td><td>Week 6</td><td>Obtain 2-sentence endorsement quote.</td></tr>
        <tr><td><strong>6. 5-Min Video Demo</strong></td><td>Screen Recording</td><td>Week 7 (ML-12)</td><td>Record brief walkthrough of model playbook.</td></tr>
      </tbody>
    </table>
  </div>

  <div class="section-card">
    <div class="section-title">4. Pass / Revise Checklist</div>
    <ul class="checklist">
      <li><span class="check-icon">✓</span> <strong>Single, memorable claim:</strong> One sentence claim locked in.</li>
      <li><span class="check-icon">✓</span> <strong>Ordered sections & CTAs:</strong> Every page mapped sequentially with flagship case leading.</li>
      <li><span class="check-icon">✓</span> <strong>CTAs ladder to The One Action:</strong> All pages drive visitors to schedule a technical interview.</li>
      <li><span class="check-icon">✓</span> <strong>Honest gather-list:</strong> 6 required assets cataloged by target milestone.</li>
    </ul>
  </div>

  <footer>
    Abdullah Naeem &bull; Machine Learning Engineer &bull; FlyRank AI Track Thread Submission PDF
  </footer>
</div>
</body>
</html>
"""

pdf_output_path = os.path.join(work_dir, "fl01_content_map.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content)
    page.pdf(path=pdf_output_path, format="A4", print_background=True)
    browser.close()

print("Content Map PDF generated successfully at:", pdf_output_path)
