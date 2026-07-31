import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    low_salary_condition = (
        accounts['income'] < 20000
    )

    average_salary_condition = (
        (accounts['income'] <= 50000) & (accounts['income'] >= 20000)
    )

    high_salary_condition = (
        accounts['income'] > 50000
    )
    
        
    return pd.DataFrame(
        {
            "category" : ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count" : [low_salary_condition.sum(), average_salary_condition.sum(),  high_salary_condition.sum()]
        }
    )



    