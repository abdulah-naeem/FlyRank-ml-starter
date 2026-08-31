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
favicon_b64 = get_base64(os.path.join(work_dir, "favicon.svg"))
specimen_b64 = get_base64(os.path.join(work_dir, "identity_kit_specimen.png"))
sitemap_b64 = get_base64(os.path.join(work_dir, "sitemap_sketch.png"))
claude_proj_b64 = get_base64(os.path.join(work_dir, "claude_portfolio_project.png"))
pressure_b64 = get_base64(os.path.join(work_dir, "pressure_test_output.png"))
workflow_b64 = get_base64(os.path.join(work_dir, "claude_project_screenshot.png"))

complete_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>FL-01 Complete Submission - Abdullah Naeem</title>
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
    margin-bottom: 24px;
  }}

  .doc-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #0F172A;
  }}

  .doc-badge {{
    background-color: #1E293B;
    color: #F8FAFC;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
  }}

  .section-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    page-break-inside: avoid;
  }}

  .section-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: #1E293B;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #F1F5F9;
    padding-bottom: 8px;
  }}

  .section-title::before {{
    content: '';
    display: inline-block;
    width: 8px;
    height: 20px;
    background-color: #2563EB;
    border-radius: 4px;
  }}

  .quote-box {{
    background: #F0F9FF;
    border-left: 4px solid #2563EB;
    padding: 14px 18px;
    border-radius: 0 8px 8px 0;
    font-size: 14px;
    margin-bottom: 12px;
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
  }}

  .table-custom td {{
    padding: 8px 10px;
    border-bottom: 1px solid #E2E8F0;
  }}

  .palette-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }}

  .color-swatch {{
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #E2E8F0;
    text-align: center;
  }}

  .swatch-color {{
    height: 36px;
    border-radius: 6px;
    margin-bottom: 6px;
    border: 1px solid rgba(0,0,0,0.08);
  }}

  .img-preview {{
    width: 100%;
    border-radius: 8px;
    border: 1px solid #E2E8F0;
    margin-top: 10px;
  }}

  footer {{
    text-align: center;
    margin-top: 24px;
    padding-top: 12px;
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
      <img src="{logo_b64}" style="height: 48px;" alt="Logo">
    </div>
    <div>
      <span class="doc-badge">FL-01 FULL SUBMISSION</span>
    </div>
  </header>

  <!-- Part 1: Proof Statement -->
  <div class="section-card">
    <div class="section-title">Module 1: Proof Statement & Core Action</div>
    <div class="quote-box">
      <strong>The One-Paragraph Proof Statement:</strong><br>
      "I build and debug practical machine learning models that solve concrete business problems, proving my ability to go beyond academic theory into real-world application. This portfolio is built specifically for Senior Data Scientists and ML Engineering Managers who are looking to hire technically fluent interns capable of adding immediate value to their pipelines. My goal is for you to review my case studies, recognize my foundational ML skills, and email me to schedule a technical interview."
    </div>
    <div class="quote-box" style="border-left-color: #1E293B; background: #F8FAFC;">
      <strong>The One-Line "Why":</strong><br>
      "A standard resume can list the Python libraries I know, but only a portfolio can prove that my code is clean, mathematically sound, and capable of solving actual business logic without data leakage."
    </div>
  </div>

  <!-- Part 2: Portfolio Sitemap -->
  <div class="section-card">
    <div class="section-title">Module 2: Portfolio Sitemap & Claude Setup</div>
    <p style="font-size: 13px; margin-bottom: 8px;"><strong>My One Action:</strong> Contact me to schedule an interview for an ML Engineer position.</p>
    <p style="font-size: 13px; margin-bottom: 12px;"><strong>Streamlined 3-Page Structure:</strong> Home / Hero (Proof + CTA), Work / Case Studies (Deep-dives), About Me (Background & Trust).</p>
    <img src="{sitemap_b64}" class="img-preview" alt="Sitemap Sketch">
  </div>

  <!-- Part 3: Identity Kit -->
  <div class="section-card">
    <div class="section-title">Module 3: Identity Kit & Design System</div>
    <div class="palette-grid" style="margin-bottom: 14px;">
      <div class="color-swatch"><div class="swatch-color" style="background:#F8FAFC;"></div><div style="font-size:11px;font-weight:600;">Background</div><div style="font-size:10px;color:#64748B;">#F8FAFC</div></div>
      <div class="color-swatch"><div class="swatch-color" style="background:#0F172A;"></div><div style="font-size:11px;font-weight:600;">Text</div><div style="font-size:10px;color:#64748B;">#0F172A</div></div>
      <div class="color-swatch"><div class="swatch-color" style="background:#1E293B;"></div><div style="font-size:11px;font-weight:600;">Main</div><div style="font-size:10px;color:#64748B;">#1E293B</div></div>
      <div class="color-swatch"><div class="swatch-color" style="background:#2563EB;"></div><div style="font-size:11px;font-weight:600;">Accent</div><div style="font-size:10px;color:#64748B;">#2563EB</div></div>
    </div>
    <div style="font-size: 13px; background: #F8FAFC; padding: 10px; border-radius: 6px; border: 1px solid #E2E8F0; margin-bottom: 12px;">
      <strong>Fonts:</strong> Headings set in <em>Plus Jakarta Sans</em> | Body & Code set in <em>Inter</em><br>
      <strong>2-Line Style Note:</strong> Style Guide: Fonts: Plus Jakarta Sans (Headings), Inter (Body). Palette: #F8FAFC (Bg), #0F172A (Text), #1E293B (Primary), #2563EB (Accent).<br>
      Mood: Minimal, high-precision ML engineering notebook — calm slate & sapphire framing clean code.
    </div>
    <img src="{specimen_b64}" class="img-preview" alt="Identity Kit Specimen">
  </div>

  <!-- Part 4: Workflow Audit -->
  <div class="section-card">
    <div class="section-title">Module 4: Workflow Audit (Recurring Tasks)</div>
    <table class="table-custom">
      <thead>
        <tr><th>Task</th><th>Classification</th><th>Rationale</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. Reading ML research papers</strong></td><td>Just me</td><td>Need personal deep absorption of math & intuition.</td></tr>
        <tr><td><strong>2. Debugging model errors</strong></td><td>Collaborate with AI</td><td>Bouncing stack traces & hypotheses speeds debugging.</td></tr>
        <tr><td><strong>3. Boilerplate data cleaning</strong></td><td>Delegate to AI</td><td>Fast regex & pandas fillna generation with manual review.</td></tr>
        <tr><td><strong>4. Environment setup</strong></td><td>Fully Automate</td><td>Bash scripts handle virtualenv setup automatically.</td></tr>
      </tbody>
    </table>
  </div>

  <footer>
    Abdullah Naeem &bull; Machine Learning Engineer &bull; FlyRank AI Track Thread Submission PDF
  </footer>
</div>
</body>
</html>
"""

pdf_output_path = os.path.join(work_dir, "fl01_complete_submission.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(complete_html)
    page.pdf(path=pdf_output_path, format="A4", print_background=True)
    browser.close()

print("Complete PDF generated successfully at:", pdf_output_path)
