"""Builds ai_dataviz_2026_workshop.ipynb. Run once, then re-run to regenerate."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []
def md(t): cells.append(nbf.v4.new_markdown_cell(t))
def code(t): cells.append(nbf.v4.new_code_cell(t))
def code_raises(t):
    c = nbf.v4.new_code_cell(t)
    c.metadata["tags"] = ["raises-exception"]  # expected to error (demo); keeps run going
    cells.append(c)

md("""# Using AI for Visualization
**BDSY 2026 · Big Data Summer Immersion · Friday, June 26, 2026 · 10:45 AM – 12:15 PM · Room 106A**

Welcome to the last morning of Week 2. By now you've **written Python** (Intro to
Python, Python I & II) and — just yesterday — built statistical graphics with
**ggplot2**. Today we connect those two threads:

- **seaborn is ggplot2's Python cousin.** Same instinct you used yesterday — hand
  it a tidy DataFrame, *map columns to visual properties*, get good defaults out —
  but it speaks pandas instead of R. (`aes(color=)` → `hue=`, `facet_wrap` → `col=`.)
- We use the data that ships **inside seaborn** — no files to upload.
- And we point an **AI coding assistant** at the plotting workflow. You already met
  this loop in *Coding with Claude* — **describe → generate → run → read the error →
  iterate**. Today's vehicle is **Gemini, built into Google Colab** (it's already in
  the room), but the skill is the loop, not the brand.

> **The rule for today: _AI drafts, you direct._** The assistant writes the code
> fast; *you* decide whether the figure is clear, honest, and makes the point. In
> public health a misleading chart isn't just ugly — it misinforms. So the last
> thing we practice is **verifying** what the AI hands you.

Run the setup cell next.""")

md("## ⚙️ Setup — run this cell first")
code('''# ===== SETUP — run this cell first! =====
import seaborn as sns
import matplotlib.pyplot as plt

# One line that makes EVERY plot look professional:
sns.set_theme(style="whitegrid", context="talk")

# seaborn ships with clean datasets — no files needed:
penguins = sns.load_dataset("penguins").dropna()
tips     = sns.load_dataset("tips")
flights  = sns.load_dataset("flights")
titanic  = sns.load_dataset("titanic")

print("Datasets loaded:")
for name, df in [("penguins", penguins), ("tips", tips),
                 ("flights", flights), ("titanic", titanic)]:
    print(f"  {name:9s} {df.shape}  ->  {list(df.columns)}")

penguins.head()''')

# ---------------- WHY SEABORN ----------------
md("""---
# 1. Why seaborn? (~8 min)

Think of it this way: **matplotlib is the engine; seaborn is the smart layer on
top.** Seaborn talks to pandas DataFrames directly, does the statistics for you,
and looks good by default. It still *returns* matplotlib objects, so you can fine-
tune anything with `plt.title`, `figsize`, `plt.savefig`.

**Coming from ggplot2?** You'll feel at home. Yesterday you wrote
`ggplot(df, aes(x, y, color=group)) + geom_point()`. In seaborn that's
`sns.scatterplot(data=df, x=, y=, hue="group")` — same grammar-of-graphics idea
(map columns to aesthetics), Python syntax.

The "aha": this single line **groups by day, averages the bill, AND draws error
bars** — the seaborn equivalent of a `stat_summary` layer, in one call.""")
code('''sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average bill by day")
plt.show()''')

md("""**You write the *what*, not the *how*.** You name the DataFrame and which
columns go on x and y — seaborn handles the rest.""")

# ---------------- THREE FAMILIES ----------------
md("""---
# 2. The three families of plots (~22 min)

Almost every seaborn plot belongs to one of three families, each answering a
different kind of question:

| Your question | Family | Functions |
|---|---|---|
| "How do two **numbers** relate?" | **Relational** | `scatterplot`, `lineplot` |
| "What's the **shape/spread** of a number?" | **Distribution** | `histplot`, `boxplot` |
| "How does a number **compare across categories**?" | **Categorical** | `barplot`, `countplot` |

Pick the family that matches your question — that's visualization principle #1.""")

