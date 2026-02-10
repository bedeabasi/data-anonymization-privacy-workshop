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

