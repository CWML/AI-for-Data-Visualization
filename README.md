# https://github.com/CWML/AI-for-Data-Visualization

## Using AI & Python for Data Visualization

A hands-on 2-hour workshop introducing **seaborn** — Python's most approachable statistical graphics library — alongside an **AI coding assistant** workflow. Participants learn just enough seaborn to direct and verify an AI (Gemini in Colab, ChatGPT, Claude, or any tool they already use) as it drafts charts. All examples use the clean datasets that ship inside seaborn (penguins, tips, flights, titanic), so there are no files to upload.

### In this 2-hour in-person session, you'll learn how to:

- Use **seaborn** for the three families of plots — relational (`scatterplot`, `lineplot`), distribution (`histplot`, `boxplot`), and categorical (`barplot`, `countplot`)
- Layer multiple variables into one figure with **semantic mappings** (`hue`, `size`, `style`, `col`) — seaborn's grammar-of-graphics approach to mapping data columns to visual properties
- Apply five core visualization principles (chart choice, reducing clutter, intentional color, labeling, avoiding misleading charts)
- Work with an **AI coding agent** (Gemini in Colab) using the describe → generate → run → read-the-error → iterate loop
- Write effective visualization prompts (dataset & columns → goal → constraints → chart type)
- Recognize and catch the common failure modes of AI-generated charts (hallucinated functions, wrong chart types, misleading scales, altered data)
- Apply the full workflow to **your own data or research question** in the open-work section

### What to know about this session:

This training is hands-on; come ready to code alongside the instructor. No prior plotting experience is required — if you're comfortable with basic Python and familiar with pandas DataFrames, you're ready. We use **Google Colab** (which has Gemini built in — no separate AI account or API key needed). Details about technical setup will be emailed to registrants a few days before the course begins. Please note that registration is required for this event.

The hands-on portion is located in the `ai_dataviz_2026_workshop.ipynb` Jupyter notebook file. This file can be viewed in GitHub or your preferred Jupyter notebook environment. [colab.research.google.com](https://colab.research.google.com) is utilized in the class.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_workshop.ipynb)

### Notebook variants & slides

- **`ai_dataviz_2026_workshop.ipynb`** — complete notebook with full code and worked answers (best for self-study). [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_workshop.ipynb)
- **`ai_dataviz_2026_instructor.ipynb`** — full code plus an inline teaching script (timing cues, what to say, what to click in Colab). For the instructor's private screen. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_instructor.ipynb)
- **`ai_dataviz_2026_student.ipynb`** — blank code cells to fill in live, trimmed prose, no solutions. The participant worksheet to project / share. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_student.ipynb)

A short (~5 min) opener deck lives in `slides/ai-for-dataviz-intro.md` (Marp markdown — see the comment at the top of the file for how to render it to PDF/PPTX/HTML).

### Session timeline

| Section | Content | Time |
|---|---|---|
| Slides + intro | Framing, the one rule, the loop | ~5 min |
| Setup | Run setup cell, explore datasets | ~2 min |
| §1 Why seaborn? | matplotlib vs. seaborn, barplot demo | ~8 min |
| §2 Three families | Relational / distribution / categorical, hands-on | ~22 min |
| §3 Semantic mappings | hue, size, style, col — small multiples | ~12 min |
| §4 AI hands-on | Prompt, paste, run, debug, iterate (4 exercises) | ~32 min |
| §5 Polish & verify | 5 principles, trust-this-figure checklist | ~15 min |
| §6 Bring your own | Open work time — your data or your question | ~25 min |
| **Total** | | **~2 hours** |

### Data

All workshop data comes from seaborn's built-in datasets via `sns.load_dataset(...)` — **penguins** (the main one), **tips**, **flights**, and **titanic**. Nothing to download or upload.

### Where to go from here (after class)

- Seaborn tutorial: https://seaborn.pydata.org/tutorial.html
- Seaborn example gallery: https://seaborn.pydata.org/examples/index.html
- Matplotlib quick start: https://matplotlib.org/stable/users/explain/quick_start.html
- Pandas 10-minute intro: https://pandas.pydata.org/docs/user_guide/10min.html
- Data-to-Viz (how to choose a chart): https://www.data-to-viz.com/
- ColorBrewer (colorblind-safe palettes): https://colorbrewer2.org/
- Gemini in Colab (data science help): https://colab.research.google.com/

### Seaborn & visualization resources

Additional resources used in building this material:

- Seaborn — *An Introduction to Seaborn*: https://seaborn.pydata.org/tutorial/introduction.html
- Ritza Articles — *Matplotlib vs. seaborn vs. Plotly vs. MATLAB vs. ggplot2 vs. pandas*: https://ritza.co/articles/matplotlib-vs-seaborn-vs-plotly-vs-MATLAB-vs-ggplot2-vs-pandas/
- Seaborn — *Example gallery*: https://seaborn.pydata.org/examples/index.html
- W3Schools — *Seaborn*: https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp
- Datacamp — *Python Seaborn Cheat Sheet*: https://www.datacamp.com/cheat-sheet/python-seaborn-cheat-sheet
- Simplilearn — *A Complete Guide to Data Visualization in Python With Libraries & More*: https://www.simplilearn.com/tutorials/python-tutorial/data-visualization-in-python
- TutorialsPoint — *Seaborn tutorial*: https://www.tutorialspoint.com/seaborn/seaborn_tutorial.pdf
