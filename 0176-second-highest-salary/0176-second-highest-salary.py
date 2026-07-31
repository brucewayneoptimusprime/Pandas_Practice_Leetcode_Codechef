import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(by = 'salary', ascending = False).reset_index(drop=True)

    salary_sole_column = employee['salary']

    salary_sole_column = salary_sole_column.drop_duplicates()

    column_name = f'SecondHighestSalary'

    if len(salary_sole_column) < 2:
        result = None
    else:
        result = salary_sole_column.iloc[1]

    return pd.DataFrame(
        {
            column_name : [result]
        }
    )