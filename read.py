# Outdated script that we used to figure out twint. Refer to "pull_tweets" script for working function.

import twint
import pandas as pd

def pull_tweets(keyword, limit):
    # keyword = string for what to look for in tweets
    # limit = max # of tweets
    c = twint.Config()
    c.Search=keyword
    c.Limit = limit
    c.Lang = "en"
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)
    tweets_df = twint.storage.panda.Tweets_df
    tweets = tweets_df.tweet
    tweets.to_csv(keyword+"_tweets.csv")
    return tweets

def main():
    pull_