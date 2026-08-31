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
headshot_b64 = get_base64(os.path.join(work_dir, "assets", "profile_headshot.png"))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Image Curation Deliverable - Abdullah Naeem</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  
  @page {{
    size: A4;
    margin: 12mm 15mm 12mm 15mm;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Inter', Arial, sans-serif;
    color: #111827;
    background: #FFFFFF;
    line-height: 1.5;
    font-size: 10.5pt;
  }}

  .header {{
    border-bottom: 2px solid #111827;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }}

  h1 {{
    font-size: 18pt;
    font-weight: 700;
    color: #111827;
    margin-bottom: 2px;
  }}

  .subtitle {{
    font-size: 10pt;
    color: #4B5563;
  }}

  h2 {{
    font-size: 12pt;
    font-weight: 700;
    color: #111827;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 4px;
    margin-top: 16px;
    margin-bottom: 10px;
  }}

  p {{
    margin-bottom: 8px;
    color: #374151;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 14px;
    font-size: 9.5pt;
  }}

  th {{
    background: #F3F4F6;
    color: #111827;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #D1D5DB;
    font-weight: 600;
  }}

  td {{
    padding: 6px 8px;
    border: 1px solid #E5E7EB;
    vertical-align: top;
  }}

  .choice-block {{
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 10px;
  }}

  .choice-title {{
    font-weight: 700;
    color: #111827;
    margin-bottom: 2px;
  }}

  .rejection-block {{
    background: #FFF5F5;
    border: 1px solid #FEB2B2;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 10px;
  }}

  .rejection-title {{
    font-weight: 700;
    color: #9B2C2C;
    margin-bottom: 2px;
  }}

  .img-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-top: 10px;
    margin-bottom: 14px;
  }}

  .img-item {{
    border: 1px solid #E5E7EB;
    padding: 6px;
    background: #FAFAFA;
    border-radius: 4px;
    text-align: center;
  }}

  .img-item img {{
    max-width: 100%;
    height: 100px;
    object-fit: contain;
    margin-bottom: 4px;
  }}

  .img-label {{
    font-size: 8.5pt;
    font-weight: 600;
    color: #374151;
  }}

  footer {{
    margin-top: 20px;
    border-top: 1px solid #E5E7EB;
    padding-top: 8px;
    font-size: 8.5pt;
    color: #6B7280;
    text-align: center;
  }}
