## AI for Data Visualization
A hands-on **sequel to Python 1**. There you learned to write a little Python and make a basic plot — here you level up to **seaborn**, the modern library that turns a pandas DataFrame into a good-looking statistical figure in one line, and you use **Gemini (built into Google Colab)** to draft those plots from plain English and make rough ones better. All examples use the clean datasets that ship inside seaborn (penguins, tips, flights, titanic), so there are no files to upload.

### In this 90-minute in-person session, you'll learn how to:

- Use **seaborn** for the three families of plots — relational (`scatterplot`, `lineplot`), distribution (`histplot`, `boxplot`), and categorical (`barplot`, `countplot`)
- Layer multiple variables into one figure with **semantic mappings** (`hue`, `size`, `style`, `col`)
- Apply five core visualization principles (chart choice, reducing clutter, intentional color, labeling, avoiding misleading charts)
- Use **Gemini in Colab** to draft a plot from a plain-language description and to make a rough plot presentation-ready
- Write effective visualization prompts (dataset & columns → goal → constraints → chart type)
- Recognize and catch the common failure modes of AI-generated charts (hallucinated functions, wrong chart types, misleading scales, altered data)

### What to know about this session:

This training will be hands-on; come ready to code alongside the instructor. It assumes you have completed **Python 1** or are comfortable with basic Python, `pandas`, and `matplotlib`. We use **Google Colab** (which has Gemini built in — no separate AI account or API key needed). Details about technical setup will be emailed to registrants a few days before the course begins. Please note that registration is required for this event.

The hands-on portion is located in the `ai_dataviz_2026_workshop.ipynb` jupyter notebook file. This file can be viewed in GitHub or your preferred jupyter notebook environment. [colab.research.google.com](https://colab.research.google.com) is utilized in the class.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CWML/AI-for-Data-Visualization/blob/main/ai_dataviz_2026_workshop.ipynb)

> **Note:** update the Colab link above once the repository is pushed (it currently assumes `CWML/AI-for-Data-Visualization` on the `main` branch).

### Data

All workshop data comes from seaborn's built-in datasets via `sns.load_dataset(...)` — **penguins** (the main one), **tips**, **flights**, and **titanic**. Nothing to download or upload.

### Bonus reference material

The `examples/art-of-dataviz-course/` folder contains extra plots and write-ups adapted from the *Art of Data Visualization* course. They aren't used in the live session but are kept as additional examples of interpreting visualizations.

### Where to go from here (after class)

These skills carry directly into later Python and machine-learning courses, where clear figures (loss curves, confusion matrices, feature distributions) matter just as much.

- Seaborn tutorial: https://seaborn.pydata.org/tutorial.html
- Seaborn example gallery: https://seaborn.pydata.org/examples/index.html
- Matplotlib quick start: https://matplotlib.org/stable/users/explain/quick_start.html
- Pandas 10-minute intro: https://pandas.pydata.org/docs/user_guide/10min.html
- Data-to-Viz (how to choose a chart): https://www.data-to-viz.com/
- ColorBrewer (colorblind-safe palettes): https://colorbrewer2.org/
- Gemini in Colab (data science help): https://colab.research.google.com/

### Prerequisite

- Python 1 for Data Analysis: https://github.com/CWML/Python1

### General Python & visualization resources
- Python PEP8 style guide: https://peps.python.org/pep-0008/
- Python cheatsheet: https://www.pythoncheatsheet.org/
- See more helpful learning resources (under Python): https://library.medicine.yale.edu/research-data/learn-work-data
