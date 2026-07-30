import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    food_conditional = (
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    )
    
    return products.loc[food_conditional, ['product_id']]