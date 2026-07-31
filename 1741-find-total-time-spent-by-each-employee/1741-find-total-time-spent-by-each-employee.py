import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']
    result_grouped_by = employees.groupby(['emp_id', 'event_day'], as_index = False).agg(

        total_time = ('duration', 'sum')
    )

    result_grouped_by = result_grouped_by.rename(
        columns = {
            "event_day" : "day"
        }
    )
    return result_grouped_by[['day', 'emp_id', 'total_time']]