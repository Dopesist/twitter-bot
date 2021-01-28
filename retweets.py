import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

twt_lst = api.favorites(screen_name='Dopesist',count=5)
# print(twt_lst)

# print tweets id
# for tweet in twt_lst:
#     print(tweet.id)

# Retweet tweets id

# twt_id = 1354444101966573574

# api.retweet(1354444101966573574)

for tweet in twt_lst:
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)
