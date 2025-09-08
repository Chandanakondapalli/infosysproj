import tweepy

API_KEY = "1gICbTZ0JEpzLxxVUtWNYGDlc"

API_SECRET_KEY = "RpZ6kF5sSIu8pnVWD8gp2K0V59i1mXdFg09Igx2TRoKuiCvRif"

BEARER_TOKEN ="AAAAAAAAAAAAAAAAAAAAAF7B3gEAAAAAuDIAsF8237IFlUwTcZGHzaWY45E%3DBidDnQzeTNbCNxNbI0thRULbrk8cwsQ9iWFlwDEtHq2AuSVlmS"

ACCESS_TOKEN ="1957826515888140292-c7gaa1W834mfDZveinfEzyio7ju50H"

ACCESS_TOKEN_SECRET ="JsN1Es3bTIdDcxIt3nIG4VcYpQCfdT9rmIc7XTodPzJGi"


# Authenticate with Twitter API
twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

print("✅ Authentication successful!")

# Get your own user account info
me = twitterClient.get_me()
print("👤 Logged in as:", me.data.username)

# Get your last 5 tweets
tweets = twitterClient.get_users_tweets(id=me.data.id, max_results=5)

print("\n📝 Your last 5 tweets:")
if tweets.data:
    for tweet in tweets.data:
        print("-", tweet.text)
else:
    print("No tweets found.")