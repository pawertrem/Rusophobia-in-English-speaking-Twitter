#!/usr/bin/env python
# coding: utf-8

# In[178]:


import snscrape.modules.twitter as sntwitter
import pandas as pd


# In[184]:


get_ipython().run_cell_magic('time', '', "1 + 1\nattributes_container = []\ndays = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']\nmax_tweets = 10000\n\nfor n in days:\n    try:\n        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('Russia until:2022-08-'+n).get_items()):\n            if i>max_tweets:\n                break\n            attributes_container.append([tweet.likeCount, tweet.content, tweet.date])\n    except KeyError:\n        pass")


# In[185]:


tweets = pd.DataFrame(attributes_container, columns=["Number of Likes", "Tweet", "Date"])
tweets_before = tweets


# In[188]:


tweets_before.to_csv('august.csv', sep=',', index=False)

