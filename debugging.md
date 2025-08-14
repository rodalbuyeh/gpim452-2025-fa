---
layout: page
title: Debugging
description: Pointers on how to solve common technical issues in R, RStudio, and Quarto.
nav_order: 5
---

# 🐞 Debugging (R / RStudio / Quarto)
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This page collects fixes for common issues in **R**, **RStudio**, and **Quarto/R Markdown** used in this course.

{: .note }
If something breaks, try this **5-step triage** first:
1) **Session → Restart R** (Ctrl/Cmd + Shift + F10)  
2) **Run all chunks top-to-bottom** (Render)  
3) Verify **packages are loaded** (`library(...)`)  
4) Check **paths** (use `here::here()`; never rely on the current working directory)  
5) Read the **last line** of the error—it’s usually the most informative.

---

## Chunks, Execution Order, and Rendering

### “It worked before, now it fails.” / “Object not found.”
You likely ran chunks **out of order** or edited a variable above.  
**Fix:** `Session → Restart R`, then **Render** (`Quarto: Render` or `Rmd: Knit`, Ctrl/Cmd + Shift + K). The grader (and TAs) will run your document **top to bottom**, so you should too.

### “My output is different each time.”
Set a **seed** near the top of your document:
```r
set.seed(123)
```
For modeling/evaluation, also set seeds in packages that support it.

### “How do I run everything quickly?”
- **Quarto**: Click **Render** (or Ctrl/Cmd + Shift + K).
- **R Markdown**: Click **Knit** (or Ctrl/Cmd + Shift + K).
- In the editor, you can also **Run All Chunks Above** to re-execute progressively.

---

## Packages & Libraries

### `could not find function "xyz"`  
You likely forgot to attach the package:
```r
library(dplyr)   # before using dplyr::mutate()
```
Or call explicitly:
```r
dplyr::mutate(...)
```

### `there is no package called 'pkg'`
Install, then attach:
```r
install.packages("pkg", dependencies = TRUE)
library(pkg)
```

### “Package failed to install / compile” (Windows/macOS)
- **macOS:** Install **Xcode Command Line Tools** (`xcode-select --install`) if compilation is needed.
- **Windows:** Install **Rtools** appropriate for your R version.
- If a source build fails, try installing the **binary** (default on Windows/macOS), or update R to a recent version.

### “Conflicts / masked objects” (e.g., `filter()` vs `stats::filter`)
Be explicit:
```r
dplyr::filter(...)
```
Check conflicts after `library(tidyverse)`.

### Locking versions for reproducibility
Consider **renv**:
```r
install.packages("renv")
renv::init()     # snapshot package versions for the project
```

---

## Paths, Data, and Project Structure

### `cannot open file 'data/file.csv': No such file or directory`
Your working directory isn’t what you think. Use **RStudio Projects** and **relative paths** with `here`:
```r
install.packages("here")
library(here)
readr::read_csv(here::here("data", "file.csv"))
```
{: .warning }
Avoid `setwd()` in notebooks. It breaks reproducibility.

### “My join exploded / duplicated rows”
Check for duplicates in keys **before** joining:
```r
dplyr::count(df, key, sort = TRUE)
```
If keys aren’t unique, understand whether you expect a one-to-one, one-to-many, or many-to-many join.

### Factor vs character mismatches in joins
Align types first:
```r
df$key <- as.character(df$key)
```

---

## Data Types & Common Errors

### `non-numeric argument to binary operator`
You tried math on a **character** column. Convert:
```r
df$x <- as.numeric(df$x)  # watch for NAs introduced by coercion
```
Prefer reading with **readr** and specifying types or using `readr::parse_number()`.

### `NAs introduced by coercion`
Check what failed to parse:
```r
readr::problems(your_tbl)
```

### `unused argument (...)` or `object is not subsettable`
You may be calling the wrong function or using the wrong object type. Inspect:
```r
class(x)
str(x)
```
and confirm the function signature (`?function_name`).

