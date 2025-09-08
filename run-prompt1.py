import tweepy
from run_prompt import execute_gemini

API_KEY = "1gICbTZ0JEpzLxxVUtWNYGDlc"

API_SECRET_KEY = "RpZ6kF5sSIu8pnVWD8gp2K0V59i1mXdFg09Igx2TRoKuiCvRif"

BEARER_TOKEN ="AAAAAAAAAAAAAAAAAAAAAF7B3gEAAAAAuDIAsF8237IFlUwTcZGHzaWY45E%3DBidDnQzeTNbCNxNbI0thRULbrk8cwsQ9iWFlwDEtHq2AuSVlmS"

ACCESS_TOKEN ="1957826515888140292-c7gaa1W834mfDZveinfEzyio7ju50H"

ACCESS_TOKEN_SECRET ="JsN1Es3bTIdDcxIt3nIG4VcYpQCfdT9rmIc7XTodPzJGi"
if __name__ == "__main__":
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

        Latest_5_tweets = twitterClient.get_users_tweets(user_id, max_results=5)

        for tweet in Latest_5_tweets.data:
            print(tweet.text)
            prompt = f"""
            Summarize the twitter tweet attached and give it a sentimental analysis score
            TWEET ==> {tweet.text}
            """
            llm_out = execute_gemini(prompt)
            print(llm_out)