import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_table_1 = pd.merge(orders, company, on = 'com_id', how = 'outer')
    merged_table_2 = pd.merge(merged_table_1, sales_person, on = 'sales_id', how = 'outer')

    merged_table_2 = merged_table_2.rename(
        columns = {
            "name_y" : "Salesperson_name",
            "name_x" : "Company_name"
        }
    )

    condition = (
        merged_table_2['Company_name'] != 'RED'
    )

    condition_to_find_sus_employees = (
        merged_table_2['Company_name'] == 'RED'

    )

    sus_employee_list = merged_table_2.loc[condition_to_find_sus_employees, ['Salesperson_name']]

     

    table_3 = merged_table_2.loc[condition, ['Salesperson_name','Company_name']]

    table_3.dropna(subset = ['Salesperson_name'], inplace = True)

    full_list = table_3['Salesperson_name']
    full_list_series = full_list.to_frame()

    sus_list = sus_employee_list['Salesperson_name']
    sus_list_series = sus_list.to_frame()

    left_only = full_list_series[~full_list_series['Salesperson_name'].isin(sus_list_series['Salesperson_name'])]

    left_only = left_only.rename(
        columns = {
            'Salesperson_name' : 'name'
        }
    )

    return left_only.drop_duplicates()
    #return sus_employee_list
    