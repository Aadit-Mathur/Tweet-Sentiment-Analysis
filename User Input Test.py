import joblib

model = joblib.load('sentiment_model.pkl')

user_tweet = input("Enter tweet: ")

prediction = model.predict([user_tweet])[0]

if(prediction == 'positive'):
    print(f"Sentiment: \033[1;32m{prediction}\033[0m")
elif(prediction == 'neutral'):
    print(f"Sentiment: \033[1;34m{prediction}\033[0m")
else:
    print(f"Sentiment: \033[1;31m{prediction}\033[0m")

