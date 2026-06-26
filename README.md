# https://github.com/j-demayo/AI-for-Data-Visualization

## Using AI for Visualization

A hands-on BDSY session that connects two threads you've already worked with this program: **Python** (Intro to Python, Python I & II) and **statistical graphics with ggplot2**. Here you meet **seaborn** — ggplot2's Python cousin — the library that turns a pandas DataFrame into a good-looking statistical figure in one line, and you use **Gemini (built into Google Colab)** as an **AI coding agent**: describe the plot you want in plain English, generate it, run it, read the errors, and iterate. All examples use the clean datasets that ship inside seaborn (penguins, tips, flights, titanic), so there are no files to upload.

> Coming from yesterday's ggplot2 session? You'll feel at home. `ggplot(df, aes(x, y, color=group)) + geom_point()` becomes `sns.scatterplot(data=df, x=, y=, hue="group")` — same grammar-of-graphics idea (map columns to aesthetics), Python syntax.

### In this 90-minute in-person session, you'll learn how to:

- Use **seaborn** for the three families of plots — relational (`scatterplot`, `lineplot`), distribution (`histplot`, `boxplot`), and categorical (`barplot`, `countplot`)
- Layer multiple variables into one figure with **semantic mappings** (`hue`, `size`, `style`, `col`), the seaborn equivalent of ggplot2 aesthetics and facets
- Apply five core visualization principles (chart choice, reducing clutter, intentional color, labeling, avoiding misleading charts)
- Work with an **AI coding agent** (Gemini in Colab) using the describe → generate → run → read-the-error → iterate loop — building on the "Coding with Claude" session earlier in the program
- Write effective visualization prompts (dataset & columns → goal → constraints → chart type)
- Recognize and catch the common failure modes of AI-generated charts (hallucinated functions, wrong chart types, misleading scales, altered data)

### What to know about this session:

This training is hands-on; come ready to code alongside the instructor. It builds on the Python and ggplot2 work you've already done this program — you should be comfortable with basic Python and the grammar-of-graphics idea of mapping data columns to visual properties. We use **Google Colab** (which has Gemini built in — no separate AI account or API key needed). Details about technical setup will be emailed to registrants a few days before the course begins. Please note that registration is required for this event.

The hands-on portion is located in the `ai_dataviz_2026_workshop.ipynb` jupyter notebook file. This file can be viewed in GitHub or your preferred jupyter notebook environment. [colab.research.google.com](https://colab.research.google.com) is utilized in the class.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_workshop.ipynb)

### Notebook variants & slides

All three notebooks are generated from a single source (`build_notebook.py`) — run `python build_notebook.py` to regenerate them so they never drift:

- **`ai_dataviz_2026_workshop.ipynb`** — complete notebook with full code and worked answers (best for self-study). [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_workshop.ipynb)
- **`ai_dataviz_2026_instructor.ipynb`** — full code plus an inline teaching script (timing cues, what to say, what to click in Colab). For the instructor's private screen. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_instructor.ipynb)
- **`ai_dataviz_2026_student.ipynb`** — blank code cells to fill in live, trimmed prose, no solutions. The participant worksheet to project / share. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/j-demayo/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_student.ipynb)

A short (~5 min) opener deck lives in `slides/ai-for-dataviz-intro.md` (Marp markdown — see the comment at the top of the file for how to render it to PDF/PPTX/HTML).

### Data

All workshop data comes from seaborn's built-in datasets via `sns.load_dataset(...)` — **penguins** (the main one), **tips**, **flights**, and **titanic**. Nothing to download or upload.

### Where to go from here (after class)

These skills carry directly into later Python and machine-learning courses, where clear figures (loss curves, confusion matrices, feature distributions) matter just as much.

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
