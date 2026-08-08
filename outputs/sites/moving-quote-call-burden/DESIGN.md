# 다이사 전환형 랜딩 디자인 시스템

## 1. Direction
정보 허브가 아니라 이사 견적 신청으로 이어지는 짧은 전환 여정입니다. 밝은 종이 질감의 배경, 짙은 잉크색 CTA, 파란 선택 상태를 사용해 신뢰감과 진행감을 동시에 만듭니다.

## 2. Tokens
- Typeface: Pretendard Variable
- Base unit: 4px
- Page: #f7f7f5
- Surface: #ffffff
- Warm surface: #faf9f7
- Text: #1a1a1a, secondary #4b5563, muted #9ca3af
- Accent: #1d4ed8, hover #1e40af
- CTA: #111827, hover #1f2937
- Border: #e8e6e1 / light #f0eeea
- Radius: 8px / 12px / 16px

## 3. Layout grammar
- Mobile-first single-column funnel, max width 480px.
- Disclosure bar precedes the hero.
- Hero has one primary action that scrolls to the qualifier.
- Qualifier uses two compact selection groups and unlocks the final CTA only after both are selected.
- Trust, process, FAQ, and bottom CTA support the primary action without competing destinations.

## 4. Interaction states
- Option: default, hover, selected, focus-visible.
- Ready CTA: disabled/low emphasis before both answers, active after completion.
- FAQ: closed/open.
- Progress: 0, 40, 80 percent.
- Reduced motion: preserve state changes while disabling non-essential movement.

## 5. Reusable primitives
- DisclosureBar
- HeroPrimaryCTA
- StepCard
- StepOption
- ReadyCTA
- TrustItem
- ProcessStep
- FAQItem
- BottomCTA

## 6. Accessibility and compliance
- Affiliate disclosure is visible at the top.
- No personal data is collected on this page; data entry happens on the external partner page.
- Official ADLIX tracking URL remains unmodified.
- Interactive options use text labels and keyboard-accessible DOM elements.
- External CTA tracking records the selected qualifier state before navigation.

## 7. Performance notes
- One self-contained HTML document with one deferred external font stylesheet.
- No framework runtime or third-party analytics bundle.
- Tracking is fire-and-forget and does not block the page interaction.
