# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep

consumer_key = 'H3FCyEAES4wH4SxJTKMV1CQGN'
consumer_secret = 'eZe0CiPgAaMsXCoM3PrkSkVOCPCk6La4164kZ1sXQVIOsRHEsw'
access_token = '1309960678967521280-l5Z0HAVT80evuNLwLEohYSKbNrYS3T'
access_token_secret = '0cu5jGzmp0JKiG9MTC3xTEh9zCboepfLnbpdzHn3ReB14'

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Tweet a line every 15 minutes



for tweet in tweepy.Cursor(api.search, q='#biochemistry').items():
    try:
        print('Tweet by: @' + tweet.user.screen_name)
        
        tweet.retweet()
        print('Retweeted the tweet')
        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')

        api.update_status(f" @{tweet.user.screen_name} is awesome!")
        print(f'tweeted @{tweet.user.screen_name} is awesome!"')
        

        sleep(25)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break