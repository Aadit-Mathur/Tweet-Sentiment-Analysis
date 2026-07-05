import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv('Tweets.csv')
df = df.drop(columns=['textID'])
df['text'] = df['text'].fillna('')

X_train = df['text']
y_train = df['sentiment']

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter = 1000))
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, 'sentiment_model.pkl')

print("Training complete")