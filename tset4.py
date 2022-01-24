# from app import spotify_df


#import of another variable from python file
#print (spotify_df)


def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    return(itm)
 

# genre = spotify_df[['genre','key']]

# keys = genre.loc[genre['genre'] == "Soul"]

# print (most_frequent(keys['key'].tolist()))


    