import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv('SpotifyFeatures.csv')

test_columns = list(test.columns)

# test.set_index(test_columns[0:3], inplace=True)
# test.sort_index(inplace=True)

genre_list = []

for index, row in test.iterrows():
    genre_list.append(row['genre'])

filter_genre_list = list(dict.fromkeys(genre_list))

print (filter_genre_list)

# number = -1
# # for genre in filter_genre_list:
# test_case_list = []

# while number != len(filter_genre_list)-1:
#     number+=1
#     interesting_number = test.loc[ test['genre'] == filter_genre_list[number]]

#     for index_val, row_value in interesting_number.iterrows():
#         test_case_list.append(list([row_value['genre'], row_value['acousticness']]))

# for 

# print (test_case_list)
    

# interesting_test = test.loc[ test['genre']== filter_genre_list[6] ]



# for index_val, row_value in interesting_test.iterrows():
#     test_case_list.append(list([row_value['genre'], row_value['acousticness']]))


# print (test_case_list)

# test.to_excel("Excel Test.xlsx", sheet_name = 'Song Data Set')
# plt.scatter(*zip(*genre_numbers))

# plt.title("Genres and how many times they show up in Data Set")
# plt.ylabel('# of Times they Show')
# plt.xlabel('Name of Genre')

# plt.show()

# #artist names and how many times they show up
# filter_artistname_list = list(dict.fromkeys(artist_list))

# artist_amount = [ len( test [ test ['artist_name'] == artist]) for artist in filter_artistname_list]

# artst_name_number = zip(filter_artistname_list, artist_amount)

# artist_numbers = list(artst_name_number)
