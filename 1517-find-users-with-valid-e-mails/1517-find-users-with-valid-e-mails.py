import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email_accepted_pattern = r"[A-Za-z][A-Za-z0-9_\-.]*@leetcode\.com"

    condition_email_matching = users['mail'].str.fullmatch(
        email_accepted_pattern,
        na = False
    )

    return users.loc[condition_email_matching]
    