# adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/tweepy.md

import os

from dotenv import load_dotenv
import tweepy

load_dotenv()

CONSUMER_KEY = os.environ.get("TWITTER_API_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_API_SECRET")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# AUTHENTICATE

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# INITIALIZE API CLIENT

client = tweepy.API(auth)

# ISSUE REQUESTS

user = client.me() # get information about the currently authenticated user

tweets = client.user_timeline() # get a list of tweets posted by the currently authenticated user

# PARSE RESPONSES

print("---------------------------------------------------------------")
print(f"RECENT TWEETS BY @{user.screen_name} ({user.followers_count} FOLLOWERS / {user.friends_count} FOLLOWING):")
print("---------------------------------------------------------------")

for tweet in tweets:
    created_on = tweet.created_at.strftime("%Y-%m-%d")
    print(" + ", tweet.id_str, created_on, tweet.text)
