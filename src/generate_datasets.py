"""
Generate synthetic datasets for the privacy workshop.

Creates:
- A private dataset (contains sensitive attributes)
- A public auxiliary dataset (used for linkage attack)
"""

import os
import random
import numpy as np
import pandas as pd

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

OUTPUT_DIR = "../data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_private_dataset(n=1000):
    """Generate synthetic private dataset."""
    df = pd.DataFrame({
        "record_id": range(n),
        "age": np.random.randint(18, 70, size=n),
        "zipcode": np.random.choice(
            ["27284", "27401", "27514", "27606", "27707"], size=n
        ),
        "occupation": np.random.choice(
            ["Engineer", "Teacher", "Nurse", "Student", "Analyst"], size=n
        ),
        "disease": np.random.choice(
            ["Diabetes", "Hypertension", "Cancer", "None"], size=n
        )
    })

    return df


def generate_auxiliary_dataset(private_df, overlap_ratio=0.6):
    """
    Generate auxiliary dataset with partial overlap.
    Contains only quasi-identifiers.
    """
    n_overlap = int(len(private_df) * overlap_ratio)

    overlap_df = private_df.sample(n=n_overlap, random_state=SEED)

    aux_df = overlap_df[["age", "zipcode", "occupation"]].copy()

    return aux_df


def main():
    private_df = generate_private_dataset()
    aux_df = generate_auxiliary_dataset(private_df)

    private_df.to_csv(os.path.join(OUTPUT_DIR, "private_dataset.csv"), index=False)
    aux_df.to_csv(os.path.join(OUTPUT_DIR, "auxiliary_dataset.csv"), index=False)

    print("Datasets generated successfully.")
    print("Private dataset shape:", private_df.shape)
    print("Auxiliary dataset shape:", aux_df.shape)


if __name__ == "__main__":
    main()
