import pandas as pd
from dateutil.parser import parse

def melt_years_to_date(df):
    """Convert wide year columns (1960, 1961...) to long format."""
    year_cols = [str(y) for y in range(1960, 2024)]
    return df.melt(
        #id_vars=["Country Name", "Country Code", "Indicator Code"],
        id_vars=["Country Name", "Country Code"],
        var_name="year",
        value_vars=year_cols,
        value_name="gdp"
    )

def clean_year_column(df):
    """Convert year strings to datetime objects."""
    df["year"] = pd.to_datetime(df["year"], format="%Y")
    return df
