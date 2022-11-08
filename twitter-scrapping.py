#Import of libraries
import snscrape.modules.twitter as sntwitter
import pandas as pd

#Collecting 10 000 tweets per day from March to August (indicator of a month should be chanegd manually in a field 'untill' as collecting all data for the entire period would take too much time and gives less chances for control of a process) 

%%time
1 + 1
attributes_container = []
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
max_tweets = 10000

for n in days:
    try:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('Russia until:2022-08-'+n).get_items()):
            if i>max_tweets:
                break
            attributes_container.append([tweet.likeCount, tweet.content, tweet.date])
    except KeyError:
        pass

#Saving of dataframe

tweets = pd.DataFrame(attributes_container, columns=["Number of Likes", "Tweet", "Date"])
tweets_before = tweets
tweets_before.to_csv('august.csv', sep=',', index=False)
