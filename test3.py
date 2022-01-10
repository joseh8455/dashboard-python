import base64

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


spotify_df = pd.read_csv('SpotifyFeatures.csv')

anime_songs = spotify_df[spotify_df['genre'].isin(['Anime'])]


type_of_genres = []
artist = []
key = []

for index, row in spotify_df.iterrows():
    type_of_genres.append(row['genre'])
    artist.append(row['artist_name'])
    key.append(row['key'])

#filtered list in dataset downloaded
filter_genre_list = list(dict.fromkeys(type_of_genres))

def everyCatgr():
    
    ctgrs = f"'{*filter_genre_list,}'"
    
    return ctgrs

strVal = everyCatgr()

print (strVal)