import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['ranking_score_wise'] = scores['score'].rank(method = 'dense', ascending = False)
    two_values = scores[['score','ranking_score_wise']].sort_values(by = 'ranking_score_wise', ascending = False)
    two_values_sorted = two_values.sort_values(by = 'ranking_score_wise', ascending = True)
    two_values_sorted = two_values_sorted.rename(
        columns = {
            "ranking_score_wise" : "rank"
        }
    )
    return two_values_sorted
    