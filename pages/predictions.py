# Imports from 3rd party libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from .newpage import sub_category_list
# Imports from this application
from app import app
from joblib import load
pipeline = load("assets/model.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
@app.callback(
    Output('prediction-content', 'children'),
    [Input('usd_goal', 'value'), 
    Input('category', 'value'),
    Input('timeline', 'value'),
    Input('sub_category', 'value'),
    Input('text', 'value'),
    ],
)
def predict(usd_goal,category,timeline,sub_category,
text
):
    df = pd.DataFrame(
        columns=['usd_goal',
        'category',
        'timeline',
        'sub_category',
        'text',
], 
        data=[[usd_goal, category,timeline,sub_category,
       text
        ]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'


column1 = dbc.Col(
    [
        dcc.Markdown('## Kickstarter Parameters', className='mb-5'), 
        dcc.Markdown('#### How much funding do you need to raise?'), 
        dcc.Input(
            id="usd_goal", type="number", placeholder="Input Kickstarter Goal",
            min=100, max=10000000, step=100, className='mb-5',
        # dcc.Slider(
        #     id='usd_goal', 
        #     min=1000, 
        #     max=1000000, 
        #     step=1, 
        #     value=800, 
        #     marks={n: str(n) for n in range(1,1000001,100000)}, 
        #     className='mb-5', 
        ), 
        dcc.Markdown('#### How long will your project be open for funding?'),
        dcc.Input(
            id="timeline", type="number", placeholder="Input the number of days funding will be open",
            min=10, max=365, step=10, className='mb-5',
        # dcc.Slider(
        #     id='timeline', 
        #     min=10, 
        #     max=365, 
        #     step=30, 
        #     value=100, 
        #     marks={n: str(n) for n in range(10,366,30)}, 
        #     className='mb-5', 
        ), 
        dcc.Markdown('#### What category is your project?'), 
        dcc.Dropdown(
            id='category',
            className='mb-5',
            options=[
                {'label': 'Art', 'value': 0},
                {'label': 'Comics', 'value': 1},
                {'label': 'Crafts', 'value': 2},
                {'label': 'Dance', 'value': 3},
                {'label': 'Design', 'value': 4},
                {'label': 'Fashion', 'value': 5},
                {'label': 'Film & Video', 'value': 6},
                {'label': 'Food', 'value': 7},
                {'label': 'Games', 'value': 8},
                {'label': 'Journalism', 'value': 9},
                {'label': 'Music', 'value': 10},
                {'label': 'Photography', 'value': 11},
                {'label': 'Publishing', 'value': 12},
                {'label': 'Technology', 'value': 13},
                {'label': 'Theater', 'value': 14},

        ],
        value=0
        ),
 
        dcc.Markdown('#### What is the sub-category?'), 
        dcc.Dropdown(
            id='sub_category',
            className='mb-5',
            options=[
                {'label': label, 'value': value}
                    for value, label in sub_category_list
        ],
        value=0
        ), 
        dcc.Markdown('#### Text'), 
        dcc.Textarea(
            id='text',
            placeholder='Enter a value...',
            value='This is a TextArea component',
            style={'width': '100%'},
            className='mb-5',
        ), 
        
        # dcc.Markdown(
        #     """
        
        #     ## Feature Explination

        #     The features on the right are the 7 major contributors to the machine 
        #     learning model. 

        #     ##### Unique ID : 
        #     ToDo
        #     ##### Since Created : 
        #     ToDo
        #     ##### Since Launched : 
        #     ToDo
        #     ##### Since Changed : 
        #     ToDo
        #     ##### USD Pledged : 
        #     ToDo
        #     ##### Text : 
        #     ToDo
        #     ##### State : 
        #     ToDo
        #     """
        # ),
    ],
    md=6,
)

column2 = dbc.Col(
    className='mb-40'
)

column3 = dbc.Col(
    [
        html.H2('Kickstarter Prediction', className='mb-4'),
        html.Div(id='prediction-content', className='lead')
    ],
    className='mb-40',
    md=5

)


layout = dbc.Row([column1, column2, column3])