md("### Relational — `scatterplot`: how do two numbers relate?")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm")
plt.title("Bill length vs. flipper length")
plt.show()''')

md("### Relational — `lineplot`: a trend over time (flights data)")
code('''sns.lineplot(data=flights, x="year", y="passengers")
plt.title("Air passengers over time")
plt.show()''')

md("### Distribution — `histplot`: the shape/spread of one number")
code('''sns.histplot(data=penguins, x="body_mass_g", bins=20)
plt.title("Distribution of penguin body mass")
plt.show()''')

md("### Distribution — `boxplot`: spread of a number across categories")
code('''sns.boxplot(data=penguins, x="species", y="body_mass_g")
plt.title("Body mass by species")
plt.show()''')

md("### Categorical — `countplot`: how many rows in each category?")
code('''sns.countplot(data=titanic, x="class")
plt.title("Number of passengers by class")
plt.show()''')

md("""> 🗣️ **Your turn (try it):** In the blank cell below, make a `barplot` of the
> average **tip** by **day** from the `tips` data. (Hint: copy the bar example
> from section 1 and change the columns.)""")
code('''# Your turn — average tip by day:
''')

# ---------------- SEMANTIC MAPPINGS ----------------
md("""---
# 3. Semantic mappings — seaborn's superpower (~12 min)

You can map a **column** to a **visual property** — exactly the `aes()` idea from
ggplot2. This lets one plot show many variables at once. The key keywords:

- `hue=`  → **color** (ggplot2 `color=`/`fill=`)
- `size=` → **dot/line size**
- `style=` → **marker shape**
- `col=` / `row=` → split into **separate side-by-side plots** (ggplot2 `facet_wrap`)

Watch what `hue="species"` does to our earlier scatter — the three species
separate into clear clouds:""")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
                hue="species")
plt.title("Penguin species separate cleanly by bill & flipper")
plt.show()''')

md("""> 👀 **Demo — watch, don't type.** The next three cells go fast; just follow
> along. You can come back and run them yourself afterward.

Layer in **two more variables** at once — `size` and `style`:""")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
                hue="species", size="body_mass_g", style="sex")
plt.title("Four variables in one figure")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.show()''')

md("""**Small multiples** with `col=` splits the data into one panel per category —
this is ggplot2's `facet_wrap`. Note `relplot` is a **figure-level** function: it
makes its *own* figure, so you style it via the returned grid, not a trailing
`plt.title()`. (Same goes for `pairplot` and `catplot`.)""")
code('''sns.relplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
            hue="species", col="island")
plt.show()''')

md("""**`pairplot`** — instant overview: every numeric variable plotted against
every other. Great first look at any new dataset.""")
code('''sns.pairplot(penguins, hue="species")
plt.show()''')

# ---------------- MAIN HANDS-ON: GEMINI ----------------
md("""---
# 4. ★ Main hands-on: drive an AI coding assistant (~32 min)

This is the core of the workshop. You don't have to memorize seaborn — **describe
what you want, let the assistant draft the code, then run, read, and improve it.**

### The loop (you met it in *Coding with Claude*)
**describe → generate → run → read the output/error → refine.** It's the same loop
whether the assistant is Claude, Copilot, or Gemini — what makes *you* effective is
a clear request and a critical eye on what comes back. Today we use **Gemini,
because it's built right into Colab** and needs no separate account.

### Where Gemini lives in Colab
- Click **+ Generate** (or the Gemini ✨ icon) above a cell to describe a plot in
  plain English and get a code cell back.
- Select an existing code cell and ask Gemini to **improve / explain** it.
- If a cell errors, click **"Explain error"** — Gemini tells you what went wrong.

> **Don't see Gemini?** UI and access vary. No problem — every exercise below
> includes a worked answer you can expand and use, so you're never stuck waiting.

### A good visualization prompt has four parts
1. **Dataset & columns** — name the DataFrame and the columns to use.
2. **Goal** — the question / the takeaway.
3. **Constraints** — "use seaborn", colorblind-safe, one figure, add a title.
4. **Chart type** (optional) — if you already know it, say so.

### Copy this prompt into Gemini
```
Using the pandas DataFrame `penguins` (columns: species, island,
bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex),
use seaborn to plot body_mass_g for each species as a boxplot, colored
by sex, with a colorblind-safe palette and a clear title. Return only code.
```""")
md("**Paste Gemini's code below and run it.** Did it work first try? If it errors, use *Explain error* or paste the error back to Gemini.")
code('''# Paste Gemini's generated code here, then run:

''')

md("> 👉 **Stuck / no Gemini?** Expand-and-run this worked answer (try the prompt first):")
code('''# Worked answer for the boxplot prompt above:
sns.boxplot(data=penguins, x="species", y="body_mass_g", hue="sex",
            palette="colorblind")
plt.title("Body mass by species and sex")
plt.xlabel("Species"); plt.ylabel("Body mass (g)")
plt.show()''')

md("""### Exercise A — ask Gemini for a brand-new plot
Pick one question and prompt Gemini for it (write your prompt, paste the code):
- *"Average tip by day of week, split by lunch vs. dinner."* (`tips`)
- *"Survival rate by passenger class."* (`titanic`)
- *"Passengers per month across years as a heatmap."* (`flights`, needs a pivot)""")
code('''# Your Gemini-built plot here:

