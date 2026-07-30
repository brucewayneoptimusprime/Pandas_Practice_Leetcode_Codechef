import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    new_table = pd.merge(
        customers, orders, left_on = 'id', right_on = 'customerId', how = 'left', suffixes = ("_customer", "_order")
        )

    
    new_table = new_table.rename(
        columns = 
        {
            "id_customer" : "customer_id",
            "id_order" : "order_id",
            "customerId" : "Orders_customer_id",
            "name" : "Customers"
        }
    )
    
  
    condition_to_filter = (
        (new_table['order_id'].isna()) | (new_table['customer_id'].isna())
    )

    

    return new_table.loc[condition_to_filter, ['Customers']]
    
    