import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['length_of_tweet'] = tweets['content'].str.len()

    

    return tweets.loc[(tweets['length_of_tweet']> 15), ['tweet_id']]
    