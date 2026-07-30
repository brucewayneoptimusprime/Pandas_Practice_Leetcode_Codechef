import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    condition_self_created = (
        (world['area'] >= 3000000) | (world['population'] >= 25000000)
    )

    result = world.loc[condition_self_created, ['name','population','area']]
    return result
    
    