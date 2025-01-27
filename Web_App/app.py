from dash import Dash, html, dcc
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# SQLAlchemy connectable
db_GCP_adress='mysql+pymysql://root:projectyelp2022@34.176.218.33/projectyelp'
db_local_adress='mysql+pymysql://root:4488@localhost/yelp_pg'
engine = create_engine(db_local_adress)

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

server = app.server

app.title = 'Plus Yelp'

app.layout = html.Div([
    
    html.Div([
        html.Div([
            html.Img(src='./assets/logo.png'),
        ], className='logo'),
        # dcc.Link('home', href='/'),
        dcc.Link('business', href='/trending'),
        dcc.Link('users', href='/users'),
        # dcc.Link('about us', href='/about'),
        
    ], className='navbar'),
    


   	dash.page_container
])

if __name__ == '__main__':
	app.run_server(
                debug=True, # for deployment
                # debug=True, # enable reload when file save
                # threaded=True, # enable dev tools
                # dev_tools_hot_reload=True, # hot reload, only true for css design
                # # use_reloader=True, 
                )

