import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')

    merged_table =  merged_table.rename(
                    columns = {
                            "id_x" : "employee_id",
                            "name_x" : "Employee_name",
                            "id_y" : "Department_ID",
                            "name_y": "Department_Name"
                                }
                    )
    merged_table['department_max_salary'] = merged_table.groupby("Department_Name")['salary'].transform('max')

    column_name_header = f'check_header'

    condition = (
        (merged_table['salary'] == merged_table['department_max_salary'])
    )

    merged_table =  merged_table.rename(
                    columns = {
                            "Department_Name" : "Department",
                            "Employee_name" : "Employee",
                            "salary" : "Salary",
                            
                                }
                    )


    return merged_table.loc[condition, ["Department", "Employee", "Salary"]]



"""
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')

    merged_table =  merged_table.rename(
                    columns = {
                            "id_x" : "employee_id",
                            "name_x" : "Employee_name",
                            "id_y" : "Department_ID",
                            "name_y": "Department_Name"
                                }
                    )

    return merged_table
"""