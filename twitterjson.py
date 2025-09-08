import tweepy
import json
API_KEY = "1gICbTZ0JEpzLxxVUtWNYGDlc"

API_SECRET_KEY = "RpZ6kF5sSIu8pnVWD8gp2K0V59i1mXdFg09Igx2TRoKuiCvRif"

BEARER_TOKEN ="AAAAAAAAAAAAAAAAAAAAAF7B3gEAAAAAuDIAsF8237IFlUwTcZGHzaWY45E%3DBidDnQzeTNbCNxNbI0thRULbrk8cwsQ9iWFlwDEtHq2AuSVlmS"

ACCESS_TOKEN ="1957826515888140292-c7gaa1W834mfDZveinfEzyio7ju50H"

ACCESS_TOKEN_SECRET ="JsN1Es3bTIdDcxIt3nIG4VcYpQCfdT9rmIc7XTodPzJGi"
if __name__ == "__main__":
    try:
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="sundarpichai")

        user_id = user.data.id

        # get tweets
        tweets  = twitterClient.get_users_tweets(
            user_id,
            max_results=50, # for people who got the output -> 50
            tweet_fields=['created_at', 'public_metrics', 'text']
        )

        # save the tweets to json file
        with open("analyzed_tweets.json", "w") as json_file:
            # [].map(e=>e.toString())
            json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")