# Rusophobia-in-English-speaking-Twitter

A problem of rusophobia has become especially prominent in Russian pro-government agenda after Febraury 24. Nevertheless, despite a widespread impression of rusophobia's presence in a western society, we have decided to provide our independent analysis and to reveal whether a problem really exists. The full text (on Russian) can be found here: http://nepolitolog.com/russophobia

All visualizations (besides LDA) are made on the 'Infogram' platform (infogram.com)

### 1. Twitter Scrapping 

The first step is collecting of tweets. Despite existing of the API, it is not an appropriate way for us as it has significant limits not allowing to collect more than 3000 observations per request. Thus, I have used 'sntwitter' to parse Twitter. The goal was to get maximum of tweets and, at the same time, to try operate in long-term perspective. Collecting of all tweets for the entire period would be a complicated process consuming a lot of time and supposing that there with a high probability will be technical problems with such a Big Data processing at the end. Therefore, I have parsed 10 000 tweets per day for every month of the period from March to August which mentiones 'Russia'. Finally, I have got about 1.8 million tweets but after filtering of the data and removing non-english tweets there were 1.5 million. There are 3 variables which were collected: text of tweet itself, number of likes to reveal the most popular tweets, and date of publication to consider time dynamics. 

### 2. Lemmatization

The second step is lemmatization of text data. I have provided it in a quite classic 'fashion': 1) removing of unnecesarry elements such as t.co links and punctuation to shorten a process of lemmatization, 2) removing non-english tweets with 'langdetect' library as we are concerned exclusively with english ones, 3) lemmatization itself with 'spacy' library, and 4) removing of stop-words. Actually, stop-words can be removed before lemmatization as well to make a process even shorter. I have used a ready dictionary of ENG stop-words found in the Internet which I considered as the most comprehensive I have seen https://github.com/mongodb/mongo/blob/master/src/mongo/db/fts/stop_words_english.txt

Nevertheless, there are still possibilities to complement it with additional stop-words which exist in context of a phenomenon we study

### 3-5. Frequency Analysis, Sentiment Analysis and Topic Modelling

FA is provided classically for a data in general and a share of tweets which directly mention 'russians' (besides default functions, 'nltk' library is used for bigrams analysis). Sentiment Analysis is based on two libraries: 'TextBlob' for calculating polarity and subjectivity, 'text2emotions' to reveal distinct emotional components (given the fact, that 'text2emotions' is processed longer in comparison with 'TextBlob', it is appled only on the segment of data in which 'russians' are mentioned). Finally, Topic Modelling is done with 'gensim' library and 'pyLDAvis' used to visualize LDA. As in the case with 'text2emotions', processing is quite complicated, so only the most popular (with the largest amount of likes) tweets have been extracted for topic modelling. Visualization is saved in 'html' to be integrated on our web-site in the final material.
