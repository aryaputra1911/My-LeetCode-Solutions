import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df["name"] = df["name"].str.lower().str.capitalize()
    return df[["user_id", "name"]].sort_values(by = "user_id")
    