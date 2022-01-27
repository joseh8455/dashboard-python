import pandas as pd
import re
import string
from collections import Counter

from nltk.corpus import stopwords
import nltk

df = pd.read_csv('SpotifyFeatures.csv')

stop_words = stopwords.words('english')

words = []

for j in range(len(stop_words)):

    words.append(stop_words[j].capitalize())

print(words)





# titles = df[['track_name','genre']]

# titleOfSong = titles.loc[titles['genre'] == "Movie"]

# list_of_songs = titleOfSong['track_name'].tolist()

# newlist = [word for word in list_of_songs for word in word.split()]

# #this get rids of everything gets rid of (feat
# regex = re.compile(r'\(.*|feat$|-|/|the|and|a|A|The')

# filter_value = [i for i in newlist if not regex.match(i)]

# count = Counter(filter_value)

# #this gets the most common word
# most_occur = count.most_common(10)

# words_common = []

# words_count = []

# for i in most_occur:
#     words_common.append(i[0])
#     words_count.append(i[1])

# full_count = [words_common, words_count]
# print (full_count[0])
# print (full_count[1])
