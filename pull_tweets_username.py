import twint
import pandas as pd

def pull_tweets_username(username):
    c = twint.Config()
    c.Username = username
    c.Limit = 50
    c.Since = "2020-12-01 00:00:00"
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)

    tweets_df = twint.storage.panda.Tweets_df
    try:
        tweets_df = tweets_df.tweet
        return tweets_df
    except:
        print("there was an error")
        return 0



def main():
       pull_tweets_username("zxcvbnm")


if __name__ == '__main__':
    main()