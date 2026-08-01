import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales.drop_duplicates(inplace = True)
    result = daily_sales.groupby(['date_id', 'make_name'], as_index = False).agg(
        unique_leads = ("lead_id", lambda lead_id : lead_id.nunique()),
        unique_partners = ("partner_id", lambda partner_id : partner_id.nunique())

    )
    
    return result