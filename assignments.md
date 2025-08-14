---
layout: page
title: Assignments
description: Full detail on course assignments.
nav_order: 6
---


## 📝 Assignments

Several lab assignments, as well as one group assignment, will build up to the final group report.  
**Starting in Week 4:** there will be a group check-in (written outcome from a scrum) due **every other week**.

### Project Data Context
The **Labor Action Tracker (LAT)** is maintained by Cornell University’s School of Industrial and Labor Relations.  
Since 2021, the LAT project has combined **public data sources** and **crowdsourced reports** to track strikes, protests, and other labor actions across the United States.

For this project, you will use LAT data **up to December 5, 2023** to train and validate your predictive models.  
You will then test your models on **new data from December 4, 2023 through February 1, 2025**.

---

### Assignment #1: Ideal Data and Team Plan  
**Due:** 11:59 PM on **October 3**

**Part I:** What would the ideal dataset for answering the research question look like? (≤ 300 words)  
**Part II:** How does the actual LAT data compare with your ideal? How will you proceed? (≤ 500 words)  
**Part III:** Provide an explicit plan for the quarter, including:
- Proposed division of labor or specialized roles
- Communication methods (e.g., Slack, Discord, Google Docs)
- Meeting frequency and type
- Where you will store your team’s work
- How you will ensure clean workflow and version control

---

### Assignment #2: Locating Labor Actions  
**Due:** 11:59 PM on **October 31**

1. Decide as a group how to handle LAT dataset entries with multiple locations.  
   - Report your decision and rationale (1 paragraph).  
   - State, in one sentence, the **unit of analysis** of the LAT data after wrangling.
2. Assign latitude/longitude coordinates to US counties.  
   - Use ChatGPT or Claude as a starting point.  
   - Submit the LLM transcript and a 1-paragraph reflection on whether it was helpful, including challenges or errors.
3. Using what you learned in (2), create a `county` variable in the LAT data.  
   - Submit your code and a screenshot of the `head()` of the LAT dataframe including the new county variable.  
   - Verify the accuracy of your county assignments.

---

### Assignment #3: Data Analysis Report  
**Due:** 8:00 AM on **December 6**

Produce a short report (≤ 4 pages / 1500 words) that reads as a cohesive document, not an FAQ.  
It should address:

**Introduction**
- Outcome you modeled
- Model you chose and why (e.g., logistic regression, random forest)
- Main takeaways and conclusions

**Data**
- Adjustments made to the provided data (new variables, treatment of outliers, transformations)
- External or supplementary data used
- How missing/incomplete data was handled

**Model**
- Models you investigated and compared
- Training process (feature selection, parameter tuning)
- Model performance on validation and test sets
- Model(s) you rely on for conclusions, and why

**Conclusions**
- Weaknesses or unanswered questions
- Usefulness of your chosen model in context
- Any policy implications

**Figures/Tables**
- Include 1–2 data-driven figures or graphics your group produced
- All tables/figures must be labeled, captioned, and discussed

**Important Notes**
- Submit as a `.pdf` produced with Quarto/RMarkdown, with **all code embedded** in the `.qmd`/`.Rmd` file. We expect both the pdf and `.qmd`/`.Rmd` submissions separately. 
- No code in the compiled report — only in the source.
- All work must be reproducible by an external reviewer with no extra setup.
- All analysis in R only (no Excel/Stata).
