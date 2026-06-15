"""Builds ai_dataviz_2026_workshop.ipynb. Run once, then delete if you like."""
import json, nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []
def md(t): cells.append(nbf.v4.new_markdown_cell(t))
def code(t): cells.append(nbf.v4.new_code_cell(t))

md("""# AI for Data Visualization Workshop
**BDSY 2026 · Friday, June 26, 2026 · 10:45 AM – 12:15 PM**

Welcome! This notebook is the hands-on portion of the session. You'll build on
your **Python 1** skills (Python, `pandas`, `matplotlib`/`seaborn`) and practice
using an AI assistant to draft, debug, and polish figures.

**The rule for today: _AI drafts, you direct._** AI is great at writing plotting
code; *you* decide whether the figure is honest and makes the point.

Run the setup cell below first.""")

md("## ⚙️ Setup — run this cell first")
code('''# ===== SETUP — run this cell first! =====
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# ---- Recreate the datasets from the "Art of Data Visualization" course ----

# 1) Monthly sales by product category (6 months)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_over_time = pd.DataFrame({
    "month": months * 3,
    "category": (["Electronics"] * 6) + (["Furniture"] * 6) + (["Clothing"] * 6),
    "sales": np.concatenate([
        np.random.normal(500, 30, 6),   # Electronics highest
        np.random.normal(300, 25, 6),   # Furniture middle
        np.random.normal(150, 20, 6),   # Clothing lowest
    ]).round(0),
})

# 2) Number of sales by product type and gender
n = 600
product_gender = pd.DataFrame({
    "product": np.random.choice(["Phone", "Laptop", "Tablet"], n, p=[0.5, 0.3, 0.2]),
    "gender": np.random.choice(["Male", "Female"], n),
})

# 3) Income vs. test score, by school type, with hours studied
m = 300
school = np.random.choice(["A", "B", "C"], m)
income = np.random.uniform(20, 120, m)             # thousands
hours = (income / 20 + np.random.normal(0, 1, m)).clip(0, 12)
base = {"A": 50, "B": 75, "C": 62}
score = np.array([base[s] for s in school]) + 0.15 * income + 1.2 * hours \
        + np.random.normal(0, 4, m)
students = pd.DataFrame({"school_type": school, "income": income.round(1),
                         "hours_studied": hours.round(1), "test_score": score.round(1)})

# 4) Four variables with a known correlation structure (Task 8)
k = 250
X1 = np.random.normal(0, 1, k)
X2 = np.random.normal(0, 1, k)                      # independent
X3 = 0.9 * X1 + np.random.normal(0, 0.3, k)        # strong + with X1
X4 = -0.5 * X1 + np.random.normal(0, 0.7, k)       # moderate - with X1
relationships = pd.DataFrame({"X1": X1, "X2": X2, "X3": X3, "X4": X4})

print("Datasets ready:")
for name, dfv in [("sales_over_time", sales_over_time), ("product_gender", product_gender),
                  ("students", students), ("relationships", relationships)]:
    print(f"  {name:18s} {dfv.shape}")
sales_over_time.head()''')

# ---------------- PART 1 ----------------
md("""---
# Part 1 — Five principles that decide if a figure works (~20 min)

We'll anchor each principle on a real plot from the course data. As we go, ask:
*does this figure answer the question clearly?*

1. **Pick the encoding that matches the question.**
2. **Reduce non-data ink** (clutter, heavy gridlines, 3D).
3. **Use color with intent** (categorical vs. sequential; colorblind-safe).
4. **Label so the figure stands alone** (takeaway title, units, annotation).
5. **Don't mislead** (truncated axes, dual axes, area traps).""")

md("**Principle 1 — match the encoding to the question.** *How do sales change over time, by category?* Time → a line chart shows trend and keeps categories comparable.")
code('''fig, ax = plt.subplots(figsize=(7, 4))
for cat, g in sales_over_time.groupby("category"):
    ax.plot(g["month"], g["sales"], marker="o", label=cat)
ax.set_title("Sales over time by category")
ax.legend()
plt.show()''')

md("""**Principle 5 — don't mislead.** The same data with a *truncated y-axis* exaggerates differences. Run both and compare what your eye concludes.""")
code('''fig, axes = plt.subplots(1, 2, figsize=(11, 4))
piv = sales_over_time.pivot(index="month", columns="category", values="sales").loc[months]
piv.plot(ax=axes[0], marker="o");  axes[0].set_title("Honest: y starts at 0")
axes[0].set_ylim(0, None)
piv.plot(ax=axes[1], marker="o");  axes[1].set_title("Misleading: zoomed y-axis")
axes[1].set_ylim(120, 540)
plt.tight_layout(); plt.show()''')

md("""> 🗣️ **Discuss:** Which of the five principles does each plot above follow or break?
> Look at `examples/art-of-dataviz-course/` for the original course figures and their written interpretations.""")

