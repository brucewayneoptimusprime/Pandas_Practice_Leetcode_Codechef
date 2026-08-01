import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby("class",as_index = False).agg(
        count_of_students = ('student', lambda student: student.count())
    )
    
    conditional_filtering = (
        result['count_of_students'] >= 5
    )



    return result.loc[conditional_filtering, ['class']]