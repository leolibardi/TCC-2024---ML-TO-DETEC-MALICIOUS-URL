from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
import numpy as np
import pandas as pd

#Importando base de aprendizado
file_path = 'malicious_phish.csv'
df = pd.read_csv(file_path)

#Removendo valores ausentes
df.fillna(df.mode().iloc[0], inplace=True)

#Implementando processamento de linguagem natural (NLP)
tokenizer = RegexpTokenizer(r'[A-Za-z]+')
df['text_tokenized'] = df.url.map(lambda t: tokenizer.tokenize(t))

stemmer = SnowballStemmer("english")
df['text_stemmed'] = df['text_tokenized'].map(lambda l: [stemmer.stem(word) for word in l])
df['text_sent'] = df['text_stemmed'].map(lambda l: ' '.join(l))


CountVectorize = CountVectorizer()
feat = CountVectorize.fit_transform(df.text_sent)
feat[:5].toarray()

#Variaveis de treino e test
trainX, testX, trainY, testY = train_test_split(feat, df.type, test_size=0.4, random_state=42)

#Sintetizando dados(Equilibrio das classes)
smote = SMOTE(random_state=42)
trainX_smote, trainY_smote = smote.fit_resample(trainX, trainY)

#ML
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(trainX, trainY)
