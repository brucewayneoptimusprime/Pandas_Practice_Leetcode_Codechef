import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    condition = (
        views['author_id'] == views['viewer_id']
    )

    table_1 = views.loc[condition, ['author_id']]
    table_1 = table_1.drop_duplicates(subset = ['author_id'])

    table_1 = table_1.sort_values(by = 'author_id', ascending = True)

    table_1 = table_1.rename(
        columns= {
            "author_id" : "id"
        }
    )

    return table_1