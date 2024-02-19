import json
import re
import os
from datetime import datetime
import tweepy
import configparser
import pandas as pd
import pprint

config = configparser.ConfigParser()
api_key = "vA2CQgSfgWCTjP3JZl2DoGktU"
api_key_secret = "1GzFnt3lTjnPUwPTrroy3Bu0BGDxPoTgcGWltE1FvvWdKsU3ES"
access_token = "1068257712373301248-Md7XJ7Dx2Toi2BjavV5jU3Pz8fmLGI"
access_token_secret = "EID1Dc2QQ8rocdpH1nTevppBLvm6HeHfFiNvSUQHHkvMk"

# auth = tweepy.OAuth1UserHandler(
#     api_key, api_key_secret, access_token, access_token_secret
# )
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# columns=['Time','User','Tweet']
# data=[]
# for tweet in public_tweets:
#     data.append([tweet.created_at,tweet.user.screen_name,tweet.text])

# df=pd.DataFrame(data,columns=columns)
# df.to_csv('tweets.csv')

# Get user information
user = api.verify_credentials()

# In tất cả thông tin tài khoản
pprint.pprint(user._json)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

columns = ["Time", "User", "Tweet"]
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)
df.to_csv("tweets.csv")
