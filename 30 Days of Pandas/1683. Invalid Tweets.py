""" 
"""
import pandas as pd
data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(tweets[tweets.content.str.len()>15][['tweet_id']])

# 2nd Solution
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len()>15].drop(columns="content")
    