</style>
</head>
<body>

  <div class="header">
    <h1>Image Curation & Visual Discernment Log</h1>
    <div class="subtitle">Abdullah Naeem &bull; FlyRank AI Track Thread Deliverable</div>
  </div>

  <h2>1. The Final Image Set (The Keepers)</h2>
  <table>
    <thead>
      <tr>
        <th>Image Asset</th>
        <th>Placement</th>
        <th>Asset Type</th>
        <th>Purpose & Placement</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Author Headshot</strong></td>
        <td>About Me & Hero</td>
        <td>Real Photograph</td>
        <td>Authentic headshot (<code>portrait.png</code>) establishing identity & trust.</td>
      </tr>
      <tr>
        <td><strong>Sitemap Sketch</strong></td>
        <td>Home & Architecture</td>
        <td>Real Capture</td>
        <td>Hand-drawn user journey sketch (<code>sitemap_sketch.png</code>).</td>
      </tr>
      <tr>
        <td><strong>Claude Project Setup</strong></td>
        <td>About & Workflow</td>
        <td>Real Screenshot</td>
        <td>Unedited screenshot (<code>claude_portfolio_project.png</code>) of tutor prompt setup.</td>
      </tr>
      <tr>
        <td><strong>Pressure Test Output</strong></td>
        <td>About & Workflow</td>
        <td>Real Screenshot</td>
        <td>Real capture (<code>pressure_test_output.png</code>) showing sitemap feedback.</td>
      </tr>
      <tr>
        <td><strong>Monogram Favicon</strong></td>
        <td>Browser Tab</td>
        <td>SVG Brand Asset</td>
        <td>Clean <code>AN.</code> monogram icon (<code>favicon.svg</code>).</td>
      </tr>
      <tr>
        <td><strong>Header Brand Logo</strong></td>
        <td>Navigation Bar</td>
        <td>SVG Brand Asset</td>
        <td>Primary header logo (<code>logo.svg</code>).</td>
      </tr>
    </tbody>
  </table>

  <h2>Visual Keeper Assets</h2>
  <div class="img-grid">
    <div class="img-item">
      <img src="{headshot_b64}" alt="Author Profile">
      <div class="img-label">Author Headshot (Real Photo)</div>
    </div>
    <div class="img-item">
      <img src="{favicon_b64}" alt="Favicon Monogram">
      <div class="img-label">Monogram Favicon (favicon.svg)</div>
    </div>
    <div class="img-item">
      <img src="{logo_b64}" alt="Header Logo">
      <div class="img-label">Header Brand Logo (logo.svg)</div>
    </div>
    <div class="img-item">
      <img src="{sitemap_b64}" alt="Sitemap Sketch">
      <div class="img-label">Sitemap Sketch (Real Capture)</div>
    </div>
    <div class="img-item">
      <img src="{claude_proj_b64}" alt="Claude Setup">
      <div class="img-label">Claude Setup (Real Screenshot)</div>
    </div>
    <div class="img-item">
      <img src="{pressure_b64}" alt="Pressure Test">
      <div class="img-label">Pressure Test Output (Real Screenshot)</div>
    </div>
  </div>

  <h2>2. Where Real Captures Were Chosen Over AI</h2>

  <div class="choice-block">
    <div class="choice-title">Work & Code = 100% Real Captures</div>
    <p>Screenshots of notebooks (<code>w03_data_contract.ipynb</code>), sitemaps, and terminal outputs are strictly real unedited captures. Synthetic AI code mockups look fake under inspection and destroy technical credibility with senior engineering managers.</p>
  </div>

  <div class="choice-block">
    <div class="choice-title">Personal Identity = Real Photograph Only</div>
    <p>A real professional headshot (<code>portrait.png</code>) is used for the author. AI avatars or stylized digital portraits create friction and reduce trust when hiring managers evaluate candidate authenticity.</p>
  </div>

  <div class="choice-block">
    <div class="choice-title">Connective Tissue = Strictly Styled Brand Assets</div>
    <p>Visuals are restricted exclusively to minimal design system tokens matching our 4-color palette (<code>#F8FAFC</code>, <code>#0F172A</code>, <code>#1E293B</code>, <code>#2563EB</code>). This keeps the interface visual frame quiet so real code remains the hero.</p>
  </div>

  <h2>3. Rejection Log (Discernment & Judgment)</h2>

  <div class="rejection-block">
    <div class="rejection-title">Rejected Image 1: Glowing 3D Cybernetic Neural Network Hero Graphic</div>
    <p><strong>Why it was rejected:</strong> While visually striking, it felt like generic AI stock art that competed with the actual work. It violated our calm slate identity kit (<code>#F8FAFC</code> / <code>#1E293B</code>) and gave the portfolio a hype-driven aesthetic rather than a disciplined engineering tone. Replaced with real code receipts and metric indicators.</p>
  </div>

  <div class="rejection-block">
    <div class="rejection-title">Rejected Image 2: Stylized Isometric Vector Illustration of a Developer</div>
    <p><strong>Why it was rejected:</strong> Generic vector illustrations fail to build personal trust with Senior ML Managers and create distance between the reader and the engineer. An authentic, unedited photograph was chosen instead.</p>
  </div>

  <div class="rejection-block">
    <div class="rejection-title">Rejected Image 3: Synthetic Code Mockup Hero Card</div>
    <p><strong>Why it was rejected:</strong> Synthetic code mockups look fake under inspection. Real executed Jupyter Notebook cells (<code>w03_data_contract.ipynb</code>) and DuckDB query outputs provide authentic, verifiable proof without superficial visual fluff.</p>
  </div>

  <footer>
    Abdullah Naeem &bull; Machine Learning Engineer &bull; FlyRank AI Track Thread Submission PDF
  </footer>

</body>
</html>
"""

pdf_output_path = os.path.join(work_dir, "fl01_image_curation.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content)
    page.pdf(path=pdf_output_path, format="A4", print_background=True)
    browser.close()

print("PDF with Monogram & Logo grid generated successfully at:", pdf_output_path)
