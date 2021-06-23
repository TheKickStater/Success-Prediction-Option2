# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Will your Kickstarter idea be successful?
           
            Do you have a Kickstarter idea you have been wanting to make, but were afraid it
            would not be successful?  Do you need some help perfecting your Kickstarter project?
            Of course you do!

            Why not use machine learning to help you predict whether your project will be successful.
            Our App will help you make these decisions and figure out a Kickstarter project with the
            best chance of success.

            Dont wait any longer! Click the button below to optimize your Kickstarter campaign.

            """
        ),
        dcc.Link(dbc.Button('Predict Kickstarter Success', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
# Example graph

column2 = dbc.Col(
    [
        # html.Img(src='graph_todo', className='img-fluid')
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])