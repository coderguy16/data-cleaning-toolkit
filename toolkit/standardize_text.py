from fuzzywuzzy import process

def fix_country_names(df, valid_names):
    """Correct typos like 'United states' → 'United States'."""
    df["Country Code"] = df["Country Code"].apply(
        lambda x: process.extractOne(x, valid_names)[0]
    )
    return df

def standardize_indicator_codes(df):
    """Ensure codes like 'ny.gdp.mktp.cd' → 'NY.GDP.MKTP.CD'."""
    df["INDICATOR_CODE"] = df["INDICATOR_CODE"].str.upper()
    return df