''')

md("> 👉 **Stuck / no Gemini?** A worked answer for the survival-rate option:")
code('''# Survival rate by passenger class (titanic):
sns.barplot(data=titanic, x="class", y="survived", palette="colorblind")
plt.title("First-class passengers survived at the highest rate")
plt.xlabel("Passenger class"); plt.ylabel("Survival rate")
plt.show()''')

md("""### Exercise B — "make it better"
Here's a working-but-ugly plot. Select it (or copy it into Gemini) and ask:
> *"Make this chart presentation-ready: clean theme, colorblind-safe palette, a
> title that states the takeaway, labeled axes with units, bigger fonts."*

Then paste Gemini's improved version in the next cell and compare.""")
code('''# BEFORE (works, but bland):
sns.scatterplot(data=penguins, x="bill_length_mm", y="body_mass_g", hue="species")
plt.show()''')
code('''# AFTER — paste Gemini's improved version here:

''')

md("> 👉 **Stuck / no Gemini?** One presentation-ready version of the plot above:")
code('''fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=penguins, x="bill_length_mm", y="body_mass_g",
                hue="species", palette="colorblind", s=70, alpha=0.8, ax=ax)
ax.set_title("Bigger bills track with heavier penguins", weight="bold")
ax.set_xlabel("Bill length (mm)"); ax.set_ylabel("Body mass (g)")
ax.legend(title="Species")
plt.show()''')

md("""### Exercise C — catch the hallucination
AI confidently invents functions that don't exist. The cell below is the kind of
thing it produces — **`sns.scatter()` is not a real function.** This is *your*
job, not the AI's: run it as-is, read the error (try *Explain error*), and **fix
it in the next cell.** This "does the output match reality?" check is the whole
point of today — a chart that *runs* can still be wrong or misleading.""")
code_raises('''# RUN THIS — it will error on purpose:
sns.scatter(data=penguins, x="bill_length_mm", y="body_mass_g")
plt.title("Bill length vs. body mass")
plt.show()''')
md("**Your fix below** — correct the function name (and add honest labels):")
code('''# Fix the broken call above:

''')
md("> 👉 Worked answer:")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="body_mass_g")
plt.title("Bill length vs. body mass")
plt.xlabel("Bill length (mm)"); plt.ylabel("Body mass (g)")
plt.show()''')

# ---------------- POLISH + VERIFY ----------------
md("""---
# 5. Polish, principles & verification (~13 min)

A plot that *runs* is not the same as a plot that's *ready to present*. Five
principles, each a small seaborn choice:

1. **Right chart** → pick the matching family (you did this in §2).
2. **Reduce clutter** → `sns.set_theme(style="whitegrid")` (already on).
3. **Color with intent** → `palette="colorblind"`; use `hue` for real categories.
4. **Label to stand alone** → a *takeaway* title, axis labels **with units**.
5. **Don't mislead** → honest axes and aggregation.

Here's the same penguin scatter, polished and exported for slides:""")
code('''fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=penguins, x="bill_length_mm", y="body_mass_g",
                hue="species", palette="colorblind", s=60, alpha=0.8, ax=ax)
ax.set_title("Gentoo penguins are the largest by body mass", weight="bold")
ax.set_xlabel("Bill length (mm)")
ax.set_ylabel("Body mass (g)")
ax.legend(title="Species")
fig.savefig("penguins_polished.png", dpi=200, bbox_inches="tight")
plt.show()
print("Saved penguins_polished.png — drop it into your slides or report.")''')

md("""### ✅ Trust-this-figure checklist (before you believe any AI plot)
- [ ] The code runs and uses **real** functions (no hallucinated `sns.scatter`).
- [ ] The **chart type matches the question** (right family).
- [ ] **Axes, units, and the title** are correct and honest.
- [ ] The **numbers match the data** — spot-check one value.
- [ ] A stranger could read it **without you explaining it**.

Quick verify — does the figure's story match the raw numbers?""")
code('''print(penguins.groupby("species")["body_mass_g"].mean().round(0))''')

md("""---
## Where to go from here
- These skills carry straight into your later Python & ML courses (loss curves,
  confusion matrices, feature distributions — all seaborn).
- See the `README.md` for a resource list (seaborn tutorial, Data-to-Viz,
  ColorBrewer).
- Keep a personal **prompt library** of the viz prompts that worked for you.

🎉 **Nice work!** You used seaborn for real plots, drove Gemini to draft and
improve them, and learned to verify before you trust.""")

nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
    "colab": {"provenance": []},
}
with open("ai_dataviz_2026_workshop.ipynb", "w") as f:
    nbf.write(nb, f)
print("Wrote ai_dataviz_2026_workshop.ipynb with", len(cells), "cells")
