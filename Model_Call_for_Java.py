import sys
import joblib

# Load your model and vectorizer
model = joblib.load("sentiment_model.pkl")

# Get the tweet from command-line argument
tweet = sys.argv[1]

# Predict sentiment
prediction = model.predict([tweet])[0]

if(prediction == 'positive'):
    print(f"Sentiment: \033[1;32m{prediction}\033[0m")
elif(prediction == 'neutral'):
    print(f"Sentiment: \033[1;34m{prediction}\033[0m")
else:
    print(f"Sentiment: \033[1;31m{prediction}\033[0m")

