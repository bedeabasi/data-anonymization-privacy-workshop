"""
Basic record linkage attack using exact matching
on quasi-identifiers.
"""

import pandas as pd


def linkage_attack(private_df, aux_df):
    """
    Performs exact matching linkage on:
    age, zipcode, occupation
    """

    merged = pd.merge(
        aux_df,
        private_df,
        on=["age", "zipcode", "occupation"],
        how="inner"
    )

    reidentified = merged["record_id"].nunique()
    total_aux = len(aux_df)

    rate = reidentified / total_aux

    return {
        "reidentified_records": reidentified,
        "total_aux_records": total_aux,
        "reidentification_rate": rate
    }
