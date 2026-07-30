import pandas as pd


def combine_two_tables(
    person: pd.DataFrame, address: pd.DataFrame
) -> pd.DataFrame:
    # Left merge person with address on personId
    merged = pd.merge(person, address, on="personId", how="left")

    # Select the required columns
    return merged[["firstName", "lastName", "city", "state"]]