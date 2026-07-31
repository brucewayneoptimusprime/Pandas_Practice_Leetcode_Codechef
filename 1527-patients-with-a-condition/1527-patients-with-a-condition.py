import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r"(^| )DIAB1"

    condition = patients['conditions'].str.contains(
        pattern,
        na = False
    )

    return patients[condition]
    