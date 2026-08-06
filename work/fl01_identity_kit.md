# Portfolio Identity Kit & Design System

> **Why it matters:** A consistent look is what separates a portfolio that feels intentional from one that feels thrown together. Make these decisions once, and every page, component, and case study inherits them cleanly.

![Identity Kit Specimen](./identity_kit_specimen.png)

---

## 1. Typography Selection

* **Heading Font:** **Plus Jakarta Sans** (Google Font — Clean, modern geometric sans-serif with high precision and structural weight for headers & titles).
* **Body & Code Font:** **Inter** (Google Font — Industrial-grade readability for dense technical writeups, equations, and code callouts).

```css
/* Typography Declaration */
:root {
  --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}

h1, h2, h3, h4 {
  font-family: var(--font-heading);
  letter-spacing: -0.025em;
}

body, p, li {
  font-family: var(--font-body);
  line-height: 1.6;
}
```

---

## 2. Color Palette (Tight 4-Color Palette)

| Role | Color Name | Hex Code | Purpose & Usage |
| :--- | :--- | :--- | :--- |
| **Near-White Background** | Slate 50 | `#F8FAFC` | Main viewport & canvas background (soft, low eye fatigue). |
| **Near-Black Text** | Slate 900 | `#0F172A` | Primary typography & headers (sharp contrast without harsh `#000000`). |
| **Main / Structural Color** | Deep Slate | `#1E293B` | Navigation bars, primary buttons, card borders & monogram container. |
| **Single Accent Color** | Sapphire Blue | `#2563EB` | Interactive hover states, active links, metric highlights & focus indicators. |

### Visual Palette Tokens

```css
/* Color System Variables */
:root {
  --bg-primary: #F8FAFC;      /* Near-white background */
  --text-primary: #0F172A;    /* Near-black high-contrast text */
  --brand-primary: #1E293B;   /* Deep slate structural elements */
  --accent-color: #2563EB;    /* Sapphire blue interactive accent */
  --border-muted: #E2E8F0;    /* Muted slate for card borders */
}
```

---

## 3. Logo & Favicon Mark

### Favicon Mark (`favicon.svg`)
A high-precision monogram featuring **AN** set in **Plus Jakarta Sans** (Bold) on a Deep Slate (`#1E293B`) rounded squircle with a Sapphire Blue accent dot (`#2563EB`).

![Favicon Mark](./favicon.svg)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="64" height="64">
  <rect width="512" height="512" rx="100" fill="#1E293B"/>
  <text x="50%" y="54%" dominant-baseline="middle" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="220" fill="#F8FAFC" letter-spacing="-6">
    AN<tspan fill="#2563EB">.</tspan>
  </text>
</svg>
```

### Full Header Logo (`logo.svg`)
Clean typographic header brand combining the monogram mark with full name and title set in Plus Jakarta Sans & Inter.

![Header Logo](./logo.svg)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="300" height="60">
  <rect x="10" y="20" width="80" height="80" rx="20" fill="#1E293B"/>
  <text x="50" y="65" dominant-baseline="middle" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="38" fill="#F8FAFC">AN<tspan fill="#2563EB">.</tspan></text>
  <text x="115" y="56" dominant-baseline="middle" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="28" fill="#0F172A">Abdullah Naeem</text>
  <text x="115" y="84" dominant-baseline="middle" font-family="'Inter', sans-serif" font-weight="500" font-size="15" fill="#64748B" letter-spacing="1.5">MACHINE LEARNING ENGINEER</text>
</svg>
```

---

## 4. Two-Line Style Note for Claude Project / System Instructions

```text
Style Guide: Fonts: Plus Jakarta Sans (Headings), Inter (Body). Palette: #F8FAFC (Bg), #0F172A (Text), #1E293B (Primary), #2563EB (Accent).
Mood: Minimal, high-precision ML engineering notebook — calm slate & sapphire framing clean code, data contracts, and validation metrics without visual clutter.
```

---

## 5. Pass / Revise Check

- [x] **One or two fonts, not a pile:** Exactly 2 fonts (Plus Jakarta Sans + Inter).
- [x] **Tight palette (3–4 colors) with actual hex codes:** Exactly 4 hex colors (`#F8FAFC`, `#0F172A`, `#1E293B`, `#2563EB`).
- [x] **Simple logo/favicon exists:** `favicon.svg` and `logo.svg` designed and integrated into the repository.
- [x] **Style note describes a single, coherent mood:** Two-line style note locked in for Claude Project custom instructions.
