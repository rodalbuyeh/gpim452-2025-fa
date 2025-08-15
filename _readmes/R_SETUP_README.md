# R + Jupyter on macOS (with conda) — Quick README

Use this as a cheat sheet to get R working smoothly inside Jupyter (Lab/Notebook) on macOS using **conda**. The key idea: **launch R from the same terminal session (and conda env) that has Jupyter** so `IRkernel::installspec()` can find `jupyter`.

---

## 1) Prereqs
- **conda** (Miniconda or Anaconda) installed
- **R** installed (CRAN or Homebrew)
  - CRAN default binary (typical): `/Library/Frameworks/R.framework/Resources/bin/R`
  - Homebrew binary: `R` (on PATH after `brew install r`)

Optional but recommended:
- **JupyterLab** (or Notebook) installed in your conda env

---

## 2) Create or use a conda environment
```bash
# Create (example: "ds")
conda create -n ds python=3.11 -y
conda activate ds

# Install Jupyter in this env
conda install -c conda-forge jupyterlab -y
# (or) pip install jupyterlab
```

Verify:
```bash
jupyter --version
which jupyter          # should point inside your conda env, e.g., .../envs/ds/bin/jupyter
```

---

## 3) Launch R *from this same terminal*
One of the following usually works:
```bash
R
# or, if CRAN R isn't on PATH:
/Library/Frameworks/R.framework/Resources/bin/R
```
> You should now see the R prompt (`>`). You're still inside the activated conda env (`ds`).

---

## 4) Install and register the IRkernel (inside R)
```r
install.packages("IRkernel")
IRkernel::installspec(user = TRUE)  # registers the "R" kernel with Jupyter for your user
```

Check that R sees Jupyter:
```r
Sys.which("jupyter")
system("jupyter --version")
```

If `Sys.which("jupyter")` is empty or the system call returns code 127 ("command not found"), R can't see Jupyter—make sure you **opened R from the activated conda env** (Step 3).

---

## 5) Use it
From the **same** env:
```bash
jupyter lab       # or: jupyter notebook
```
- In the launcher, choose **R** as the kernel.
- To mix Python & R in one notebook, use `rpy2` from the Python side:
  ```bash
  pip install rpy2
  ```
  In a Python notebook cell:
  ```python
  %load_ext rpy2.ipython
  %%R
  x <- rnorm(10); mean(x)
  ```

---

## 6) Common troubleshooting
**Symptom:** `IRkernel::installspec()` -> “jupyter-client has to be installed but 'jupyter kernelspec --version' exited with code 127.”  
**Meaning:** R can't find the `jupyter` CLI.

**Fix path visibility** (inside R):
```r
# Quick check:
Sys.which("jupyter")
system("jupyter --version")

# Temporary PATH injection if needed (replace with your env path):
Sys.setenv(PATH = paste(Sys.getenv("PATH"), "/Users/YOU/miniconda3/envs/ds/bin", sep=.Platform$path.sep))
IRkernel::installspec(user = TRUE)
```

**Manual prefix install** (drops kernelspec under `<prefix>/share/jupyter/kernels/ir`):
```r
IRkernel::installspec(user = FALSE, prefix = "/Users/YOU/miniconda3/envs/ds")
```

**Multiple Python/Jupyter installs:** Ensure the one you want is **first on PATH** when starting R.

**Remove/reinstall kernelspec**:
```bash
jupyter kernelspec list
jupyter kernelspec remove ir
# Then re-run IRkernel::installspec() from R
```

---

## 7) Single-shot setup (copy/paste)
From a fresh Terminal:
```bash
# 1) Activate env with Jupyter
conda activate ds

# 2) Launch R from same shell
R -q <<'EOF'
install.packages("IRkernel", repos="https://cloud.r-project.org")
IRkernel::installspec(user = TRUE)
q(save="no")
EOF

# 3) Start Jupyter
jupyter lab
```

---

## 8) Notes & paths (macOS)
- Conda env binaries: `~/miniconda3/envs/<env>/bin/`
- CRAN R binary (system-wide): `/Library/Frameworks/R.framework/Resources/bin/R`
- Jupyter kernelspecs (user): `~/Library/Jupyter/kernels/`
- Jupyter kernelspecs (prefix): `<prefix>/share/jupyter/kernels/`

---

### TL;DR
1. `conda activate <env>` where Jupyter is installed.  
2. Start **R from that same terminal** (`R` or full CRAN path).  
3. In R: `install.packages("IRkernel"); IRkernel::installspec(user=TRUE)`  
4. Run `jupyter lab` and pick the **R** kernel.


### To run rise plugin...
1. Install requirements.txt
2. Use the rise magic stuff
3. Output the files to share, as follows: 

For regular html
```bash
jupyter nbconvert Untitled.ipynb \     
  --to html --template=lab \
  --output notebook \
  --HTMLExporter.embed_images=True
```

For fancy slides
```bash
jupyter nbconvert Untitled.ipynb \
  --to slides \
  --output slides.html \
  --template=lab \
  --SlidesExporter.reveal_url_prefix=https://unpkg.com/reveal.js@4 \
  --SlidesExporter.reveal_theme=white
```