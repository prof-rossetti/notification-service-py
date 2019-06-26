# adapted from:
# ... https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/tweepy.md
# ... https://www.geeksforgeeks.org/tweet-using-python/

import datetime
import os
import pprint

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



# ISSUE REQUEST(S)


# adapted from:
#  + https://stackoverflow.com/questions/27243819/how-to-get-tweets-of-a-particular-hashtag-in-a-location-in-a-tweepy
#  + https://stackoverflow.com/questions/44948628/how-to-take-all-tweets-in-a-hashtag-with-tweepy
#  + https://stackoverflow.com/a/25895602/670433

matching_tweets = tweepy.Cursor(client.search, q="cricket").items(25)

for t in matching_tweets:
    print(t.text) #> <class 'tweepy.models.Status'>
    print(t.created_at) #> datetime.datetime(2019, 6, 25, 5, 17, 33)
    #tags = t.entities["hashtags"]
    #print(tags)
    #print("--------------------------")
    breakpoint()

#breakpoint()


exit()


user = client.me() # get information about the currently authenticated user

time_now = datetime.datetime.now() # a way for us to implement status uniqueness to avoid subsequent tweets running into ... tweepy.error.TweepError: [{'code': 187, 'message': 'Status is a duplicate.'}]
time_now_formatted = str(time_now) #> '2019-03-13 16:41:26.282159'
status = f"An example tweet sent programmatically from https://github.com/prof-rossetti/notification-service-py at {time_now_formatted}"
response = client.update_status(status=status)

# PARSE RESPONSES

pp = pprint.PrettyPrinter(indent=4)

print("---------------------------------------------------------------")
print(f"TWEETING AS... @{user.screen_name} ({user.followers_count} FOLLOWERS / {user.friends_count} FOLLOWING)")
print("---------------------------------------------------------------")
print("RESPONSE:", type(response))
print("ID:", response.id_str)
print("TEXT:", response.text)
print("PROPERTIES:")
pp.pprint(dict(response._json))
