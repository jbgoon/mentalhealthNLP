import twint
import pandas as pd

c = twint.Config()
c.Search="great"
c.Limit = 10
c.Pandas = True
c.Hide_output = True
twint.run.Search(c)

tweets_df = twint.storage.panda.Tweets_df

print(tweets_df.tweet)
