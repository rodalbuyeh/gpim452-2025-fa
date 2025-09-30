---
layout: page
title: Syllabus
description: >-
  Course policies and information.
nav_order: 2
---

# 📖 Syllabus
{:.no_toc}


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This course provides an introduction to the logic and practice of data science as used in policy making, program evaluation, and corporate enterprise. We do this with extensive, hands-on work with real data using the R statistical computing environment. This course emphasizes the opportunities and challenges of working with high dimensional data, as opposed to the memory and algorithmic challenges associated with big data. The course emphasizes the process of data gathering, pre-processing, and visualization. We then turn to the logic of machine learning, including model selection and hyperparameter tuning.

This course will not magically make you a data scientist, an expert in “big data”, or a professional-grade programmer in 10 weeks. Rather, we aim to provide the conceptual background, ethical framework, and computational experience that will turn someone with policy expertise and social science training into a valuable member of a data science team.

{: .note }
This course also serves as a **gateway for further study** in advanced areas of data science for policy and social science, including:
- Natural language processing
- Network and graph analysis
- Geographic information systems
- Tools and workflows for managing massive datasets

Students who complete this course will emerge better prepared to pursue specialized electives or research in these domains.

### Learning Objectives
* Familiarity with the vocabulary and key concepts in data science
* Understand the difference between big data and high-dimensional data and how one enables the exploitation of the other
* Understand the logic of predictive machine learning
* Gain conceptual understanding and hands on experience with some of the most frequently used ML tools
* See how policymakers and governments apply data science in real world situations
* Develop an appreciation for ethical concerns that big data present, especially for governments

### Skills Objectives
By the end of the course, you should be able to:

- Practice **good computing and workflow management**, including clean project organization
- Recognize potential problems or “red flags” in data or analysis before they cause errors
- Ingest data from multiple sources, including:
  - Reading from local files
  - Pulling from APIs
  - Web scraping
- Clean and summarize data effectively
- Merge and join datasets from multiple tables or sources
- Summarize and visualize **high-dimensional data**
- Apply **dimensionality reduction** techniques where appropriate
- Troubleshoot code and workflow issues in R
- Train, validate, and evaluate predictive models
- Produce compelling, reproducible reports using **Quarto** or **RMarkdown**
- Work effectively in **data-driven policy teams**, including:
  - Remote and asynchronous collaboration
  - Bringing a social science/policy perspective to heterogeneous teams
  - Producing effective, decision-maker-friendly reports
- Integrate basic version control as part of workflow

### Assumed knowledge
This class is an advanced data-intensive elective. We assume the following:
* Completion of QM I and II or equivalent.
* Understanding of basic mathematical concepts and notation such as percent change, exponents and exponentiation, logarithms, summation. Familiarity with linear algebra and differential calculus will be helpful but not assumed.
* Understanding of basic statistical concepts such as probability, frequency, and sampling distributions; central tendency (mean, median, mode); variation (variance, standard deviation, quantile); and conditional probability.
* Familiarity with linear regression, its calculation and interpretation.
* Familiarity with basic statistical graphics (histogram, scatterplot).
* Some previous exposure to statistical computing in R

If these requirements do not apply to you, please contact the instructor immediately.

---
## Course Staff and Meetings

