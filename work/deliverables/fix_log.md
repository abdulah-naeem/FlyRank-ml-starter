# Mobile-First Fix Log

**Date:** September 10, 2026
**Author:** Abdullah Naeem

## What Was Audited
- Readability (Contrast)
- Tap Targets (Accessibility)
- Responsive Spacing (Padding)
- Link Integrity (Checking broken paths)

## Fixes Applied

1. **Text Contrast (Accessibility & Readability)**
   - *Problem:* The secondary text (`--text-muted`) was `#64748B`, which could be slightly hard to read against the off-white `#F8FAFC` background on dimmer mobile screens.
   - *Fix:* Darkened the CSS variable to `#475569`, easily passing the WCAG AA contrast ratio while preserving the aesthetic.

2. **Mobile Tap Targets (Accessibility)**
   - *Problem:* Primary and secondary buttons, the submit button, and navigation links didn't explicitly enforce a minimum height, making them potentially harder to tap accurately on phones.
   - *Fix:* Added `min-height: 44px` to `.btn-primary`, `.btn-secondary`, and `.form-submit`. Added `padding: 8px 12px` to `.nav-links a`.

3. **Responsive Card Padding (Layout)**
   - *Problem:* `.contact-card`, `.about-card`, and `.case-card` used a uniform `40px` or `32px` padding. On small viewports (like an iPhone SE), this padding ate up too much horizontal real estate, cramming the text.
   - *Fix:* Added a media query at `max-width: 640px` that scales card padding down to a comfortable `24px`, giving the text room to breathe.

4. **Hero Section Spacing (Layout)**
   - *Problem:* The hero section had `72px` of top padding, pushing the core message too far down the screen on short mobile viewports.
   - *Fix:* Reduced the hero's top padding to `48px` on mobile screens to ensure the primary CTA is visible "above the fold."

5. **Link Integrity & Images**
   - *Problem:* N/A - Links were structurally sound and pointed to valid domains or anchors. No oversized raster images exist in the build (only highly optimized SVGs).
   - *Fix:* Verified `action="/"` on the contact form, LinkedIn URLs, and local PDF resume links. No changes required.
