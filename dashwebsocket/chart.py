import dashwebsocket
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import json
import pandas as pd
import requests
from pandas import json_normalize
import plotly.graph_objects as go
from datetime import datetime


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])



app.layout = html.Div([
    html.Div([
        dashwebsocket.DashWebsocket(
            id='input',
            url='ws://localhost:5656'
        )
    ],style={'display': 'none'}),
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('MSFT',className="card-title"),
                        dbc.CardBody(id='MSFT')
                    ], color="dark", inverse=True)
                ]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('AAPL',className="card-title"),
                        dbc.CardBody(id='AAPL')
                    ], color="dark", inverse=True)
                ]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('NVDA',className="card-title"),
                        dbc.CardBody(id='NVDA')
                    ], color="dark", inverse=True)
                ]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('AMZN',className="card-title"),
                        dbc.CardBody(id='AMZN')
                    ], color="dark", inverse=True)
                ])
            ])
        ])
    ], color="secondary", inverse=True),
    dcc.Graph(
        id='candles',
        animate=True,
        figure=fig,
    )
])



if __name__ == '__main__':
    app.run_server(debug=True,port=8051,host='0.0.0.0')
    # app.run_server(debug=True)