### Class Meetings
* **Time**: Mondays & Wednesdays, 8:00 AM - 9:20 AM
* **Location**: [RBC 3203](https://map.concept3d.com/?id=1005#!ct/18312?m/237145?s/RBC_Main)

### Office Hours
Office hours are your chance to ask for clarification on assignments and concepts. As part of the course grade you are **REQUIRED** to come to office hours at least twice during the quarter.

{: .note }
**You must sign up for a 15-minute office hours slot at least 2 hours prior to the beginning of a session.** You may sign up for one slot per session. If coming as a small group (2-4 people), you may sign up for two consecutive 15-minute slots.

* **Prof. Rod Albuyeh** (ralbuyeh@ucsd.edu)
    * **Hours**: Mondays & Wednesdays, 9:30 AM - 10:30 AM
    * **Location**: [TEC Cafe](https://map.concept3d.com/?id=1005#!ct/18312?m/165696?s/TEC%20Cafe)
    * **Sign-up**: [Sign up for slots here](https://calendly.com/ralbuyeh-sandiego/15min)


---
## Books and Related Materials

### Required Text
* Baumer, Kaplan, and Horton. 2023. *Modern Data Science with R.* 3rd Edition. (MDSR3)
    * Online version at <https://mdsr-book.github.io/mdsr3e/>

All additional required readings will be posted to the course site.

### Optional/Recommended Texts
* **Causal Inference**: Angrist & Pischke's *Mostly Harmless Econometrics* or *Mastering ‘Metrics*; Morgan & Winship's *Counterfactuals and Causal Inference*
* **More R**: Wickam and Grolemund's [*R for Data Science*](https://r4ds.had.co.nz/index.html); Healy's [*Data Visualization*](https://socviz.co/); Shermann's [*A Reader on Data Visualization*](https://mschermann.github.io/data_viz_reader/)
* **AI tools**: ChatGPT, Claude, RTutor.ai
* **Data Science for Policy**: Harrell's *A Civic Technologist’s Practice Guide*; Kim's *Computational Thinking for Social Scientists*; Lane's *Democratizing our Data*; Salganick's [*Bit by Bit*](https://www.bitbybitbook.com/en/1st-ed/preface/); Weidmann's *Data Management for Social Sciences*; Pahlka's *Recoding America*

### Computation in R
All computation in this class will use the **R** statistical computing language. Any homework requiring R should be submitted using **Quarto** or **RMarkdown**. We strongly recommend using **RStudio**, an IDE for R. Advanced users or hybrid R/Python developers should look into Positron.
* To download/install R: <https://cran.r-project.org/>
* To download/install RStudio: <https://posit.co/downloads/>
* To download/install Quarto: <https://quarto.org/docs/download/>
* To download/install TinyTeX (for PDF rendering): <https://yihui.org/tinytex/r/>
* To download/install Positron (for advanced users): <https://positron.posit.co/download.html>

---
## Course Structure

This course will follow a “flipped” and hybrid format with analog, video, remote/online, and in-person components.

* **Individual Activities**: This includes reading, watching short lecture videos, listening to podcasts, and working on lab assignments. This work is expected to be completed prior to every large-group meeting.
* **Small Group Activities**: This includes meetings for your group projects. You can also take advantage of office hours, either individually or as small groups.
* **Large Group Activities**: These are our formal in-person class meetings. Some days will be short lectures, while others will be devoted to questions, case materials, guest speakers, or group work.

{: .warning }
**This class format will only work if everyone completes the individual work prior to group meetings.** Failure to do so will have negative effects on you and your colleagues. There may be a graded comprehension assessment at the beginning of some class meetings.

### Expectations
I expect that you will come to class **ON TIME** and prepared. In return, you can expect that I have selected the materials for a reason, will come prepared with a clear agenda, and will return all on-time assignments within a week.

### Email & Ed Forum policy
I will use email and the [Ed forum](https://edstem.org/us/courses/81870/discussion) regularly. I will do my best to respond to emails and messages within 24 hours. **I will NOT respond to correspondence during holidays or weekends.**

---
## Assignments & Grading

Your score is a weighted average of the following:

| Component                   | Weight | Type       |
| :-------------------------- | :----- | :--------- |
| Participation               | 10%    | Individual |
| Lab exercises               | 19%    | Individual |
| Assignment #1               | 5%     | Group      |
| Assignment #2               | 10%    | Group      |
| Assignment #3               | 25%    | Group      |
| Final Exam                  | 30%    | Individual |
| Office hours visits (minimum 2 required) | 1%     | Individual |

There will be no extra credit or supplemental assignments.

### Lab Exercises
Each lab session has an associated set of R exercises, due by **11:59 PM on the Monday** following the lab. A good faith attempt will receive an acceptable grade. No late exercises will be accepted. Lab exercises should be your individual work.


### Class Project and Assignments
The core group assignment uses data from the Labor Action Tracker (LAT) to build a predictive model for labor actions in the USA. You will either predict if an action is a "strike" or predict *where* an action will happen. We will randomly assign groups of 4-5 people.

* **Assignment #1: Ideal data and team plan.** Due 11:59 PM on October 3.
    * Describe your ideal dataset, compare it to the LAT data, and provide an explicit team plan for the quarter.
* **Assignment #2: Locating labor actions.** Due 11:59 PM on October 31.
    * Decide how to handle actions with multiple locations, use an LLM to help assign lat/long coordinates to counties, and create a new county variable in the LAT data.
* **Assignment #3: A data analysis report.** Due 8:00 AM on December 6.
    * A short report (max 4 pages/1500 words) summarizing your model, data adjustments, and conclusions. The report must be a cohesive `.pdf` produced with Quarto/RMarkdown, with all code embedded. An external party must be able to reproduce your report from your code.

### Final Exam
The final exam will be in class on **December 3**. It will cover conceptual, practical, and ethical issues from the course. The exam is closed-book, but you may use one 3”x5” card of hand-written notes.


---

### Groups
- Groups assigned by end of Week 2.
- Groups submit one response per assignment; all members receive the same grade.
- End-of-quarter peer evaluation: if a majority of your teammates indicate you did not contribute fairly, your group assignment grade will be reduced by **one full letter grade**.

---
## Course Rules

### Maintaining Academic Integrity
I take academic honesty seriously. You may discuss work with others, but all analytic work is expected to be your own. You must appropriately cite all sources. All suspected cases of academic dishonesty will be referred to the office of academic integrity.

All analytic work is expected to be your own, and all sources (data, code, text) must be properly cited.  
UCSD’s academic honesty policy: <http://academicintegrity.ucsd.edu/>  

Suspected violations will be referred to the Office of Academic Integrity (OAI). If you are unsure about proper citation, acceptable collaboration, or what constitutes plagiarism, ask before submitting work.


### Use of ChatGPT and other generative AI tools
Generative AI can be a helpful tool, but it poses challenges. Some assignments will require you to use it. When using AI, you are responsible for the accuracy, logic, and clarity of all content.

{: .warning }
**For every assignment, you must include an appendix with one of the following statements:**
1. "I/we certify that we did not use any LLM or generative AI tool in this assignment"
2. "I/we used \_\_\_\_\_\_\_\_\_\_ LLM/AI tool in this assignment."

If you disclose AI use, you must also state *why* you used it, reflect on whether it was helpful, and provide a link to the entire exchange. If disclosure is missing, it will be treated as undeclared AI use and reported to OAI. **AI tools are forbidden during in-class exams.**

When using generative AI tools, you may treat them as:

- **Collaborators** — interact with the AI conversationally, iteratively refining prompts and using the tool to help shape analysis or prose.
- **Sources** — use the AI to retrieve specific code snippets, summaries, or text that you adapt or integrate into your work.

Regardless of approach, **you bear full ethical responsibility** for:
- The **accuracy**, **relevance**, and **logical soundness** of all outputs you use
- The clarity and correctness of arguments, code, and interpretations
- **Accurate attribution** of ideas, quotations, and code to their original sources
- Ensuring that AI-generated content does not introduce plagiarism or violate academic integrity standards


## Submitting Written Work
- All written work must be `.pdf` files produced with Quarto or RMarkdown, **with all code embedded** in your `.qmd`/`.rmd` source file.
- **Do not** submit Google Docs, Word files, Excel sheets, or Stata output.
- All submissions will be checked via Turnitin.com for similarity detection; papers are included in Turnitin’s reference database for plagiarism prevention.

## Reproducibility Requirement
All group project work must be fully reproducible:
- An external reviewer should be able to run your code and produce your report without any extra setup.
- All analysis must be done in R (no Excel/Stata).
- No code should appear in the compiled `.pdf` report — only in the source file.


## Late Work & Make-Up Exams

- Late assignments lose **1 percentage point per hour** after the deadline.
- No work will be accepted more than **48 hours** after the deadline without a documented, university-approved excuse.

### Acceptable Excuses
Acceptable documented excuses include:
- Illness documented by **UCSD Health Services** or a licensed physician
- Death or serious illness in the immediate family
- Other circumstances recognized by **standing University policy**

### Employment-Related Travel
In **exceptional cases**, university-sanctioned employment-related travel may be accepted as a valid reason for late work or a missed exam.  
This exception applies **only** if:
- It is approved by the instructor **at least two weeks in advance**
- Documentation is provided verifying the official nature of the travel

### Make-Up Exams
There will be **no make-up exams** without an approved excuse as defined above.


### Grade disputes
To dispute a grade, you must submit a written memo of no more than 400 words explaining the error within seven calendar days of the assignment being returned.

## Group Work & Peer Evaluation
At the end of the quarter, you will evaluate your group members’ contributions.  
If a majority of your teammates indicate that you failed to contribute fairly, your group project grade will be reduced by **one full letter grade**.


## Students with Disabilities
Students requesting accommodations must provide a current Authorization for Accommodation (AFA) letter from the Office for Students with Disabilities (OSD).  
- OSD website: <http://disabilities.ucsd.edu>  
- Office: University Center 202 (behind Center Hall)  
Present your AFA letter privately **at least two weeks before an exam** so arrangements can be made.
