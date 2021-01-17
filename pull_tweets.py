

def pull_tweets_keyword(keyword, limit):
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
    pull_tweets("politics", 1000)

if __name__ == "__main__":
    main()