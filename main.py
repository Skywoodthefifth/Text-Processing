from logging import config
import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
api_key = "KlQVELT3mMnpTt1IrtTJ3ssgK"
api_key_secret = "qUUCNEqLQIio0Au1d0wjGHxn1YaXGlwl1uZ8JjJU0Mg3i5JpA6"
access_token = "940958115117244416-NhANUhypHA3MqKTjIQs3WrLhJxwlXub"
access_token_secret = "NUoUtkB4PzmYcR4aBcxLS6xJn7Zacrw86g6i4dHhBrf0z"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
# create dataframe
columns = ["Time", "User", "Tweet"]
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
    print(tweet.created_at)
    print(tweet.user.screen_name)
    print(tweet.text)

df = pd.DataFrame(data, columns=columns)

df.to_csv("tweets.csv")
