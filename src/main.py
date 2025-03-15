import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from toolkit.clean_dates import melt_years_to_date, clean_year_column
from toolkit.deduplicate import merge_country_duplicates
from toolkit.standardize_text import fix_country_names, standardize_indicator_codes
if __name__ == "__main__":

    # Load messy data
    data_directory = os.path.join(os.getcwd(), 'data')

    gdp = pd.read_csv(
        os.path.join(data_directory, "gdp_time_series.csv"),
        skiprows=4,                  # Skip first 4 metadata rows
        header=0,                    # Treat the 5th line as the header
        na_values=[""],              # Treat empty strings as NaN
        thousands=",",               # Handle numbers like "405,586,592"
        dtype={"Country Code": str}   # Preserve leading zeros in codes
    )


    # Drop unnamed columns
    gdp = gdp.drop(columns=[col for col in gdp.columns if "Unnamed" in col])


    metadata = pd.read_csv(os.path.join(data_directory, "country_metadata.csv"))

    indicators = pd.read_csv(os.path.join(data_directory, "indicator_metadata.csv"))

    # Clean Table 1: GDP Data
    gdp_long = melt_years_to_date(gdp)


    gdp_long = clean_year_column(gdp_long)

    # Clean Table 2: Country Metadata
    valid_countries = metadata["Country Code"].unique()
    metadata = fix_country_names(metadata, valid_countries)

    # Merge & Deduplicate
    merged = merge_country_duplicates(gdp_long, metadata)

    # Clean Table 3: Indicators
    indicators = standardize_indicator_codes(indicators)

    # Save cleaned data
    os.makedirs("output", exist_ok=True)
    output_path = os.path.join(os.getcwd(), "output", "cleaned_gdp.csv")
    merged.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
