from textblob import TextBlob

#Calculating how sentiments have changed during an entire period (by months) in terms of polarity 

for row in data.itertuples():
    tweet = data.at[row[0], 'Lemma']
    analysis = TextBlob(tweet)
    data.at[row[0], 'polarity'] = analysis.sentiment[0]
    data.at[row[0], 'subjectivity'] = analysis.sentiment[1]
    if analysis.sentiment[0]>0:
        data.at[row[0], 'Sentiment'] = "Positive"
    elif analysis.sentiment[0]<0:
        data.at[row[0], 'Sentiment'] = "Negative"
    else:
        data.at[row[0], 'Sentiment'] = "Neutral"
  
datasent = data[["Date", "Sentiment"]]
datasent['Date'] = pd.to_datetime(datasent['Date']).dt.date
datasent['Date'] = pd.to_datetime(datasent['Date'], errors='coerce')
datasent['month'] = datasent['Date'].dt.month
datasent = datasent[datasent['month'] != 2]

datasent.to_csv('datasent.csv', sep=',', index=False)

#The same in terms of subjectivity

datasent = data[["Date", "subjectivity"]]

datasent['Date'] = pd.to_datetime(datasent['Date']).dt.date
datasent['Date'] = pd.to_datetime(datasent['Date'], errors='coerce')
datasent['month'] = datasent['Date'].dt.month
datasent = datasent[datasent['month'] != 2]

datasent.to_csv('datasub.csv', sep=',', index=False)

# Detailed revealing of emotions from tweets mentioning 'russians' (not polarity, but share of certain emotional component)

import text2emotion as te

def emotion_detection_t2e (x):
    all_emotions_value = te.get_emotion(x)
    keymax = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    return keymax
    
filtered_df['emotion'] = filtered_df['Lemma'].apply(te.get_emotion)

filtered_df['happy'] = filtered_df['emotion'].apply(lambda x: list(x.values())[0])
filtered_df['angry'] = filtered_df['emotion'].apply(lambda x: list(x.values())[1])
filtered_df['surprise'] = filtered_df['emotion'].apply(lambda x: list(x.values())[2])
filtered_df['sad'] = filtered_df['emotion'].apply(lambda x: list(x.values())[3])
filtered_df['fear'] = filtered_df['emotion'].apply(lambda x: list(x.values())[4])

emotions = filtered_df[['Number of Likes', 'Date', 'Lemma', 'happy', 'angry', 'surprise', 'sad', 'fear']]

emolist = (round(filtered_df['happy'].mean(), 2),
round(filtered_df['angry'].mean(), 2),
round(filtered_df['surprise'].mean(), 2),
round(filtered_df['sad'].mean(), 2),
round(filtered_df['fear'].mean(), 2))

emolistnames = ('happy', 'angry', 'surprise', 'sad', 'fear')

ruemo = pd.DataFrame(list(zip(emolistnames, emolist)),
               columns =['Emotion', 'Average Share in a Tweet'])
ruemo.to_csv('ruemo.csv', sep=',', index=False)