### `Error in ... : cannot allocate vector of size ...` (memory)
- Import selectively (`readr::cols_only(...)`, `col_select=`).
- Filter earlier, sample a subset, or work with **Arrow**/**DuckDB** for larger-than-memory data.
- Remove unused objects and restart R.

---

## dplyr / tidyr “gotchas”

### `summarise()` and grouping
From dplyr 1.1+, summarise uses `.groups` rules. If results look odd, set explicitly:
```r
df %>%
  group_by(group) %>%
  summarise(x = mean(x), .groups = "drop")
```

### Across / where helpers
If a verb “can’t find column” after using `across()`, ensure you’re in a **data-masking** context (inside `mutate/summarise`) and column names are correct.

---

## Quarto / R Markdown Rendering

### “Knit/Render fails” and mentions **LaTeX**
Install **TinyTeX** (lightweight TeX distribution):
```r
tinytex::install_tinytex()
```
Re-render. If issues persist, render to **HTML** to isolate whether LaTeX is the culprit.

### “pandoc not found”
Install **Quarto** (includes Pandoc) and use RStudio ≥ recent:
- Quarto: https://quarto.org  
- After install, restart RStudio.

### Hide code in the compiled PDF (per course policy)
Use `echo: false` in YAML or at the chunk level:
```yaml
---
title: "Report Title"
format:
  pdf:
    keep-tex: false
execute:
  echo: false
  warning: false
  message: false
---
```
Code remains in the **source** (`.qmd`/`.Rmd`) but not in the compiled PDF.

### Cache slow chunks safely
```yaml
execute:
  cache: true
```
Remember to **clear cache** if stale results appear.

---

## Plotting & Graphics

### Plots don’t show, or figures too large/small
Set chunk options:
```{r}
#| fig-width: 7
#| fig-height: 4
#| fig-align: "center"
```

### Non-ASCII fonts / PDF errors
Prefer base fonts or install system fonts and use **showtext**. If PDF still fails, render HTML first to debug.

---

## Reproducibility & “Session Info”

Include a **Session Info** appendix to capture versions:
```r
sessionInfo()
# or
devtools::session_info()
```
Set seeds, fix paths with `here`, lock packages with `renv`, and render from a clean session.

---

## Minimal Reproducible Examples (Getting Help)

When asking on Ed or in office hours, provide a **minimal reproducible example** (“reprex”): the smallest data + code that still triggers the error.
```r
install.packages("reprex")
reprex::reprex({
  library(dplyr)
  tibble(x = c("1","2","a")) |> 
    mutate(x = as.numeric(x))
})
```
Include: the error message, the code, and what you expected.

---

## Common RStudio Actions (Cheat Sheet)

- **Restart R:** Session → Restart R (Ctrl/Cmd + Shift + F10)  
- **Render (Quarto) / Knit (Rmd):** Ctrl/Cmd + Shift + K  
- **Run selection / line:** Ctrl/Cmd + Enter  
- **Find file paths:** Use `here::here("data", "file.csv")`  
- **Clear environment:** Broom icon in **Environment** pane (but prefer Restart R)  

---

## Appendix: Typical Fixes by Message

- **`Error: object 'foo' not found`** → Re-run chunks above; did you create `foo`?  
- **`could not find function "bar"`** → `library(pkg)` or `pkg::bar()`  
- **`there is no package called 'pkg'`** → `install.packages("pkg", dependencies=TRUE)`  
- **`NAs introduced by coercion`** → Column is not numeric; parse/clean then convert  
- **`cannot allocate vector of size`** → Import less, filter early, use Arrow/DuckDB, restart R  
- **`unused argument (xyz = ...)`** → Wrong function or version; check `?function_name`  
- **Join produced too many rows** → Check duplicate keys; confirm join type  
- **LaTeX error / missing fonts** → Install `tinytex`; try HTML; simplify figures  

---

If you hit something thorny, grab a screenshot of the exact **error text**, include your YAML header, the **few lines above** the failing chunk, and your **session info**—that context almost always reveals the fix.
