import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employees, employee_uni, left_on = 'id', right_on = 'id', how = "outer")
    result.sort_values(by = 'name', ascending = True, inplace = True)
    result.dropna(subset = ['name'], inplace = True)
    return result[['unique_id','name']]
    