import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    all_combinations = pd.merge(students, subjects, how = 'cross')

    result_first = pd.merge(students, examinations, left_on = 'student_id', right_on = 'student_id', how = 'outer')

    result_second = result_first.groupby(['student_id','student_name', 'subject_name'], as_index = False, dropna = False).agg(
        attended_exams = ('student_id', 'size')
    )

    more_weird_merge = pd.merge(all_combinations, result_second, on = ['student_id', 'student_name', 'subject_name'] , how = 'left')

    more_weird_merge['attended_exams'] = more_weird_merge['attended_exams'].fillna(0)


    more_weird_merge.sort_values(by = ['student_id', 'subject_name'], ascending = [True, True], inplace = True)

    return more_weird_merge
    