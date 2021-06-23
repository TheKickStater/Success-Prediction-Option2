import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from app import app
import pandas as pd

sub_category_list = [(0, '3d Printing'), (1, 'Academic'), (2, 'Accessories'), (3, 'Action'),
 (4, 'Animals'), (5, 'Animation'), (6, 'Anthologies'), (7, 'Apparel'), (8, 'Apps'),
 (9, 'Architecture'), (10, 'Art'), (11, 'Art books'), (12, 'Audio'), (13, 'Bacon'),
 (14, 'Blues'), (15, 'Calendars'), (16, 'Camera equipment'), (17, 'Candles'),
 (18, 'Ceramics'), (19, "Children's books"), (20, 'Childrenswear'), (21, 'Chiptune'),
 (22, 'Civic design'), (23, 'Classical music'), (24, 'Comedy'), (25, 'Comic books'), 
 (26, 'Comics'), (27, 'Community gardens'), (28, 'Conceptual art'), (29, 'Cookbooks'),
 (30, 'Country & folk'), (31, 'Couture'), (32, 'Crafts'), (33, 'Crochet'), (34, 'Dance'),
 (35, 'Design'), (36, 'Digital art'), (37, 'Diy'), (38, 'Diy electronics'), (39, 'Documentary'),
 (40, 'Drama'), (41, 'Drinks'), (42, 'Electronic music'), (43, 'Embroidery'), (44, 'Events'),
 (45, 'Experimental'), (46, 'Fabrication tools'), (47, 'Faith'), (48, 'Family'), (49, 'Fantasy'),
 (50, "Farmer's Markets"), (51, 'Farms'), (52, 'Fashion'), (53, 'Festivals'), (54, 'Fiction'),
 (55, 'Film & Video'), (56, 'Fine Art'), (57, 'Flight'), (58, 'Food'), (59, 'Food Trucks'),
 (60, 'Footwear'), (61, 'Gadgets'), (62, 'Games'), (63, 'Gaming Hardware'), (64, 'Glass'),
 (65, 'Graphic Design'), (66, 'Graphic Novels'), (67, 'Hardware'), (68, 'Hip-Hop'),
 (69, 'Horror'), (70, 'Illustration'), (71, 'Immersive'), (72, 'Indie Rock'),
 (73, 'Installations'), (74, 'Interactive design'), (75, 'Jazz'), (76, 'Jewelry'),
 (77, 'Journalism'), (78, 'Kids'), (79, 'Knitting'), (80, 'Latin'), (81, 'Letterpress'),
 (82, 'Literary Journals'), (83, 'Literary Spaces'), (84, 'Live Games'), (85, 'Makerspaces'),
 (86, 'Metal'), (87, 'Mixed Media'), (88, 'Mobile Games'), (89, 'Movie Theaters'),
 (90, 'Music'), (91, 'Music Videos'), (92, 'Musical'), (93, 'Narrative Film'), (94, 'Nature'),
 (95, 'Nonfiction'), (96, 'Painting'), (97, 'People'), (98, 'Performance Art'),
 (99, 'Performances'), (100, 'Periodicals'), (101, 'Pet Fashion'), (102, 'Photo'),
 (103, 'Photobooks'), (104, 'Photography'), (105, 'Places'), (106, 'Playing Cards'),
 (107, 'Plays'), (108, 'Poetry'), (109, 'Pop'), (110, 'Pottery'), (111, 'Print'),
 (112, 'Printing'), (113, 'Product Design'), (114, 'Public Art'), (115, 'Publishing'),
 (116, 'Punk'), (117, 'Puzzles'), (118, 'Quilts'), (119, 'R&B'), (120, 'Radio & Podcasts'),
 (121, 'Ready-to-Wear'), (122, 'Residencies'), (123, 'Restaurants'), (124, 'Robots'),
 (125, 'Rock'), (126, 'Romance'), (127, 'Rcience fiction'), (128, 'Sculpture'),
 (129, 'Shorts'), (130, 'Small Batch'), (131, 'Social Practice'), (132, 'Software'),
 (133, 'Sound'), (134, 'Space Exploration'), (135, 'Spaces'), (136, 'Stationery'),
 (137, 'Tabletop Games'), (138, 'Taxidermy'), (139, 'Technology'), (140, 'Television'),
 (141, 'Textiles'), (142, 'Theater'), (143, 'Thrillers'), (144, 'Toys'), (145, 'Translations'),
 (146, 'Typography'), (147, 'Vegan'), (148, 'Video'), (149, 'Video Art'), (150, 'Video Games'),
 (151, 'Wearables'), (152, 'Weaving'), (153, 'Web'), (154, 'Webcomics'), (155, 'Webseries'),
 (156, 'Woodworking'), (157, 'Workshops'), (158, 'World Music'), (159, 'Young Adult'), (160, 'Zines')]

# def build_banner():
#     return html.Div(
#         id="banner",
#         className="banner",
#         children=[
#             html.Div(
#                 id="banner-text",
#                 children=[
#                     html.H5("Kickstarter Prediction"),
#                 ],
#             ),
#         ],
#     )


# def build_tabs():
#     return html.Div(
#         id="tabs",
#         className="tabs",
#         children=[
#             dcc.Tabs(
#                 id="app-tabs",
#                 value="tab2",
#                 className="custom-tabs",
#                 children=[
#                     dcc.Tab(
#                         id="Kickstarter-Paramters",
#                         label="Kickstarter Parameters",
#                         value="tab1",
#                         className="custom-tab",
#                         selected_className="custom-tab--selected",
#                     ),
#                     dcc.Tab(
#                         id="Kickstarter-Details",
#                         label="Kickstarter Details",
#                         value="tab2",
#                         className="custom-tab",
#                         selected_className="custom-tab--selected",
#                     ),
#                 ],
#             )
#         ],
#     )


# app.layout = html.Div(
#     id="big-app-container",
#     children=[
#         build_banner(),
#         html.Div(
#             id="app-container",
#             children=[
#                 build_tabs(),
#                 # Main app
#                 html.Div(id="app-content"),
#             ],
#         ),
#     ],
# )

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