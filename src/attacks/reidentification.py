"""
Basic record linkage attack using exact matching
on quasi-identifiers.
"""

import pandas as pd

def linkage_attack(private_df: pd.DataFrame, aux_df: pd.DataFrame):
    """
    Exact-match linkage on quasi-identifiers: age, zipcode, occupation.

    Returns:
      - matched_aux_records: number of auxiliary rows that matched at least one private row
      - unique_private_records_reidentified: number of unique private record_ids linked via matches
      - aux_match_rate: matched_aux_records / total_aux_records  (always in [0,1])
      - avg_private_matches_per_aux: how many private rows each matched aux row links to on average
    """
    keys = ["age", "zipcode", "occupation"]

    merged = pd.merge(aux_df.reset_index(names="aux_row_id"),
                      private_df,
                      on=keys,
                      how="inner")

    total_aux = len(aux_df)

    # How many aux rows found at least one match?
    matched_aux = merged["aux_row_id"].nunique()

    # How many unique private individuals were linked (re-identified)?
    unique_private = merged["record_id"].nunique()

    # Useful diagnostic: how ambiguous the linkage is
    avg_matches = (len(merged) / matched_aux) if matched_aux > 0 else 0.0

    return {
        "matched_aux_records": int(matched_aux),
        "total_aux_records": int(total_aux),
        "aux_match_rate": float(matched_aux / total_aux) if total_aux > 0 else 0.0,
        "unique_private_records_reidentified": int(unique_private),
        "avg_private_matches_per_aux": float(avg_matches),
    }

