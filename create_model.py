import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def process_text(sentence):
    # remove handles + sites
    remove_handle = re.sub(r'@[\w]+', '', sentence)
    remove_site = re.sub(r'(http\S+) | (www.\S+) | (\S+.com/\S+) | (\S+.com)', '', remove_handle)

    # remove dashes + special chars + nums (isalpha)
    dashless = remove_site.replace('-', ' ').replace('/', ' ')
    clean_sentence = re.sub(r'[^A-Za-z ]+', '', dashless)

    return clean_sentence


def clean_tweets(tweets_df):
    # loop through tweets in df
    tokens = []
    clean_tweet_list = []
    for index, row in tweets_df.iterrows():
        tweet = row[1]
        clean_tweet = process_text(tweet)

        word_list = clean_tweet.split(' ')
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
    feature_list = list(set(features.split(' ')))

    # tokenize both w tfidf
    vectorizer = TfidfVectorizer(vocabulary=feature_list, use_idf=True, lowercase=False)
    x_train_tfidf = vectorizer.fit_transform(x_train)
    x_test_tfidf = vectorizer.fit_transform(x_test)

    return x_train_tfidf, x_test_tfidf, y_train, y_test, feature_list


# build model (Naive Bayes, Logistic Bayes, Neural Network)
def naive_bayes(x_train, x_test, y_train, y_test):
    model = MultinomialNB().fit(x_train,y_train)
    accuracy = model.score(x_test, y_test)

    return accuracy, model


def is_concern(text):
    # get data
    data_site = pd.read_csv('combined_tweets.csv')
    depressed = data_site[data_site['label']==1]
    normal = data_site[data_site['label']==0]
    normal = normal.sample(n=len(depressed))
    frames = [depressed, normal]
    data_site = pd.concat(frames)
    data_site = data_site.sample(frac=1)
    processed = clean_tweets(data_site)

    # build model
    x_train, x_test, y_train, y_test, features = get_train_test(processed)
    accuracy, model = naive_bayes(x_train, x_test, y_train, y_test)

    # clean up input message
    clean_text = process_text(text)

    # vectorize input text with tfidf
    vectorizer = TfidfVectorizer(vocabulary=features, use_idf=True, lowercase=False)
    text_tfidf = vectorizer.fit_transform([clean_text])

    # classify text using model
    prediction = int(model.predict(text_tfidf))

    return prediction


def is_concern_array(string_list):
    # get data
    data_site = pd.read_csv('combined_tweets.csv')
    depressed = data_site[data_site['label'] == 1]
    normal = data_site[data_site['label'] == 0]
    normal = normal.sample(n=len(depressed))
    frames = [depressed, normal]
    data_site = pd.concat(frames)
    data_site = data_site.sample(frac=1)
    processed = clean_tweets(data_site)

    # build model
    x_train, x_test, y_train, y_test, features = get_train_test(processed)
    accuracy, model = naive_bayes(x_train, x_test, y_train, y_test)

    # clean up input message
    clean = []
    for i in string_list:
        clean_text = process_text(i)
        clean.append(clean_text)

    # vectorize input text with tfidf
    vectorizer = TfidfVectorizer(vocabulary=features, use_idf=True, lowercase=False)
    text_tfidf = vectorizer.fit_transform(clean)

    # classify text using model
    prediction = model.predict(text_tfidf)

    # calculate percent of items with concern
    count = 0
    for i in prediction:
        if i == 1:
            count += 1
    freq = count/len(prediction)

    return prediction, freq
