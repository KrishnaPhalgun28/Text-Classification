# Dataset Link: http://help.sentiment140.com/for-students

import pandas as pd
cols = ['sentiment', 'id', 'date', 'query', 'user', 'text']
data = pd.read_csv('training.1600000.processed.noemoticon.csv', header=None, names=cols, engine='python', encoding='latin1')
data.drop(['id', 'date', 'query', 'user'], axis=1, inplace=True)
data.to_csv('train.csv', index=False)

from bs4 import BeautifulSoup
def clean_tweet(tweet):
	tweet = BeautifulSoup(tweet, 'lxml').get_text()
	tweet = re.sub(r'@[A-Za-z0-9]+', ' ', tweet)
	tweet = re.sub(r'https?://[A-Za-z0-9./]+', ' ', tweet)
	tweet = re.sub(r'[^a-zA-Z.!?]', ' ', tweet)
	tweet = re.sub(r' +', ' ', tweet)
	return tweet

data['text'] = data['text'].apply(clean_tweet)
data[data.sentiment == 4] = 1
data.to_csv('cleaned_train.csv', index=False)