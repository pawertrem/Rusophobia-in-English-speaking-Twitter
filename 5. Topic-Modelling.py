#Import of data and libraries

import pyLDAvis.gensim_models
pyLDAvis.enable_notebook()# Visualise inside a notebook
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaMulticore
from gensim.models import CoherenceModel

import pandas as pd
data = pd.read_csv ('./df_lemma.csv', sep=',', encoding='utf-8')

#Given that building of the LDA is a quite time-consuming process in the case of our amount of observations, only 10 000 of the most liked tweets are left for topic modelling  

datatest = data.sort_values(by=['Number of Likes'], ascending=False).head(10000)

#Removing of italian words left after the 'language filtering', presence of which has appeared to be problematic after the first attempt to build LDA 

def remove_words(list1, remove_words):
    for word in list(list1):
        if word in remove_words:
            list1.remove(word)
    return list1  

trash = ['000', '400', 'das', 'tica', 'san', 'sobre', 'estado', 'russa', 'russos', 'pela', 'pelo', 'ele', 'eua', 'dia']

datatest['Lemma'] = datatest['Lemma'].apply(lambda x: remove_words(x, trash))

#Creation of a dictionary

dictionary = Dictionary(datatest['Lemma'])
dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=10000)

#Creation of a corpus

corpus = [dictionary.doc2bow(doc) for doc in datatest['Lemma']]

#LDA

from gensim.models.ldamodel import LdaModel

k = 5
tweets_lda = LdaModel(corpus,
                      num_topics = k,
                      id2word = dictionary,
                      random_state = 1,
                      passes=50)

tweets_lda.show_topics()

#Visualisation of LDA

import pyLDAvis.gensim_models
pyLDAvis.enable_notebook()# Visualise inside a notebook

vis = pyLDAvis.gensim_models.prepare(tweets_lda, corpus, dictionary=tweets_lda.id2word)
vis

pyLDAvis.save_html(vis, 'C:/Users/User/Desktop/Jupyter/lda.html')
