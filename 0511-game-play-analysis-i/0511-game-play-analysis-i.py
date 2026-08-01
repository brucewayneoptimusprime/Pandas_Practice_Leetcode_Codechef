import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby("player_id", as_index = False).agg(
        first_login = ('event_date','min')
    ) 

    return result

    