import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby("teacher_id",as_index = False).agg(
        cnt = ("subject_id",'nunique')
    )
    
    return result