import pandas as pd

def merge_country_duplicates(df, metadata_df):
    """Fix country code mismatches using Table 2 metadata."""
    # Merge Table 1 GDP data with Table 2 metadata
    merged = pd.merge(
        df,
        metadata_df[["Country Code", "Region", "IncomeGroup"]],
        on="Country Code",
        how="left"
    )
    # Remove duplicates (e.g., USA vs US)
    return merged.drop_duplicates(subset=["Country Code", "year"])
