# Import our Twitter credentials from credentials.py
# Add all import statements at top of file
import tweepy
from time import sleep
from credentials import *


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file=open('verne.txt','r')
file_lines=my_file.readlines()
my_file.close()

# Tweet a line every 15 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(900)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

tweet()