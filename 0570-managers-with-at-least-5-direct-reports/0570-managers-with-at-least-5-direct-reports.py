import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    intermediate_table = pd.merge(employee,employee, left_on = 'managerId', right_on = 'id', how = 'inner')

    intermediate_table = intermediate_table.rename(
            columns =
        {
            'name_x' : 'employee_name',
            'name_y' : 'manager_name',
            'id_y'   : 'manager_id'
        }
    )


    result = intermediate_table.groupby(['manager_id','manager_name'], as_index = False,dropna = False).agg(
        reporting_from_employee_count = ('employee_name', 'size')
    )

    condition = (
        result['reporting_from_employee_count'] >= 5
    )

    result = result.rename(
        columns ={
            "manager_name" : 'name',
        }
    )


    return result.loc[condition, ['name']]