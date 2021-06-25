# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## The Build Process

            #### Data Pipeline
            Data is a highly important factor in any attempt to model uncertainty, and modelling based on NLP is no
            different.  Due to the limited nature of our model's potential inputs, our team felt it neccessary to find
            a large quantity of data on which to train our model.  This data was found on the WebRobots site in the form
            of large JSON files containing months worth of KickStarter updates dating back to 2015.  We opted for only 
            using 2020 and 2021 data, as it is most interesting and applicable to the near future.  The sum size of the data
            inputted into the pre-processing pipeline was about 20.4 gigabytes, and contained around 3,600,000 observations.
            Many of these observations were duplicates, recording projects at different states of funding and completeness.
            This data was pared down to .5 gigabytes and about 200,000 observations, a nice dataset to train a model on.

            #### Leakage
            As a team we felt it was highly important to ensure there is no data leakage in our modelling effort
            It is quite easy to build a complicated if/else statement based on after-the-fact measures.  Our model
            was strictly trained on information available to an entrepreneur before running a KickStarter campaign.
            To account for the additional difficulty inherent with such a strict approach, we ensured that our data
            source was solid.  

            #### The Model
            For our model we employed a keras model employing multiple LSTM layers as well as multiple dense layers.
            This allows us the ability to call our model a true deep-learning model.  Basic NLP encoding was applied
            to the text input in both the training data as well as to the input from the user (as required).  The
            model achieved a validation accuracy of around 75% on the fairly large validation set.  This validation
            score is acceptable, however given the binary nature of the output labels, it is not extremely impressive.

            #### Possible Improvement
            Room for improvement in terms of modelling accuracy could come from better input data, which is to say
            more features and longer text input.  Our data source only contained the short 'blurb' of each campaign.
            If we had access to the longer 'description' of each campaign, it is likely natural language processing
            would be more effective.  Additionally categories like 'location' and 'location-type' could be applied 
            as model inputs, but are probably not particularly helpful to any would-be crowd-funded entrepreneurs, 
            and for that reason we elected not to include those features.  The biggest possible area to improve upon
            in terms of modelling predictive accuracy is likely two part: first, applying more advanced NLP techniques
            to the data available to us, second, creating a feature-union pipeline to train different models on different
            portions of the input dataframe.  These improvements are likely to find their way into future iterations of
            this project.


            """
        ),
        dcc.Markdown(""" 
        

        
        """
        ),



    ],
)

layout = dbc.Row([column1])