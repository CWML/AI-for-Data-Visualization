"""Builds ai_dataviz_2026_workshop.ipynb. Run once, then re-run to regenerate."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []
def md(t): cells.append(nbf.v4.new_markdown_cell(t))
def code(t): cells.append(nbf.v4.new_code_cell(t))

md("""# AI for Data Visualization Workshop
**BDSY 2026 · Friday, June 26, 2026 · 10:45 AM – 12:15 PM**

Welcome back! This is a hands-on **sequel to Python 1**. There you learned to
write a little Python and make a basic `matplotlib` plot. Today we level up:

- We'll use **seaborn**, the modern library that makes good-looking statistical
  plots from a pandas DataFrame in *one line*.
- We'll use the data that ships **inside seaborn** — no files to upload.
- And we'll use **Gemini, built into Google Colab**, to draft plots from plain
  English and to make rough plots better.

> **The rule for today: _AI drafts, you direct._** Gemini writes the code fast;
> *you* decide whether the figure is clear, honest, and makes the point.

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
# 1. Why seaborn? (~10 min)

Think of it this way: **matplotlib is the engine; seaborn is the smart layer on
top.** Seaborn talks to pandas DataFrames directly, does the statistics for you,
and looks good by default. It still *returns* matplotlib objects, so everything
from Python 1 (`plt.title`, `figsize`, `plt.savefig`) still works.

The "aha": this single line **groups by day, averages the bill, AND draws error
bars** — work that took many lines in Python 1.""")
code('''sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average bill by day")
plt.show()''')

md("""**You write the *what*, not the *how*.** You name the DataFrame and which
columns go on x and y — seaborn handles the rest.""")

# ---------------- THREE FAMILIES ----------------
md("""---
# 2. The three families of plots (~20 min)

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
# 3. Semantic mappings — seaborn's superpower (~15 min)

You can map a **column** to a **visual property**. This lets one plot show many
variables at once. The key keywords:

- `hue=`  → **color**
- `size=` → **dot/line size**
- `style=` → **marker shape**
- `col=` / `row=` → split into **separate side-by-side plots** (small multiples)

Watch what `hue="species"` does to our earlier scatter — the three species
separate into clear clouds:""")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
                hue="species")
plt.title("Penguin species separate cleanly by bill & flipper")
plt.show()''')

md("Layer in **two more variables** at once — `size` and `style`:")
code('''sns.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
                hue="species", size="body_mass_g", style="sex")
plt.title("Four variables in one figure")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.show()''')

md("""**Small multiples** with `col=` (a figure-level function, `relplot`) splits
the data into one panel per category — often clearer than cramming it together:""")
code('''sns.relplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
            hue="species", col="island")
plt.show()''')

md("""**`pairplot`** — instant overview: every numeric variable plotted against
every other. Great first look at any new dataset.""")
code('''sns.pairplot(penguins, hue="species")
plt.show()''')

# ---------------- MAIN HANDS-ON: GEMINI ----------------
md("""---
# 4. ★ Main hands-on: build visualizations with Gemini (~30 min)

This is the core of the workshop. You don't have to memorize seaborn — describe
what you want and let **Gemini (built into Colab)** write the code. Then you run,
read, and improve it.

### Where Gemini lives in Colab
- Click **+ Generate** (or the Gemini ✨ icon) above a cell to describe a plot in
  plain English and get a code cell back.
- Select an existing code cell and ask Gemini to **improve / explain** it.
- If a cell errors, click **"Explain error"** — Gemini tells you what went wrong.

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

md("""### Exercise A — ask Gemini for a brand-new plot
Pick one question and prompt Gemini for it (write your prompt, paste the code):
- *"Average tip by day of week, split by lunch vs. dinner."* (`tips`)
- *"Survival rate by passenger class."* (`titanic`)
- *"Passengers per month across years as a heatmap."* (`flights`, needs a pivot)""")
code('''# Your Gemini-built plot here:

''')

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

md("""### Exercise C — catch the hallucination
AI sometimes invents functions that don't exist. The line below is the kind of
thing it produces. Run it, read the error (try *Explain error*), then fix it.""")
code('''# BROKEN ON PURPOSE — there is no sns.scatter(); it's sns.scatterplot()
# sns.scatter(data=penguins, x="bill_length_mm", y="body_mass_g")  # uncomment to see error

# Fix:
sns.scatterplot(data=penguins, x="bill_length_mm", y="body_mass_g")
plt.title("Bill length vs. body mass")
plt.show()''')

# ---------------- POLISH + VERIFY ----------------
md("""---
# 5. Polish, principles & verification (~15 min)

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
