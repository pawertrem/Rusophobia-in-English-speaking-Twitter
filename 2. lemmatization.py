import pandas as pd
import re

#Combining all dataframes in one
march = pd.read_csv ('./tweets/march.csv', sep=',', encoding='utf-8')
april = pd.read_csv ('./tweets/april.csv', sep=',', encoding='utf-8')
may = pd.read_csv ('./tweets/may.csv', sep=',', encoding='utf-8')
june = pd.read_csv ('./tweets/june.csv', sep=',', encoding='utf-8')
july = pd.read_csv ('./tweets/july.csv', sep=',', encoding='utf-8')
august = pd.read_csv ('./tweets/august.csv', sep=',', encoding='utf-8')

df = pd.concat([march, april, may, june, july, august])
df.shape

#Cleaning of tweets (removing of 'trash' symbols and links)

def clean_tweet(tweet):
    if type(tweet) == np.float:
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp) # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+","", temp)
    temp = re.sub("#[A-Za-z0-9_]+","", temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]',' ', temp)
    temp = re.sub("[^a-z0-9]"," ", temp)
    return temp
  
results = [clean_tweet(tw) for tw in df['Tweet']]  
df['Tweet'] = results

#Removing of non-english tweets (as a word 'Russia' which was a key for scraping can be met not only in english-written tweets)

from langdetect import detect
df = df[df['Tweet']!='']
for index, row in df['Tweet'].iteritems():
    try:
        lang = detect(row) #detecting each row
        df.loc[index, 'Lang'] = lang
    except:
        lang = 'no'
        df.loc[index, 'Lang'] = lang
        
df = df[df['Lang'] == 'en']
data = df

#Lemmatization itself

import spacy
nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
def lemmatization(text):
    doc=nlp(text)
    lemma = " ".join([token.lemma_ for token in doc])
    return lemma

data['Lemma']=data['Tweet'].apply(lemmatization)

#Removing of stop-words (better to apply after lemmatization as helps to remove those SW which would not be detected in non-lematized form)

import io
with io.open("./stop_words_english.txt",'r',encoding='utf8') as f:
    stopwords = f.read()

stopwords = stopwords.replace('\n', ' ').split(" ")

stopwords = stopwords+['russia', 'russian', 'ukraine', 'ukranian', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ssia', 'amp', 'don', 'ukrainian', 'russias', 'che']

data['Lemma'] = data['Lemma'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords) and len(word)>2]))
