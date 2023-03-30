from tweety.bot import Twitter


app = Twitter()

all_tweets = app.search("Ukraine")
for tweet in all_tweets.tweets:
    print(tweet.text)
