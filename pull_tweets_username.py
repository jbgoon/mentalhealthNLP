import twint
import pandas as pd

def pull_tweets_username(username):
    c = twint.Config()
    c.Username = username
    c.Limit = 500
    c.Since = "2018-01-01 00:00:00"
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)

    tweets_df = twint.storage.panda.Tweets_df
    try:
        tweets_df = tweets_df.tweet
        return tweets_df
    except:
        return []



def main():
       pull_tweets_username("ucdavis")


if __name__ == '__main__':
    main()