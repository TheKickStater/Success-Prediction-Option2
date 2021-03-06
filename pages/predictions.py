# Imports from 3rd party libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_daq as daq
from .newpage import sub_category_list
# Imports from this application
from app import app
# import pickle, json
import pandas as pd
import numpy as np
import requests
import json


url = 'https://kickstarterbackend.herokuapp.com/model'
# Calls prediction from external model by providing api call with values.
def predict(usd_goal,category,timeline,sub_category,text):
    body = {"usd_goal":usd_goal, "term":timeline, "category":category, "blurb":text, "subcategory":sub_category}
    response = requests.post(url, json=body, headers={"content-type":"application/json"})
    y_pred_proba = float(response.json()['prediction'])
    if(y_pred_proba) >= 0.5:
        y_pred = "Success predicted"
    else:
        y_pred = "Lack of success predicted"
    return y_pred, y_pred_proba


column1 = dbc.Col(
    [
        dcc.Markdown('## Kickstarter Campaign Parameters', className='mb-5'),
        # Creates a Goal input and pass the value
        dcc.Markdown('#### How much funding do you need to raise?'),
        daq.NumericInput(
            id = "usd_goal", min=100, max=10000000, value=1000,
            className='mb-5', size=540

            ),
        # Creates a Kickstert Funding Length input and pass the value
        dcc.Markdown('#### How long will your project be open for funding?'),
        daq.NumericInput(
            id = "timeline", min=10, max=365, value=30,
            className='mb-5', size=540

            ),
        # Creates a category input and passes numerical value
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
        # Creates a sub-category input and passes numerical value
        dcc.Markdown('#### What is the sub-category?'), 
        dcc.Dropdown(
            id='sub_category',
            className='mb-5',
        value=0
        ), 
        # Takes text data and passes to the model
        dcc.Markdown('#### Kickstarter Description'), 
        dcc.Textarea(
            id='text',
            placeholder='Enter a value...',
            value='Please write a short description of your project ( < 50 words)',
            style={'width': '100%'},
            className='mb-5',
        ), 
        # Adds a butotn that extracts the input values and passes to the model
        dbc.Button("Predict Kickstarter Success", id="example-button", color='primary',
                   className="mr-2"),
        html.Div(id='container-button-timestamp'),
        html.Span(id="example-output",
                  style={"vertical-align": "middle"}),
    ],
    md=6,
)

# Set call back to be applied with button press.
@app.callback(
    Output("prediction-content",
           "children"), [Input("example-button", 'n_clicks')],
    [
        State('usd_goal', 'value'),
        State('category', 'value'),
        State('timeline', 'value'), 
        State('sub_category', 'value'),
        State('text', 'value'),
    ]
)
# Function that passes values to predict function on button click
def on_button_click(n, timeline,usd_goal,category,text,sub_category):
    '''
    on_button_click function passes information from the model on clicl
    '''
    if n is None:
        return "Please fill in the Kickstarter Model"
    else:
        y_pred, y_pred_proba = predict(timeline,usd_goal,category,text,sub_category)
        return '{}, with a likelihood of {}%'.format(y_pred, y_pred_proba)

# Create another callback for gauge probability
@app.callback(
    Output("my-gauge",
           "value"), [Input("example-button", 'n_clicks')],
    [
        State('usd_goal', 'value'),
        State('category', 'value'),
        State('timeline', 'value'), 
        State('sub_category', 'value'),
        State('text', 'value'),
    ]
)
# Pass predict function to retrive y_pred_proba
def predict_button_click(n_clicks, timeline,usd_goal,category,text,sub_category):
    '''
    on_button_click function passes information from the model on clicl
    '''
    y_pred, y_pred_proba = predict(timeline,usd_goal,category,text,sub_category)
    y_pred_proba = y_pred_proba * 100
    if n_clicks == None:
        return 0
    else:
        return y_pred_proba

# Using a blank column for spacing
column2 = dbc.Col(
    className='mb-40'
)

column3 = dbc.Col(
    [
        # Create a lable and pass prediction value
        html.H2('Kickstarter Prediction', className='mb-4'),
        html.Div(id='prediction-content', className='lead'),
        daq.Gauge(
            id= 'my-gauge',
            color={"gradient":True,"ranges":{"red":[0,60],"yellow":[60,80],"green":[80,100]}},
            value= 0,
            label='',
            max=100,
            min=0,
        )
    ],
    className='mb-40',
    md=5
)
layout = dbc.Row([column1, column2, column3])

# Creates options for sub category based on category list
@app.callback(
    Output('sub_category', 'options'),
    Input('category', 'value'))
def set_cities_options(select_category):
    return sub_category_list[select_category]

# Inputs sub category options into dropdown menu
@app.callback(
    Output('sub_category', 'value'),
    Input('sub_category', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']