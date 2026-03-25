# Workshop Setup Instructions

Follow these steps carefully before the first session.

If you have never used Git, Conda, or Jupyter before, do not worry. Just follow the steps exactly as written.

---

# Step 1: Install Git

Git allows you to download the workshop code.

### Check if Git is already installed

Open a terminal:

- **Windows:** Open *Anaconda Prompt* or *PowerShell*
- **macOS:** Open *Terminal*
- **Linux:** Open your terminal

Type:

```bash
git --version
```

If you see a version number (for example, `git version 2.40.0`), Git is installed.

If you see an error, download Git from:

https://git-scm.com/downloads

Install it using the default options.

After installation, close and reopen your terminal and run:

```bash
git --version
```

---

# Step 2: Install Conda (Miniconda Recommended)

Conda manages the Python environment so everyone uses the same setup.

Download Miniconda:

https://docs.conda.io/en/latest/miniconda.html

Install it using default settings.

After installation:

- **Windows:** Open *Anaconda Prompt*
- **macOS/Linux:** Restart your terminal

Verify installation:

```bash
conda --version
```

You should see something like:

```
conda 23.x.x
```

If not, restart your terminal and try again.

---

# Step 3: Download (Clone) the Workshop Repository

Choose a location where you want the workshop folder to live (for example, your Desktop).

In your terminal, type:

```bash
cd Desktop
```

Then run:

```bash
git clone https://github.com/bedeabasi/data-anonymization-privacy-workshop.git
cd data-anonymization-privacy-workshop
```

You have now downloaded the workshop code.

---

# Step 4: Confirm You Are in the Correct Folder

Type:

```bash
pwd
ls
```

You should see folders like:

```
src
data
notebooks
setup
```

If you do not see these, you are not inside the correct folder.

---

# Step 5: Create the Workshop Environment

Now create the Python environment:

```bash
conda env create -f setup/environment.yml
```

This may take several minutes. That is normal.

---

# Step 6: Activate the Environment

Activate it:

```bash
conda activate privacy-workshop
```

Your terminal should now look something like:

```
(privacy-workshop) yourname@computer
```

That means the environment is active.

---

# Step 7: Verify Python Is Correct

Check that Python is coming from the workshop environment.

On macOS/Linux:

```bash
which python
```

On Windows:

```bash
where python
```

The path should contain:

```
privacy-workshop
```

If it does not, the environment is not active.

---

# Step 8: Start Jupyter Notebook

Launch Jupyter:

```bash
jupyter notebook
```

Your web browser should open automatically.

If it does not:
- Copy the URL shown in the terminal
- Paste it into your browser

---

# Step 9: Open the Session 1 Notebook

In the browser:

1. Click the `notebooks` folder
2. Click `session1_reidentification.ipynb`

Run the cells **from top to bottom** by clicking each cell and pressing:

```
Shift + Enter
```

If setup is correct, you should see:

- Private dataset shape: (1000, 5)
- Auxiliary dataset shape: (600, 3)
- Re-identification results printed successfully

---

# Optional: If Datasets Are Missing

If the folder `data/raw/` is empty, generate the datasets:

```bash
python src/generate_datasets.py
```

Then reopen the notebook.

---

# Common Beginner Issues

## Conda not recognized

You may be using the wrong terminal.

- Windows → Use *Anaconda Prompt*
- macOS/Linux → Restart terminal

---

## ModuleNotFoundError

Make sure:

```bash
conda activate privacy-workshop
```

Then restart the notebook kernel:

```
Kernel → Restart Kernel
```

---

## File Not Found Errors

Make sure you started Jupyter from inside:

```
data-anonymization-privacy-workshop
```

Not from your home directory.

---

## Notebook seems frozen

Restart the kernel:

```
Kernel → Restart Kernel and Clear Output
```

Then run cells again.

---

# Before the First Session Checklist

Make sure you can confirm ALL of the following:

- [ ] `git --version` works
- [ ] `conda --version` works
- [ ] `conda activate privacy-workshop` works
- [ ] `jupyter notebook` opens in your browser
- [ ] You can run all cells in `session1_reidentification.ipynb` without errors

If any item fails, fix it before the session.

---

# Important Rules

- Do not rename folders.
- Do not change file paths.
- Always run notebooks from top to bottom.
- If something breaks, copy the FULL error message.

---

You are ready for the workshop.
