import joblib

model = joblib.load('sentiment_model.pkl')

test_tweets = [
    "This is good!",
    "What a terrible dish!",
    "It's alright.",
    "I am sooo happy.",
    "Ok",
    "Very poor"
]

for tweet in test_tweets:
    prediction = model.predict([tweet])[0]
    print(f"Tweet: {tweet} \033[91m[{prediction}]\033[0m")