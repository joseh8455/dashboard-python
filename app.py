from re import I

import dash
import dash_core_components as dcc
import dash_table as dt
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
genre_amount = [len(spotify_df [ spotify_df ['genre'] == genre ]) for genre in filter_genre_list ]

filter_artist_list = list(dict.fromkeys(artist))
filtered_keys = list(dict.fromkeys(key))


external_stylesheets = [
    {
        "href": 'https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,300;0,400;1,300&display=swap',
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Spotify Dashboard"


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src=app.get_asset_url('Spotify_Logo_CMYK_Green.png'), id='top-image'),
                html.H1(children='Spotify Music Analytics Based on Data Set', id='top-h1'),
                html.P(children="This uses a data set downloaded from Kaggle. This a personal project that I decided to take on. Im still not sure what the end result will be.", id='top-p'),
                html.P(children='Made by @Jose M. Hernandez', id='madeby')
            ],
            className='top-section'
        ),
        html.Div(children= [
           html.H1(children='Example of Data Set worked with', id='expData',style={'margin-top':'350px'}),
           html.Div(children = [dt.DataTable(     
                                id='table',
                                style_table={ 'height': '300px','width':'800px', 'overflowY': 'auto'},
                                fill_width = False,
                                columns=[{"name": j, "id": j} for j in spotify_df.columns],
                                data=spotify_df.to_dict('records'),)], className='dataFrame-holder'),
           html.P(children="Labore magna ad ipsum consequat duis laborum in consequat velit veniam excepteur adipisicing dolor. Quis nostrud esse pariatur cillum enim velit aute nulla. Minim officia minim"+ 
                  "sint quis dolore duis consectetur consequat sit officia incididunt aute non dolor. Commodo occaecat nisi voluptate pariatur ea velit pariatur. Ex adipisicing elit aute magna quis nostrud"+
                  "voluptate aliquip tempor voluptate ad sunt consectetur.",className='exmp_dfset')

            
            ],
                 className="midSection"),
        #graphs
        html.Div(
            children=[
                #where the information for graphs go
                dcc.Graph(
                    figure={
                        "data":[
                            {
                                "x": filter_genre_list,
                                "y" : genre_amount,
                                "type": "bar"
                            },
                        ],
                        "layout" : {"title" : "Genres and how many times they show up in Data Set"},
                        # 'style' : {}
                    },
                    id="first=graph"
                ),
            ],
            className='graph1'
        ),
        html.Div(
            children=[
                #where the second graph goes
            ],
            className='graph2'
        ),
        html.Div(children= [
            #id is used to tie to more charts down the road
            dcc.Dropdown( id=' first-Query', options= [{'label': i ,'value': i}for i in filter_genre_list
                        ])
            
            ], className='frst-drpdwn'),
        
        
        html.Div(
            children=[
                html.H1(children='Enjoy The Data :).'),
                html.P(children='Information Provided by Kaggle.'),
                html.A(children='GitHub to other projects', href='https://github.com/joseh8455')
            ],
            className='footer'
        )
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)
