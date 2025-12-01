# GPIM 452: Big Data for Policy, Government, and Management

[![Course Website](https://img.shields.io/badge/Website-Live-blue)](https://rodalbuyeh.github.io/gpim452-2025-fa/)
[![Jekyll](https://img.shields.io/badge/Built%20with-Jekyll-red)](https://jekyllrb.com/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This repository contains the complete course website for **GPIM 452: Big Data for Policy, Government, and Management**, taught at UC San Diego in Fall 2025.

## 📚 About This Course

GPIM 452 is an advanced, hands-on data science course designed for policy students. The course provides an introduction to the logic and practice of data science as used in policy making, program evaluation, and corporate enterprise, with extensive work in R.

**Key Topics:**
- Data manipulation, wrangling, and visualization in R
- Working with high-dimensional and large-scale data
- Machine learning for predictive policy modeling
- Web scraping, APIs, and modern data collection
- Ethics in data science and algorithmic decision-making
- AI-augmented analysis and LLM integration

**Duration:** 10 weeks (Fall 2025)

## 🌐 Course Website

The live course website is available at: **[https://rodalbuyeh.github.io/gpim452-2025-fa/](https://rodalbuyeh.github.io/gpim452-2025-fa/)**

The site includes:
- Full syllabus and course policies
- Weekly schedules with readings and videos
- Lecture slides (Quarto reveal.js presentations)
- Lab materials and assignments
- Resource guides for R, Python, and data science tools
- Links to Gradescope, Campuswire, and office hours

## 📂 Repository Structure

```
.
├── _lectures/           # Quarto lecture slides (.qmd) and rendered HTML
│   ├── images/          # Lecture graphics and diagrams
│   └── lec*.qmd         # Source files for each lecture
├── _modules/            # Weekly schedule markdown files
├── lab_materials/       # R lab exercises and datasets
│   ├── R/               # Lab .qmd files and PDFs
│   └── data/            # Raw and processed data
├── _layouts/            # Jekyll HTML templates
├── _includes/           # Reusable Jekyll components
├── _sass/               # Custom CSS (bluecsd theme)
├── _staffers/           # Instructor bio pages
├── assets/              # Images and media
├── syllabus.md          # Complete course policies
├── assignments.md       # Assignment details and feature store
├── resources.md         # Links to R/Python learning resources
├── calendar.md          # Google Calendar embed
└── _config.yml          # Jekyll site configuration
```

## 🛠️ Tech Stack

This site is built with:
- **[Jekyll](https://jekyllrb.com/)** - Static site generator
- **[Just the Docs](https://just-the-docs.com/)** - Clean documentation theme
- **[Quarto](https://quarto.org/)** - For lecture slides and student reports
- **[GitHub Pages](https://pages.github.com/)** - Hosting
- **R/RStudio** - All course computation

## 💻 Development Workflow

### Option 1: Hybrid Workflow (Recommended)

**Best for:** Editing locally + reliable testing in the cloud

1. **Edit locally with your preferred editor**
   - Make changes to course content, lectures, etc.
   - Commit and push to GitHub

2. **Test in GitHub Codespaces**
   - Go to the GitHub repository
   - Click **Code** → **Codespaces** → **Create codespace**
   - In the Codespace terminal:
     ```bash
     bundle install
     bundle exec jekyll serve --host 0.0.0.0
     ```
   - Codespaces will automatically forward port 4000
   - View the site in your browser

**Benefits:**
- No local dependency management
- Clean Linux environment
- Free tier (120 core-hours/month)
- Best of both worlds

### Option 2: Local Development

**⚠️ Note:** Apple Silicon (M1/M2/M3) users may encounter gem compilation issues. Codespaces is recommended.

1. Install Jekyll dependencies:
   ```bash
   bundle install
   ```

2. Start local server:
   ```bash
   bundle exec jekyll serve
   ```

3. View at [http://localhost:4000](http://localhost:4000)

**Troubleshooting:**
- If you get a "webrick" error: `bundle add webrick`
- On Apple Silicon compilation errors: use Codespaces instead
- Version conflicts: delete `Gemfile.lock` and re-run `bundle install`

See [`_readmes/README.md`](_readmes/README.md) for detailed setup instructions.

## 📝 Making Updates

### Adding/Editing Lectures

1. Create or edit `.qmd` files in `_lectures/`
2. Render to HTML with Quarto:
   ```bash
   quarto render _lectures/lec01_intro.qmd
   ```
3. Commit both `.qmd` and `.html` files

### Updating Weekly Schedule

Edit the corresponding file in `_modules/` (e.g., `week-01.md`)

### Modifying Syllabus or Assignments

Edit `syllabus.md` or `assignments.md` directly in the root directory

## 🎓 Course Project

Students work in groups on the **Labor Action Tracker (LAT)** project, building predictive models to forecast labor strikes and actions across the US using:
- Cornell ILR's Labor Action Tracker data
- Feature augmentation with Census, IRS, and deprivation indices
- Machine learning techniques (regularization, trees, ensembles)
- Reproducible Quarto reports

## 📖 Key Learning Outcomes

By the end of this course, students can:
- Practice good computing workflow and project management
- Ingest data from files, APIs, and web scraping
- Clean, merge, and visualize high-dimensional data
- Apply dimensionality reduction techniques
- Train, validate, and evaluate predictive models
- Produce reproducible reports with Quarto/RMarkdown
- Work effectively in data-driven policy teams
- Integrate AI tools ethically and transparently

## 📜 License & Usage

Course materials are shared for educational purposes. If you adapt this course structure or materials:
- Please attribute the original source
- Share improvements back to the community
- Respect academic integrity in student-facing materials

## 🔗 Links

- **Course Website:** [https://rodalbuyeh.github.io/gpim452-2025-fa/](https://rodalbuyeh.github.io/gpim452-2025-fa/)
- **Theme Documentation:** [Just the Docs](https://just-the-docs.com/)
- **Quarto Documentation:** [quarto.org](https://quarto.org/)


---

**Last Updated:** December 2025

