#Frequency of words

top_w = pd.DataFrame(pd.Series(' '.join(data['Lemma']).split()).value_counts()[:50])
top_w.to_csv('top_w.csv', sep=',', index=True)

#Frequency of bigrams

import nltk

nltk.download([
"names",
"stopwords",
"state_union",
"twitter_samples",
"movie_reviews",
"averaged_perceptron_tagger",
"vader_lexicon",
"punkt",
])

tokens = ' '.join(data['Lemma']).split()
bigrams = nltk.bigrams(tokens)
frequence = nltk.FreqDist(bigrams)

freq = pd.DataFrame(frequence.items(), columns=['word', 'frequency'])
freq = freq.sort_values(by=['frequency'], ascending=False)
freq = freq.head(50)
freq.to_csv('bigrams.csv', sep=',', index=True)

#Frequency of words specifically around a notion of 'russians' (in terms of 3 words in both direction)

filtered_df['Passer'] = filtered_df['Lemma'].str.extract(r'((?:\S+\s+){0,3}\brussians\b\s*(?:\S+\b\s*){0,3})')
noNA = filtered_df.dropna()
top_r = pd.DataFrame(pd.Series(' '.join(noNA['Passer']).split()).value_counts()[:50])
top_r.to_csv('russians.csv', sep=',', index=True)
