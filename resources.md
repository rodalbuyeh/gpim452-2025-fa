---
layout: page
title: Resources
description: Useful links and resources for R, RStudio, and Quarto.
nav_order: 4
---

# 📚 Resources (R / RStudio / Quarto)
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Supplemental Resources

### Course-Specific Resources

These resources directly complement the lectures, labs, and assignments in this course.

- **Textbook**: Baumer, Kaplan, Horton. *Modern Data Science with R* (MDSR3) → [Free online version](https://mdsr-book.github.io/mdsr3e/)
- [R for Data Science (2e)](https://r4ds.hadley.nz/) — comprehensive introduction to R, tidyverse, and workflows
- [Data Visualization: A Practical Introduction](https://socviz.co/) — Kieran Healy’s excellent free book
- [Quarto Documentation](https://quarto.org/docs/reference/) — for `.qmd` report authoring
- [Posit Cloud](https://posit.cloud) — cloud-hosted RStudio for browser-based coding
- [Cheat Sheets (RStudio)](https://posit.co/resources/cheatsheets/) — official R cheat sheets
- [R Graph Gallery](https://r-graph-gallery.com/) — visual inspiration for data plots

---

### R Extra Practice

General resources for improving your R skills.

- [swirl](https://swirlstats.com/) — interactive R learning in your console
- [Learn R Tidyverse](https://r4ds.hadley.nz/) — interactive examples & exercises
- [DataCamp R Courses](https://www.datacamp.com/category/r?page=1) *(some free)*
- [Software Carpentry R Lessons](https://swcarpentry.github.io/r-novice-gapminder/)
- [Exercism R Track](https://exercism.org/tracks/r)

---

### Probability & Statistics Practice

For extra practice beyond our course lectures and assignments:

- [Khan Academy Probability & Statistics](https://www.khanacademy.org/math/statistics-probability)
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive probability and statistics concepts
- [Introduction to Modern Statistics (IMS)](https://openintro-ims.netlify.app/) — free, open-source statistics text in R

---

### Interactive Tools

- [esquisse](https://dreamrs.github.io/esquisse/) — RStudio add-in for drag-and-drop ggplot2 creation
- [DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/index.html) — quick EDA reports
- [Shiny Gallery](https://shiny.posit.co/gallery/) — interactive dashboards built in R

---

### Instructional Videos

These videos walk through common R and Quarto tasks you’ll encounter.

- [Intro to R and RStudio](https://youtu.be/_V8eKsto3Ug)
- [R Markdown / Quarto Basics](https://youtu.be/_f3latmOhew?si=4KimsUc_Q3MOxlnc)
- [Data Wrangling with dplyr](https://youtu.be/Gvhkp-Yw65U?si=6WqJZagk3ek-EbIJ)
- [Data Visualization with ggplot2](https://www.youtube.com/live/h29g21z0a68?si=3-4HU8ahwlr9t81T)

---

### Review Videos

- [Tidyverse join functions explained](https://youtu.be/v9GMXGpj2K0?si=WHSrcgI4-a6DYlA3)
- [Apply functions in R](https://youtu.be/7sJ8r6Lb7-o?si=ppZlfZKN_54myB7_)

---

## Practice & Exam Prep

While our course assessments are unique, practicing R coding and analysis with open datasets is the best preparation.

- [TidyTuesday](https://github.com/rfordatascience/tidytuesday) — weekly data challenges
- [OpenIntro Datasets](https://openintrostat.github.io/openintro/) — clean, public datasets in an R package
- [RStudio Primers](https://posit.cloud/learn/primers) — interactive tutorials

---

## UC San Diego Links

- [Library Guide to Data and Statistics](https://ucsd.libguides.com/data-statistics)
- [Academic Integrity Homepage](https://academicintegrity.ucsd.edu)
- [Counseling and Psychological Services (CAPS)](https://caps.ucsd.edu)

---

## 🐍 Python Resources

For learners interested in transitioning from **R to Python**, with emphasis on **machine learning workflows** and reproducible data science.

### Transitioning from R to Python

| Task | R Package / Function | Python Equivalent | Learn More |
|------|----------------------|-------------------|-------------|
| Data manipulation | `dplyr`, `tidyr` | `pandas` (`query`, `assign`, `melt`, `pivot`) | [DataCamp: Pandas Foundations](https://www.datacamp.com/courses/pandas-foundations) |
| Statistical modeling | `lm`, `glm`, `caret` | `statsmodels`, `scikit-learn` | [scikit-learn User Guides](https://scikit-learn.org/stable/user_guide.html) |
| Visualization | `ggplot2` | `matplotlib`, `seaborn`, `plotnine` | [DataCamp: Data Visualization in Matplotlib](https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib) |
| Data I/O | `readr`, `haven` | `pandas.read_csv`, `pyreadstat`, `openpyxl` | [Real Python: Reading and Writing Files](https://realpython.com/read-write-files-python/) |
| Functional programming | `purrr` | `map`, `itertools`, `toolz` | [Real Python: Functional Programming](https://realpython.com/python-functional-programming/) |
| Tidy evaluation | `rlang`, `across()` | Pandas chaining or `pipe()` | [Modern Pandas Tutorial](https://tomaugspurger.github.io/modern-1-intro.html) |
| Reproducible notebooks | `RMarkdown` | `Jupyter`, `Quarto` | [Quarto Docs](https://quarto.org/docs/computations/python.html) |

**See also:**  
- [Pandas Comparison with R](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html)  
- [Datacamp Python for R Users](https://www.datacamp.com/courses/python-for-r-users)  

### Machine Learning Workflows

Core Python ecosystem for applied ML:

- `numpy` — numerical computation  
- `pandas` — structured data manipulation  
- `scikit-learn` — regression, classification, pipelines, model selection  
- `xgboost`, `lightgbm`, `catboost` — gradient boosting frameworks  
- `tensorflow`, `pytorch` — deep learning  
- `mlflow` — experiment tracking  
- `optuna` — hyperparameter optimization  

**Hands-on training:**  
- [DataCamp Machine Learning Scientist Track](https://www.datacamp.com/tracks/machine-learning-scientist-with-python)  
- [Kaggle Learn: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)  
- [fast.ai Practical Deep Learning](https://course.fast.ai/)  
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)

### Environment and Workflow Tools

**Setup:**  
- `conda` / `mamba` — manage environments  
- `poetry` — dependency and packaging management  
- `jupyterlab` — interactive notebooks  
- `git` + `GitHub` — version control  

**Reference courses:**  
- [Linux Command Line for Beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)  
- [Real Python: Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)  
- [VS Code for Python](https://code.visualstudio.com/docs/languages/python)

### Python Further Reading

- [Python Data Science Handbook – Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/)  
- [Introduction to Machine Learning with Python – O'Reilly](https://learning.oreilly.com/library/view/introduction-to-machine/9781449369880/)  
- [Kaggle: Python Course](https://www.kaggle.com/learn/python)  
- [Real Python Tutorials](https://realpython.com/)  

---

## Highly Recommended for Power Users
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
- [Google's Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)