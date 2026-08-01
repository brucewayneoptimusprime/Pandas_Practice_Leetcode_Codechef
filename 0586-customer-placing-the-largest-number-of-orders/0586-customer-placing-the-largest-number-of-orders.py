import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number', as_index = False).agg(
        number_of_orders = ('order_number', "count")
    )

    condition = (
        result['number_of_orders'] == result['number_of_orders'].max() 
    )

    return result.loc[condition, ['customer_number']]
    