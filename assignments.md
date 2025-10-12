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

---

## 🗂️ Feature Store: Augmenting Your Analysis

To make your assignments **"bigger"** and more sophisticated, consider **augmenting your feature space** by enriching the LAT data with additional contextual variables. The datasets below provide ZIP code–level enrichment that can significantly enhance your predictive models.

### 📍 Geographic Reference

**U.S. Census ZCTA Shapefiles**  
- [Download (TIGER/Line)](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)  
- Polygon boundaries for ZIP Code Tabulation Areas (ZCTAs).  
- Use for spatial joins, mapping, and area aggregation.

**HUD–USPS ZIP Crosswalk**  
- [HUD Crosswalk Files](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)  
- Maps ZIPs to census tracts, counties, CBSAs.  
- Useful when allocating metrics across geographies.

### 💰 Demographic and Economic Data

**IRS ZIP-Code Data**  
- [IRS SOI ZIP-Code Statistics](https://catalog.data.gov/dataset/zip-code-data)  
- Income, returns, and filer counts by ZIP.

**SimpleMaps ZIP Database**  
- [SimpleMaps US ZIP Codes](https://simplemaps.com/data/us-zips)  
- CSV with location, population, time zone, and county.

### 🧮 Deprivation and Socioeconomic Indices

**Neighborhood Atlas – Area Deprivation Index (ADI)**  
- [Download](https://www.neighborhoodatlas.medicine.wisc.edu/)  
- Official ADI at the Census block group level.  
- Can be aggregated to ZIP or ZCTA using population- or area-weighted joins.  
- Measures income, education, employment, and housing disadvantage.

**Social Deprivation Index (SDI)**  
- [Graham Center SDI](https://www.graham-center.org/content/brand/rgc/maps-data-tools/social-deprivation-index.html)  
- Provided at tract, county, and ZCTA levels.  
- Composite of seven ACS indicators (poverty, education, employment, housing, etc.).  
- Ready for ZCTA-level joins.

**Distressed Communities Index (DCI)**  
- [Economic Innovation Group DCI](https://eig.org/distressed-communities/)  
- ZIP-level measure categorizing areas as prosperous to distressed.  
- Combines metrics like poverty, education, and business growth.

**Geomarker.io Deprivation Index (ZCTA)**  
- [GitHub Repository](https://github.com/geomarker-io/dep_index)  
- Open-source deprivation index aggregated to ZCTA from Census tract data.  
- Good for direct ZIP/ZCTA feature joins.

### 🧭 Implementation Notes

- **ZIP vs ZCTA:** USPS ZIPs are routing designations; ZCTAs are Census approximations for area joins.  
- **Aggregation:** Most deprivation indices originate at the census tract or block group level. Use crosswalks or spatial weighting for ZIP-level aggregation.  
- **Boundary overlap:** ZIPs may span multiple counties or states. Use crosswalks for proportional allocation.  
- **Updates:** ZIP codes and Census vintages change regularly. Verify that datasets use consistent reference years.  
- **Licensing:** Check redistribution terms for any third-party or commercial datasets.

### 💡 Feature Engineering Ideas

**Expanding your feature space can dramatically improve model performance:**
- **Economic context:** Join IRS income data to understand local economic conditions
- **Social vulnerability:** Use ADI or SDI scores to capture community disadvantage
- **Geographic clustering:** Create spatial lag variables for neighboring areas
- **Temporal features:** Add seasonality, trends, or time-since-last-action variables
- **Industry context:** Incorporate local employment patterns or business density

**Remember:** More features ≠ better models. Focus on theoretically motivated variables that align with your research question and use proper feature selection techniques to avoid overfitting.