# ---------------- PART 2 ----------------
md("""---
# Part 2 — Hands-on: let AI draft a plot (~25 min)

You don't have to remember every matplotlib argument. Describe what you want and
let the AI write a first draft — then you fix and direct it.

### A good visualization prompt has four parts
1. **Data shape** — columns, types, a sample (`df.head()` output).
2. **Goal** — the question the figure should answer / the takeaway.
3. **Constraints** — library, size, colorblind-safe, single figure, etc.
4. **Library** — "use seaborn" / "use matplotlib only".

### Copy-paste prompt template
```
I have a pandas DataFrame `product_gender` with columns:
  product (Phone/Laptop/Tablet), gender (Male/Female).
Write Python (seaborn) to plot the COUNT of sales by product, split by gender,
as grouped bars. Use a colorblind-safe palette, add a title and axis labels.
Return only the code.
```""")
md("**Your turn:** paste the AI's answer into the cell below and run it. Does it work on the first try? If it errors, paste the error back to the AI and ask it to fix it.")
code('''# Paste AI-generated code here and run it.
# (Reference solution — try the AI version first, then compare:)
sns.countplot(data=product_gender, x="product", hue="gender",
              order=["Phone", "Laptop", "Tablet"], palette="colorblind")
plt.title("Number of sales by product type and gender")
plt.ylabel("Number of sales"); plt.xlabel("Product")
plt.show()''')

md("""### Debugging exercise — AI hallucinations are real
The cell below is the kind of code an AI sometimes produces: it *looks* right but
uses a function that doesn't exist. Run it, read the error, then fix it (or ask
the AI to). What's wrong?""")
code('''# BROKEN ON PURPOSE — there is no sns.scatter(); the function is sns.scatterplot()
# sns.scatter(data=students, x="income", y="test_score")   # <-- uncomment to see the error

# Fix:
sns.scatterplot(data=students, x="income", y="test_score")
plt.title("Income vs. test score")
plt.show()''')

# ---------------- PART 3 ----------------
md("""---
# Part 3 — Hands-on: from rough draft to professional figure (~25 min)

A working plot is not the same as a *presentation-ready* plot. We'll iterate with
the AI to polish one figure. Start from the rough version, then improve it.""")
md("**Rough draft** — correct, but bland and hard to read at a glance:")
code('''sns.scatterplot(data=students, x="income", y="test_score", hue="school_type")
plt.show()''')

md("""**Polish prompt to try with the AI:**
```
Improve this seaborn scatter of income vs. test_score colored by school_type:
- clean theme, larger fonts, figure 8x5
- colorblind-safe palette
- a TITLE that states the takeaway (higher income & study hours -> higher scores)
- axis labels with units ($000s), legend titled "School type"
- size the points by hours_studied
- export to PNG at 200 dpi with tight bounding box
```""")
code('''# Polished reference figure (compare with the AI's version):
sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=students, x="income", y="test_score", hue="school_type",
                size="hours_studied", sizes=(20, 200), palette="colorblind",
                alpha=0.8, ax=ax)
ax.set_title("Higher income and more study hours track higher test scores",
             fontsize=14, weight="bold")
ax.set_xlabel("Family income ($000s)")
ax.set_ylabel("Test score")
ax.legend(title="School type", bbox_to_anchor=(1.02, 1), loc="upper left")
fig.savefig("income_vs_score.png", dpi=200, bbox_inches="tight")
plt.show()
print("Saved income_vs_score.png — drop this into your slides or report.")''')
md("> 💡 Reset the theme with `sns.set_theme()` defaults if later plots look off, or restart and run Setup again.")

# ---------------- PART 4 ----------------
md("""---
# Part 4 — Pitfalls & a 30-second verification checklist (~10 min)

AI writes plausible code fast — including plausible *mistakes*. Always check:

| # | Failure mode | How to catch it |
|---|--------------|-----------------|
| 1 | **Hallucinated API** (`sns.scatter`, fake kwargs) | Run it; read the error; check the docs |
| 2 | **Wrong chart type** (pie for trends, etc.) | Ask: does the encoding match the question? |
| 3 | **Misleading scale** (truncated/dual axes) | Check that the axis starts where it should |
| 4 | **Altered/dropped data** (silent filtering, wrong aggregation) | Compare row counts / totals before vs. after |

### ✅ Trust-this-figure checklist
- [ ] The code runs and uses real functions.
- [ ] The chart type matches the question.
- [ ] Axes, units, and the title are correct and honest.
- [ ] The numbers match the source data (spot-check a value).
- [ ] A stranger could read it without you explaining it.""")
md("""### Quick exercise — verify the data wasn't altered
Ask the AI for "average test score by school type," then verify its number yourself:""")
code('''print(students.groupby("school_type")["test_score"].mean().round(1))
# Does this match what the AI told you? Spot-check before trusting any figure.''')

md("""---
## Where to go from here
- These skills carry into your later Python and ML courses (loss curves, confusion matrices, feature distributions).
- See the `README.md` for a full resource list (Matplotlib, Seaborn, Data-to-Viz, ColorBrewer).
- Keep a personal **prompt library** of the visualization prompts that worked for you.

🎉 **Nice work!** You drafted with AI, polished a figure, and learned to verify it.""")

nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
    "colab": {"provenance": []},
}
with open("ai_dataviz_2026_workshop.ipynb", "w") as f:
    nbf.write(nb, f)
print("Wrote ai_dataviz_2026_workshop.ipynb with", len(cells), "cells")
