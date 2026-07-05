import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Tweets.csv')
print(df.columns)

df = df.drop(columns = ['textID'])
print(df.columns)

df['sentiment'].value_counts().plot(kind='bar', title = 'Sentiment Distribution')

plt.xlabel('Sentiment')
plt.ylabel('Count of tweets')
plt.show()
plt.savefig('sentiment_distribution.png')