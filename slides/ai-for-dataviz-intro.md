---
marp: true
title: Using AI for Visualization — Intro
description: 5-minute opener for the Yale Medical Library "Using AI for Visualization" workshop
paginate: true
theme: default
---

<!--
HOW TO USE THIS DECK
- It's a Marp deck (Markdown). Render it any of these ways:
  - VS Code: install the "Marp for VS Code" extension, open this file, click the
    preview / "Export slide deck" button (PDF, PPTX, or HTML).
  - CLI:  npx @marp-team/marp-cli slides/ai-for-dataviz-intro.md --pdf
          npx @marp-team/marp-cli slides/ai-for-dataviz-intro.md --pptx   (edit in Google Slides/PowerPoint)
- Target ~5 minutes, ~1 slide every 40-50s. Open with slides 1-6, then jump into
  the notebook. Slide 7 (the trust checklist) is a callback to show again at the END.
- Speaker notes live in these HTML comments (Marp shows them in presenter view).
-->

# Using AI for Visualization

### Yale Medical Library · 2-Hour Hands-On Workshop

*Use AI to draft charts. Use your judgment to direct and verify them.*

<!--
Open warm. One-liner: "Today you'll use seaborn — Python's statistical graphics
library — and an AI coding assistant to build charts fast. The AI does the typing;
you do the thinking." Quick show of hands: who has used any plotting library before,
in any language? Who has used an AI coding assistant? Anchor to both — we build on
what they know. If someone raises their hand for R or ggplot2, that's a great
segue: seaborn uses the same grammar-of-graphics idea.
-->

---

# Why this matters (it's not just pretty pictures)

- A chart is how data **makes an argument** — to colleagues, reviewers, funders, the public.
- A **misleading** chart doesn't just look bad — it **misinforms**.
- AI can now draft a chart in seconds. That makes **your judgment** the scarce
  skill, not the typing.

> ## The one rule today: **AI drafts, you direct.**

<!--
This is the thesis slide — say the rule out loud and write it on the board if you
can. Give one quick concrete example of a misleading chart (truncated y-axis that
exaggerates a difference, or a wrong aggregation). Keep it to ~45s. Everything else
today serves this rule.
-->

---

# The seaborn grammar: map columns to visual properties

The underlying idea: **hand a DataFrame column to a visual property, and the chart builds itself.**

| What you want | seaborn keyword |
|---|---|
| color by a column | `hue="column"` |
| size dots by a column | `size="column"` |
| split into side-by-side panels | `col="column"` |
| x / y position | `x=` / `y=` |

Same logic applies in any grammar-of-graphics library (R's ggplot2 uses `aes(color=)` and `facet_wrap` for the same ideas). If you've seen it before, it'll feel familiar. If not, you'll have it in 10 minutes.

<!--
Don't teach seaborn here — that's the notebook. Just land the mental model: you
name the DataFrame and the column, seaborn handles the rest. For anyone who's used
ggplot2: the concepts transfer 1:1, just different syntax. ~40s.
-->

---

# The loop

## describe → generate → run → **read** → refine

- Works with **any** assistant: ChatGPT, Claude, Copilot — or **Gemini, built into
  Colab** (nothing to install).
- The skill is the **loop and the critical eye**, not the brand.
- Reading the **error** (or the output) is where the learning happens.

<!--
Emphasize "read." Beginners ask, paste, and pray. The pros read what came back. In
Colab: "+ Generate" / the ✨ icon to draft, "Explain error" when a cell breaks.
Tell them the notebook has worked answers as a safety net so nobody is stuck on AI
access. ~45s.
-->

---

# Anatomy of a good viz prompt

**1. Dataset & columns** → name the DataFrame and exact columns
**2. Goal** → the question / the takeaway
**3. Constraints** → "use seaborn", colorblind-safe, one figure, clear title
**4. Chart type** *(optional)* → if you already know it, say so

```
Using the DataFrame `penguins` (columns: species, body_mass_g, sex, ...),
use seaborn to plot body_mass_g per species as a boxplot, colored by sex,
colorblind-safe palette, clear title. Return only code.
```

<!--
The four-part structure is the single biggest lever on output quality. Contrast
"plot body mass" (vague) vs the full prompt (specific). Tell them they'll reuse this
skeleton all session. ~45s.
-->

---

# The dangerous failures are the *plausible* ones

- AI rarely fails with obvious gibberish.
- It borrows a feature from **another library** and writes code that *looks* right —
  e.g. `trendline="ols"` (that's **Plotly**, not seaborn) → it errors.
- Worse: code that **runs but quietly plots the wrong thing.**

### So we always **verify before we trust.**

<!--
Set up Exercise D and §5 of the notebook. The hallucination isn't scary because it
crashes — it's scary because it's confident and plausible. This is the heart of
"AI drafts, you direct." ~40s. Then transition: "open the notebook, run the setup
cell." -->

---

# ✅ Trust-this-figure checklist

Before you believe **any** AI-generated plot:

- [ ] Uses **real** seaborn functions/arguments (nothing borrowed from another library)
- [ ] **Chart type matches the question** (right family)
- [ ] **Axes, units, title** are correct and honest
- [ ] **Numbers match the data** — spot-check one value
- [ ] A stranger could read it **without you explaining it**

> **AI drafts. You direct. You verify.**

<!--
Don't dwell on this at the open — flash it (~20s) so they know where we're headed.
Bring it BACK at the very end of the session as the closing slide / takeaway. That
bookends the whole 2 hours on the one rule.
-->
