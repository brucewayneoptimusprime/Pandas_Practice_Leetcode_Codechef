import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director.drop_duplicates(inplace = True)

    
    result = actor_director.groupby(['actor_id','director_id'], as_index = False).agg(
            pair_count = ('actor_id', 'size')
    )

    condition = (

        result['pair_count'] >= 3

    )
    
    return result.loc[condition, ['actor_id','director_id']]