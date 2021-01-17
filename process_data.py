import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# cleaning raw tweet data + tokenization
def clean_tweets(tweets_df):
    # loop through tweets in df
    tokens = []
    clean_tweet_list = []
    for index, row in tweets_df.iterrows():
        # remove handle + website
        tweet = row[1]
        remove_handle = re.sub(r'@[\w]+', '', tweet)
        remove_site = re.sub(r'http\S+', '', remove_handle)

        # remove special chars + nums (isalpha)
        alpha = re.sub(r'[^A-Za-z ]+', '', remove_site)

        word_list = alpha.split(' ')
        clean_list = []
        for word in word_list:
            if (word == '') or (word == '\n') or (word == '\t'):
                continue
            else:
                clean_list.append(word.lower())

        tokens.append(clean_list)
        clean_tweet_list.append(' '.join(clean_list))

    tweets_df['tokens'] = tokens
    tweets_df['clean_tweet'] = clean_tweet_list

    return tweets_df


# split into train and test
def get_train_test(tweets_df):
    # create column with clean tweet
    x_train, x_test, y_train, y_test = train_test_split(tweets_df['clean_tweet'], tweets_df['label'], test_size=0.3)

    # get train data features
    features = [tweet for tweet in x_train]
    features = ' '.join(features)
    unique = list(set(features.split(' ')))

    # tokenize both w tfidf
    vectorizer = TfidfVectorizer(vocabulary=unique, use_idf=True, lowercase=False)
    x_train_tfidf = vectorizer.fit_transform(x_train)
    x_test_tfidf = vectorizer.fit_transform(x_test)

    return x_train_tfidf, x_test_tfidf, y_train, y_test


# build model (Naive Bayes, Logistic Bayes, Neural Network)
# test accuracy, F1 (harmonic mean of precision/recall)
def naive_bayes(x_train, x_test, y_train, y_test):
    model = MultinomialNB().fit(x_train,y_train)
    predictions = model.predict(x_test)
    accuracy = model.score(x_test, y_test)

    return accuracy

########################################################################################################################


data = pd.read_csv(
    'https://raw.githubusercontent.com/viritaromero/Detecting-Depression-in-Tweets/master/sentiment_tweets3.csv')
processed = clean_tweets(data)
x_train, x_test, y_train, y_test = get_train_test(processed)
accuracy = naive_bayes(x_train, x_test, y_train, y_test)
print(accuracy)
