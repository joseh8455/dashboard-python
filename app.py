from collections import Counter
import re
import dash
from dash import dcc as dcc
import dash.dash_table as dt
from dash import html as html
from dash.dependencies import Input, Output
import pandas as pd

from test4 import most_frequent

spotify_df = pd.read_csv('SpotifyFeatures.csv')

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

def common_word(x):
    titles = spotify_df[['track_name','genre']]

    titleOfSong = titles.loc[titles['genre'] == x]

    list_of_songs = titleOfSong['track_name'].tolist()
    newlist = [word for word in list_of_songs for word in word.split()]
    regex = re.compile(r'\(.*|feat$|-|/|.[Tt]he|and|a|A|The|Pt.|I\'m')

    pre_filter1 = [i for i in newlist if not regex.match(i)]

    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    upper_words = []
    cap_words = []
    for j in range(len(stop_words)):
        upper_words.append(stop_words[j].upper())
        cap_words.append(stop_words[j].capitalize())
        
    
    pre_filter2 = [x for x in pre_filter1 if not x in stop_words]
    pre_filter3 = [y for y in pre_filter2 if not y in upper_words]
    pre_filter4 = [z for z in pre_filter3 if not z in cap_words]

    #this gets the most common word
    count = Counter(pre_filter4)
    most_occur = count.most_common(10)

    words_common = []

    words_count = []

    for i in most_occur:
        words_common.append(i[0])
        words_count.append(i[1])

    full_count = [words_common, words_count]
    return full_count

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
                    id="first-graph"
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
            html.Div(id = 'dd-output1'),
            #id is used to tie to more charts down the road
            dcc.Dropdown( id='first-Query', options= [{'label': i ,'value': i}for i in filter_genre_list
                        ], placeholder="Category of music", className = "drpdwn-musiccat")
            
            ]
            
                 ,className='frst-drpdwn'),
        html.Div(children = [
                html.H1(id = "common-letter"),
                html.P(id = "common-word")
            ],className=""),
        
        html.Div(
            id="common-word-graph"
        ),
        
        html.Div(
            children=[
                html.H1(children='Enjoy The Data :).',className='footer-header'),
                html.H2(children='Information Provided by Kaggle.', className='footer-info'),
                html.A(children='GitHub to other projects', href='https://github.com/joseh8455', className='footer-link')
            ],
            className='footer'
        )
    ]
)

@app.callback(
    Output(component_id='dd-output1', component_property='children'),
    Input(component_id='first-Query', component_property='value')
)
def update_output_div(input_value):
    return 'You have selected to go in depth with: {}'.format(input_value)

@app.callback(
    Output(component_id='common-letter', component_property='children'),
    Input(component_id='first-Query', component_property='value')
)
def commonLetter(input_value):
    genre = spotify_df[['genre','key']]
    keys = genre.loc[genre['genre'] == '{}'.format(input_value)]
    common_letter = most_frequent(keys['key'].tolist())
    return "This is the common key note based on {}".format(input_value) + ":" + common_letter

@app.callback(
    Output(component_id="common-word-graph", component_property="children"),
    Input(component_id="first-Query", component_property="value")
)
def commonWords(input_value):
    words = common_word("{}".format(input_value))[0]
    wordCount = common_word("{}".format(input_value))[1]

    word_count = dcc.Graph(
        figure= {
            "data":[
                    {
                        "x": words,
                        "y" : wordCount,
                        "type": "bar"
                    },
                ],
            "layout" : {"title" : "Top 10 Most Common Word"},
        }
    )
    return word_count



if __name__ == "__main__":
    app.run_server(debug=True)
