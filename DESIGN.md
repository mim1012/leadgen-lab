# Leadgen Lab Design System

## Product Context

Leadgen Lab's moving quote page is a static pre-lander for Korean users considering a moving estimate request. Its job is not to maximize impulsive clicks. It should help visitors decide whether they are ready for a partner estimate flow.

## Design Direction

The experience should feel practical, calm, and trustworthy. Treat the page as a lightweight diagnostic tool, not a promotional coupon page. The first viewport should make the qualification flow obvious: value statement and four-question diagnosis first, with affiliate disclosure present but visually quiet.

## Visual Tokens

- Background: `#f7f5ef`
- Surface: `#ffffff`
- Subtle surface: `#fcfbf7`
- Primary text: `#18201c`
- Secondary text: `#53615a`
- Muted text: `#768078`
- Border: `#ddd8cd`
- Primary action: `#17624f`
- Primary dark: `#0d4035`
- Primary soft: `#e7f2ed`
- Affiliate/accent: `#d8662f`
- Accent soft: `#fff0e5`
- Warning soft: `#fff8e8`
- Radius: `8px`
- Shadow: use sparingly, max `0 18px 48px rgba(24, 32, 28, 0.10)`

## Typography

Use Korean system sans-serif fonts: `"Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif`. Keep letter spacing at `0`. Hero text should be large but controlled, with a desktop maximum around `64px` and a mobile range around `34px-40px`. Do not use decorative serif fonts for core UI.

Headlines should use short, forceful lines rather than long explanatory sentences. Prefer a two-part structure: a compact context line, then a bold decision line. Use weight, scale, and subtle color accents for emphasis. Do not rely on giant red blocks or decorative display fonts.

## Layout Rules

- Mobile-first behavior matters more than decorative desktop composition.
- The diagnostic card must be visible in the first desktop viewport and near the top on mobile.
- The diagnosis result should own the next action: ready users go to the partner CTA, not-ready users go to the checklist.
- The checklist should follow the diagnosis directly as the recovery path for users who are not ready.
- Use full-width sections with constrained inner content.
- Cards are allowed only for functional groups such as diagnosis, checklist, and risk notes.
- Do not nest cards inside cards.
- Keep fixed-format controls stable with explicit minimum heights.

## Component Rules

- Buttons use 8px radius, strong contrast, and direct action labels.
- Diagnosis chips must have clear default, hover, and selected states.
- The primary outbound CTA should become most persuasive after the user passes diagnosis.
- The not-ready diagnosis state should show a checklist action instead of leaving users at a dead end.
- Affiliate disclosure should be visible but visually quiet. Prefer a small header/footer line and a fuller disclosure near the final CTA rather than a loud hero badge.
- Checklist rows should read like an operational worksheet, not marketing copy.

## Do Not

- Do not use giant red headline blocks.
- Do not use heavy brutalist shadows.
- Do not use gradient orbs, bokeh blobs, or generic decorative backgrounds.
- Do not make the page look like a coupon ad or urgency funnel.
- Do not bury the diagnosis below long marketing copy.
- Do not claim "no calls", "lowest price", or guaranteed savings.
