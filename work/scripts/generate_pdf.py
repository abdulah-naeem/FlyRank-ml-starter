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

favicon_b64 = get_base64(os.path.join(work_dir, "favicon.svg"))
logo_b64 = get_base64(os.path.join(work_dir, "logo.svg"))
specimen_b64 = get_base64(os.path.join(work_dir, "identity_kit_specimen.png"))
sitemap_b64 = get_base64(os.path.join(work_dir, "sitemap_sketch.png"))
claude_proj_b64 = get_base64(os.path.join(work_dir, "claude_portfolio_project.png"))
pressure_b64 = get_base64(os.path.join(work_dir, "pressure_test_output.png"))
workflow_b64 = get_base64(os.path.join(work_dir, "claude_project_screenshot.png"))

identity_kit_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Identity Kit Deliverable - Abdullah Naeem</title>
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

  .header-brand {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  .header-brand img {{
    height: 48px;
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
    letter-spacing: 0.5px;
  }}

  .banner {{
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    color: #F8FAFC;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 24px;
  }}

  .banner h2 {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18px;
    margin-bottom: 6px;
    color: #2563EB;
  }}

  .banner p {{
    font-size: 14px;
    opacity: 0.9;
  }}

  .section-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}

  .section-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 14px;
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

  /* Palette Grid */
  .palette-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }}

  .color-swatch {{
    border-radius: 8px;
    padding: 12px;
    border: 1px solid #E2E8F0;
    text-align: center;
  }}

  .swatch-color {{
    height: 44px;
    border-radius: 6px;
    margin-bottom: 8px;
    border: 1px solid rgba(0,0,0,0.08);
  }}

  .swatch-name {{
    font-size: 12px;
    font-weight: 600;
    color: #0F172A;
  }}

  .swatch-hex {{
    font-family: monospace;
    font-size: 11px;
    color: #64748B;
  }}

  /* Typography Grid */
  .typo-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }}

  .typo-box {{
    background: #F8FAFC;
    padding: 14px;
    border-radius: 8px;
    border: 1px solid #E2E8F0;
  }}

  .typo-role {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748B;
    font-weight: 700;
    margin-bottom: 4px;
  }}

  .typo-name {{
    font-size: 18px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 4px;
  }}

  .typo-sample {{
    font-size: 13px;
    color: #334155;
  }}

  /* Style Note Box */
  .style-note {{
    background-color: #F0F9FF;
    border-left: 4px solid #2563EB;
    padding: 14px 18px;
    border-radius: 0 8px 8px 0;
    font-size: 13px;
    color: #0F172A;
  }}

  .style-note strong {{
    color: #1E293B;
  }}

  .specimen-img {{
    width: 100%;
    border-radius: 8px;
    border: 1px solid #E2E8F0;
    margin-top: 12px;
  }}

  /* Checklist */
  .checklist {{
    list-style: none;
  }}

  .checklist li {{
    font-size: 13px;
    padding: 6px 0;
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
    <div class="header-brand">
      <img src="{logo_b64}" alt="Logo">
    </div>
    <div>
      <span class="doc-badge">FL-01 DELIVERABLE</span>
    </div>
  </header>

  <div class="banner">
    <h2>Identity Kit & Visual Design System</h2>
    <p>A consistent look is what separates a portfolio that feels intentional from one that feels thrown together. Make them once and every page inherits them.</p>
  </div>

  <div class="section-card">
    <div class="section-title">1. Color Palette (Tight 4-Color Tokens)</div>
    <div class="palette-grid">
      <div class="color-swatch">
        <div class="swatch-color" style="background-color: #F8FAFC;"></div>
        <div class="swatch-name">Background</div>
        <div class="swatch-hex">#F8FAFC</div>
      </div>
      <div class="color-swatch">
        <div class="swatch-color" style="background-color: #0F172A;"></div>
        <div class="swatch-name" style="color: #0F172A;">Near-Black Text</div>
        <div class="swatch-hex">#0F172A</div>
      </div>
      <div class="color-swatch">
        <div class="swatch-color" style="background-color: #1E293B;"></div>
        <div class="swatch-name">Deep Slate Main</div>
        <div class="swatch-hex">#1E293B</div>
      </div>
      <div class="color-swatch">
        <div class="swatch-color" style="background-color: #2563EB;"></div>
        <div class="swatch-name" style="color: #2563EB;">Sapphire Accent</div>
        <div class="swatch-hex">#2563EB</div>
      </div>
    </div>
  </div>

  <div class="section-card">
    <div class="section-title">2. Typography Pairings</div>
    <div class="typo-grid">
      <div class="typo-box">
        <div class="typo-role">Heading Font</div>
        <div class="typo-name" style="font-family: 'Plus Jakarta Sans', sans-serif;">Plus Jakarta Sans</div>
        <div class="typo-sample" style="font-family: 'Plus Jakarta Sans', sans-serif;">Build & Debug Applied Machine Learning Models</div>
      </div>
      <div class="typo-box">
        <div class="typo-role">Body & Code Font</div>
        <div class="typo-name" style="font-family: 'Inter', sans-serif;">Inter</div>
        <div class="typo-sample" style="font-family: 'Inter', sans-serif;">Clean code, data contracts, mathematical proofs, and validation metrics.</div>
      </div>
    </div>
  </div>

  <div class="section-card">
    <div class="section-title">3. Two-Line Style Note (for Claude Project)</div>
    <div class="style-note">
      <p><strong>Style Guide:</strong> Fonts: Plus Jakarta Sans (Headings), Inter (Body). Palette: #F8FAFC (Bg), #0F172A (Text), #1E293B (Primary), #2563EB (Accent).</p>
      <p style="margin-top: 6px;"><strong>Mood:</strong> Minimal, high-precision ML engineering notebook — calm slate & sapphire framing clean code, data contracts, and validation metrics without visual clutter.</p>
    </div>
  </div>

  <div class="section-card">
    <div class="section-title">4. Visual Specimen & Logo Mark</div>
    <div style="display: flex; gap: 16px; align-items: center; margin-bottom: 12px;">
      <div>
        <p style="font-size: 12px; font-weight: 600; color: #64748B; margin-bottom: 4px;">FAVICON MONOGRAM (512x512)</p>
        <img src="{favicon_b64}" style="width: 64px; height: 64px; border-radius: 12px;">
      </div>
      <div>
        <p style="font-size: 12px; font-weight: 600; color: #64748B; margin-bottom: 4px;">HEADER BRAND MARK</p>
        <img src="{logo_b64}" style="height: 48px;">
      </div>
    </div>
    <img src="{specimen_b64}" class="specimen-img" alt="Visual Specimen">
  </div>

  <div class="section-card">
    <div class="section-title">5. Pass / Revise Checklist</div>
    <ul class="checklist">
      <li><span class="check-icon">✓</span> <strong>One or two fonts, not a pile:</strong> Exactly 2 fonts (Plus Jakarta Sans + Inter).</li>
      <li><span class="check-icon">✓</span> <strong>Tight palette with actual hex codes:</strong> 4 distinct hex codes (#F8FAFC, #0F172A, #1E293B, #2563EB).</li>
      <li><span class="check-icon">✓</span> <strong>Simple logo / favicon exists:</strong> SVG monogram and header logo designed and exported.</li>
      <li><span class="check-icon">✓</span> <strong>Style note describes a single, coherent mood:</strong> Two-line prompt locked into Claude Project settings.</li>
    </ul>
  </div>

  <footer>
    Abdullah Naeem &bull; Machine Learning Engineering Portfolio &bull; FlyRank AI Track Thread Deliverable
  </footer>
</div>
</body>
</html>
"""

pdf_output_path = os.path.join(work_dir, "fl01_identity_kit.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(identity_kit_html)
    page.pdf(path=pdf_output_path, format="A4", print_background=True)
    browser.close()

print("PDF generated successfully at:", pdf_output_path)
