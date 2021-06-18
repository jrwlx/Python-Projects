import tweepy
import time

auth = tweepy.OAuthHandler('mTQJpNe8AV4Poi4VWsKfyUwII', '9yCwWsddZfBjt9CJjvrs1X4gW0iPd8fDSCjWVGWa0rn0RMKGmp')
auth.set_access_token('887911920572837888-XnWILEiTIoVVMZorEDsmP8q84cUPZVn', 'RH4SCFcEPJYXM1O481ikPcu8YNRx6Et2SkLBV4EdPwIa7')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# Narcissistic Bot
search_string = 'Jarren'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Nnesandz_05':
#         follower.follow()
#         break

