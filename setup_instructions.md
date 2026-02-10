# Workshop Setup Instructions

Follow these steps carefully before the first session.

---

## Step 1: Install Git

Check if Git is installed:

```bash
git --version
```

If Git is not installed, download and install it from:

https://git-scm.com/downloads

After installation, reopen your terminal and re-run:

```bash
git --version
```

---

## Step 2: Install Conda (Miniconda Recommended)

This workshop uses Conda to manage the Python environment.

Download Miniconda for your operating system:

https://docs.conda.io/en/latest/miniconda.html

After installation, verify Conda is available:

```bash
conda --version
```

---

## Step 3: Clone the Workshop Repository

In your terminal, navigate to a directory where you want to store the workshop files, then run:

```bash
git clone <REPO_URL>
```

Replace `<REPO_URL>` with the GitHub repository link provided to you.

Move into the project directory:

```bash
cd data-anonymization-privacy-workshop
```

---

## Step 4: Create the Conda Environment

Create the environment using the provided configuration file:

```bash
conda env create -f setup/environment.yml
```

Activate the environment:

```bash
conda activate privacy-workshop
```

Confirm the environment is active:

```bash
python --version
```

---

## Step 5: Launch Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Your web browser should open automatically.  
If not, copy and paste the URL shown in the terminal into your browser.

In the Jupyter interface, open the `notebooks/` folder.

---

## Step 6: Verify Your Setup

Open the notebook:

```
notebooks/session1_reidentification.ipynb
```

Run the first cell.

If the cell runs without errors, your setup is complete.

---

## Common Troubleshooting

### Conda environment creation fails

Try updating Conda:

```bash
conda update conda
```

Then re-run **Step 4**.

### Jupyter command not found

Try:

```bash
python -m notebook
```

### Environment not activating

Make sure you activated the correct environment:

```bash
conda activate privacy-workshop
```

---

## Important Notes

- Do **not** modify the datasets unless instructed.
- All datasets used in this workshop are **synthetic**.
- If you encounter issues you cannot resolve, bring the **full error message** to the first session.

---

## Prerequisites Checklist (Before Day 1)

Before attending the first session, make sure you can confirm **all** of the following:

- [ ] Git is installed (`git --version` works)
- [ ] Conda is installed (`conda --version` works)
- [ ] The `privacy-workshop` environment activates successfully
- [ ] Jupyter Notebook launches without errors
- [ ] You can open and run `session1_reidentification.ipynb`

If **any** item fails, resolve it **before** the first session.

---

## Repository Structure

After cloning the repository, your directory should look like this:

```
data-anonymization-privacy-workshop/
├── README.md
├── setup/
│   └── environment.yml
├── notebooks/
│   ├── session1_reidentification.ipynb
│   ├── session2_k_anonymity.ipynb
│   └── session3_differential_privacy.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── anonymization/
│   └── attacks/
└── results/
```

If your structure differs significantly, you may have cloned the repository incorrectly.

---

## Environment Details

This workshop uses a **dedicated Conda environment** to ensure consistency across systems.

- Python version: **3.9**
- Core libraries:
  - NumPy
  - Pandas
  - Scikit-learn
  - Matplotlib
  - Jupyter
  - Seaborn

All dependencies are pinned in:

```
setup/environment.yml
```

Do **not** install additional packages unless explicitly instructed.

---

## Workshop Flow Overview

Each session follows the same structure:

1. **Conceptual overview** (threat model, assumptions, risks)
2. **Hands-on notebook walkthrough**
3. **Attack or evaluation**
4. **Discussion of failures and tradeoffs**

Sessions build on each other — skipping earlier notebooks is **not recommended**.

---

## Rules of Engagement

To ensure everyone has a smooth experience:

- Do **not** rename notebooks or folders
- Do **not** hardcode absolute file paths
- Run notebooks **top to bottom**
- Ask questions when something breaks — debugging is part of the learning

---

## Common Issues and Fixes

### Kernel not found in Jupyter

Select the correct kernel manually:

```
Kernel → Change Kernel → privacy-workshop
```

### Notebook runs slowly

- Close unused applications
- Restart the kernel:
  ```
  Kernel → Restart Kernel and Clear Output
  ```

### Package import errors

Reinstall the environment:

```bash
conda deactivate
conda env remove -n privacy-workshop
conda env create -f setup/environment.yml
conda activate privacy-workshop
```

---

## Academic Integrity Notice

This workshop is for **educational and research purposes only**.

- Do not attempt re-identification on real or proprietary datasets
- Do not reuse workshop code for unauthorized data analysis
- Follow your institution’s ethical research guidelines

---

## Getting Help

If you are stuck:

1. Copy the **full error message**
2. Note which step you were on
3. Bring both to the session or office hours

Vague descriptions like “it doesn’t work” will slow things down.

---

You are fully prepared.
