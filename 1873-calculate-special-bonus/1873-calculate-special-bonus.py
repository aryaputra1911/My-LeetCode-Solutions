import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.loc[(employees["employee_id"] % 2 == 1) & (employees["name"].str[0] != "M")]
    join = pd.merge(employees, df, on = "employee_id", how = "left")
    return join[["employee_id", "salary_y"]].rename(columns={'salary_y': 'bonus'}).fillna(0).sort_values(by = "employee_id")
    