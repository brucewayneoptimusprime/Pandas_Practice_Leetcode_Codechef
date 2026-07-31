import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salary_sole_single_column_series = employee['salary'].drop_duplicates().sort_values(ascending = False).reset_index(drop=True)

    columname = f'getNthHighestSalary({N})'

    if len(salary_sole_single_column_series) < N or N <= 0:
        answer = None
    else:
        answer = salary_sole_single_column_series.iloc[N-1]

    return pd.DataFrame(
        {
            columname : [answer]
        }
    )