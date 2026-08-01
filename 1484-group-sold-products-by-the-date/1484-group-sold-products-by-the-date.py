import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    activities.drop_duplicates(subset = ['sell_date','product'], keep = "first", inplace = True)

    result = activities.groupby("sell_date", as_index = False).agg(
          num_sold = ('product','count'),
          products = ('product', lambda product : ",".join(sorted(product.unique()))) 
    )

    return result
    