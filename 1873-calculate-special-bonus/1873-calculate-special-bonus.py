import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    bonus_condition = (
        (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith("M"))
    )

    employees['bonus'] = employees['salary'].where(bonus_condition, 0)

    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id', ascending = True)
    