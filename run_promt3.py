import tweepy

API_KEY = "1gICbTZ0JEpzLxxVUtWNYGDlc"

API_SECRET_KEY = "RpZ6kF5sSIu8pnVWD8gp2K0V59i1mXdFg09Igx2TRoKuiCvRif"

BEARER_TOKEN ="AAAAAAAAAAAAAAAAAAAAAF7B3gEAAAAAuDIAsF8237IFlUwTcZGHzaWY45E%3DBidDnQzeTNbCNxNbI0thRULbrk8cwsQ9iWFlwDEtHq2AuSVlmS"

ACCESS_TOKEN ="1957826515888140292-c7gaa1W834mfDZveinfEzyio7ju50H"

ACCESS_TOKEN_SECRET ="JsN1Es3bTIdDcxIt3nIG4VcYpQCfdT9rmIc7XTodPzJGi"
twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)



def execute_gemini(prompt):
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content( # user prompt (same as chat input)
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    tools = [
        # types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["sentiment_type", "sentiment_score", "topic", "keywords", "target_audience"],
            properties={
                "sentiment_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["angry", "sad", "fearful", "sarcastic", "motivational", "positive", "negative", "excited",
                          "neutral"],
                ),
                "sentiment_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "topic": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "keywords": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(
                        type=genai.types.Type.STRING,
                    ),
                ),
                "target_audience": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    )

    result = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return result.text








