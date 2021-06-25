import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from app import app
import pandas as pd

# Hard coded sub category to save space for model on heroku
sub_category_list= [[{'label': 'Art', 'value': 10}, {'label': 'Ceramics', 'value': 18}, {'label': 'Conceptual Art', 'value': 28},
  {'label': 'Digital Art', 'value': 36}, {'label': 'Illustration', 'value': 70}, {'label': 'Installations', 'value': 73},
  {'label': 'Mixed Media', 'value': 87}, {'label': 'Painting', 'value': 96}, {'label': 'Performance Art', 'value': 98},
  {'label': 'Public Art', 'value': 114}, {'label': 'Sculpture', 'value': 128}, {'label': 'Social Practice', 'value': 131},
  {'label': 'Textiles', 'value': 141}, {'label': 'Video Art', 'value': 149}],
 [{'label': 'Anthologies', 'value': 6}, {'label': 'Comic Books', 'value': 25}, {'label': 'Comics', 'value': 26},
  {'label': 'Events', 'value': 44}, {'label': 'Graphic Novels', 'value': 66}, {'label': 'Webcomics', 'value': 154}],
 [{'label': 'Candles', 'value': 17}, {'label': 'Crafts', 'value': 32}, {'label': 'Crochet', 'value': 33},
  {'label': 'Diy', 'value': 37}, {'label': 'Embroidery', 'value': 43}, {'label': 'Glass', 'value': 64},
  {'label': 'Knitting', 'value': 79}, {'label': 'Pottery', 'value': 110}, {'label': 'Printing', 'value': 112},
  {'label': 'Quilts', 'value': 118}, {'label': 'Stationery', 'value': 136}, {'label': 'Taxidermy', 'value': 138},
  {'label': 'Weaving', 'value': 152}, {'label': 'Woodworking', 'value': 156}],
 [{'label': 'Dance', 'value': 34}, {'label': 'Performances', 'value': 99}, {'label': 'Residencies', 'value': 122},
  {'label': 'Spaces', 'value': 135}, {'label': 'Workshops', 'value': 157}],
 [{'label': 'Architecture', 'value': 9}, {'label': 'Civic Design', 'value': 22}, {'label': 'Design', 'value': 35},
  {'label': 'Graphic Design', 'value': 65}, {'label': 'Interactive Design', 'value': 74}, {'label': 'Product Design', 'value': 113},
  {'label': 'Toys', 'value': 144}, {'label': 'Typography', 'value': 146}],
 [{'label': 'Accessories', 'value': 2}, {'label': 'Apparel', 'value': 7}, {'label': 'Childrenswear', 'value': 20},
  {'label': 'Couture', 'value': 31}, {'label': 'Fashion', 'value': 52}, {'label': 'Footwear', 'value': 60},
  {'label': 'Jewelry', 'value': 76}, {'label': 'Pet Fashion', 'value': 101}, {'label': 'Ready-To-Wear', 'value': 121}],
 [{'label': 'Action', 'value': 3}, {'label': 'Animation', 'value': 5}, {'label': 'Comedy', 'value': 24},
  {'label': 'Documentary', 'value': 39}, {'label': 'Drama', 'value': 40}, {'label': 'Experimental', 'value': 45},
  {'label': 'Family', 'value': 48}, {'label': 'Fantasy', 'value': 49}, {'label': 'Festivals', 'value': 53},
  {'label': 'Film & Video', 'value': 55}, {'label': 'Horror', 'value': 69}, {'label': 'Movie Theaters', 'value': 89},
  {'label': 'Music Videos', 'value': 91}, {'label': 'Narrative Film', 'value': 93}, {'label': 'Romance', 'value': 126},
  {'label': 'Science Fiction', 'value': 127}, {'label': 'Shorts', 'value': 129}, {'label': 'Television', 'value': 140},
  {'label': 'Thrillers', 'value': 143}, {'label': 'Webseries', 'value': 155}],
 [{'label': 'Bacon', 'value': 13}, {'label': 'Community Gardens', 'value': 27}, {'label': 'Cookbooks', 'value': 29},
  {'label': 'Drinks', 'value': 41}, {'label': 'Events', 'value': 44}, {'label': "Farmer'S Markets", 'value': 50},
  {'label': 'Farms', 'value': 51}, {'label': 'Food', 'value': 58}, {'label': 'Food Trucks', 'value': 59},
  {'label': 'Restaurants', 'value': 123}, {'label': 'Small Batch', 'value': 130}, {'label': 'Spaces', 'value': 135},
  {'label': 'Vegan', 'value': 147}],
 [{'label': 'Games', 'value': 62}, {'label': 'Gaming Hardware', 'value': 63}, {'label': 'Live Games', 'value': 84},
  {'label': 'Mobile Games', 'value': 88}, {'label': 'Playing Cards', 'value': 106}, {'label': 'Puzzles', 'value': 117},
  {'label': 'Tabletop Games', 'value': 137}, {'label': 'Video Games', 'value': 150}],
 [{'label': 'Audio', 'value': 12}, {'label': 'Journalism', 'value': 77}, {'label': 'Photo', 'value': 102},
  {'label': 'Print', 'value': 111}, {'label': 'Video', 'value': 148}, {'label': 'Web', 'value': 153}],
 [{'label': 'Blues', 'value': 14}, {'label': 'Chiptune', 'value': 21}, {'label': 'Classical Music', 'value': 23},
  {'label': 'Comedy', 'value': 24}, {'label': 'Country & Folk', 'value': 30}, {'label': 'Electronic Music', 'value': 42},
  {'label': 'Faith', 'value': 47}, {'label': 'Hip-Hop', 'value': 68}, {'label': 'Indie Rock', 'value': 72},
  {'label': 'Jazz', 'value': 75}, {'label': 'Kids', 'value': 78}, {'label': 'Latin', 'value': 80},
  {'label': 'Metal', 'value': 86}, {'label': 'Music', 'value': 90}, {'label': 'Pop', 'value': 109},
  {'label': 'Punk', 'value': 116}, {'label': 'R&B', 'value': 119}, {'label': 'Rock', 'value': 125},
  {'label': 'World Music', 'value': 158}],
 [{'label': 'Animals', 'value': 4}, {'label': 'Fine Art', 'value': 56}, {'label': 'Nature', 'value': 94},
  {'label': 'People', 'value': 97}, {'label': 'Photobooks', 'value': 103}, {'label': 'Photography', 'value': 104},
  {'label': 'Places', 'value': 105}],
 [{'label': 'Academic', 'value': 1}, {'label': 'Anthologies', 'value': 6}, {'label': 'Art Books', 'value': 11},
  {'label': 'Calendars', 'value': 15}, {'label': "Children'S Books", 'value': 19}, {'label': 'Comedy', 'value': 24},
  {'label': 'Fiction', 'value': 54}, {'label': 'Letterpress', 'value': 81}, {'label': 'Literary Journals', 'value': 82},
  {'label': 'Literary Spaces', 'value': 83}, {'label': 'Nonfiction', 'value': 95}, {'label': 'Periodicals', 'value': 100},
  {'label': 'Poetry', 'value': 108}, {'label': 'Publishing', 'value': 115}, {'label': 'Radio & Podcasts', 'value': 120},
  {'label': 'Translations', 'value': 145}, {'label': 'Young Adult', 'value': 159}, {'label': 'Zines', 'value': 160}],
 [{'label': '3D Printing', 'value': 0}, {'label': 'Apps', 'value': 8}, {'label': 'Camera Equipment', 'value': 16},
  {'label': 'Diy Electronics', 'value': 38}, {'label': 'Fabrication Tools', 'value': 46}, {'label': 'Flight', 'value': 57},
  {'label': 'Gadgets', 'value': 61}, {'label': 'Hardware', 'value': 67}, {'label': 'Makerspaces', 'value': 85},
  {'label': 'Robots', 'value': 124}, {'label': 'Software', 'value': 132}, {'label': 'Sound', 'value': 133},
  {'label': 'Space Exploration', 'value': 134}, {'label': 'Technology', 'value': 139}, {'label': 'Wearables', 'value': 151},
  {'label': 'Web', 'value': 153}],
 [{'label': 'Comedy', 'value': 24}, {'label': 'Experimental', 'value': 45}, {'label': 'Festivals', 'value': 53},
  {'label': 'Immersive', 'value': 71}, {'label': 'Musical', 'value': 92}, {'label': 'Plays', 'value': 107},
  {'label': 'Spaces', 'value': 135}, {'label': 'Theater', 'value': 142}]]

# Started creating tabs for stretch goal interaction
app.layout = html.Div([
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Tab one',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab two',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab three, multiline',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab four',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes')
])


@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

layout = app.layout

