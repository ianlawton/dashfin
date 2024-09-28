import dashwebsocket
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import json
import dash_ag_grid as dag
import pandas as pd
import requests
from pandas import json_normalize

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
df2 = pd.read_csv("./nasdaq_screener_1711703649305.csv")

columnDefs = [
    {'field': 'country'},
    {'field': 'pop', 'headerName': 'Population'},
    {'field': 'lifeExp', 'headerName': 'Life Expectancy'},
]

columnDefs2 = [
    {'field': 'Symbol'},
    {'field': 'Name'},
    {'field': 'Last Sale', 'type': 'rightAligned'},
    {'field': 'Net Change', 'type': 'rightAligned'},
    {'field': '% Change', 'type': 'rightAligned'},
    {'field': 'Market Cap', 'type': 'rightAligned'},
    {'field': 'Country'},
    {'field': 'IPO Year'},
    {'field': 'Volume', 'type': 'rightAligned', 'cellDataType': 'number'},
    {'field': 'Sector'},
    {'field': 'Industry'},
]

grid = dag.AgGrid(
    id="getting-started-sort-disable-animation",
    rowData=df2.to_dict("records"),
    columnDefs=columnDefs2,
    className="ag-theme-balham-dark",
    style={'height': 'calc( 100vh - 100px - 2rem)'},
    defaultColDef={"filter": True},
    dashGridOptions={"animateRows": False}
)


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
    grid
])

@app.callback(
    [Output('MSFT', 'children'), 
    Output('AAPL', 'children'),
    Output('NVDA', 'children'), 
    Output('AMZN', 'children')],
    [Input('input', 'msg')])
def display_output(value):
    if value and value is not None:
        data = json.loads(value)
        stock = data['stock']
        price = html.H1(data['price'])   
        diff = html.H4(dbc.Badge(data['diff'], color="danger" if '-' in data['diff'] else 'success', className="mr-1"))
        content = dbc.Row([dbc.Col([price]),dbc.Col([diff])])
        if stock == 'MSFT':
            return content, dash.no_update, dash.no_update, dash.no_update
        elif stock == 'AAPL':
            return dash.no_update, content, dash.no_update, dash.no_update
        elif stock == 'NVDA':
            return dash.no_update, dash.no_update, content, dash.no_update
        elif stock == 'AMZN':
            return dash.no_update, dash.no_update, dash.no_update, content
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True,port=8050,host='0.0.0.0')
    # app.run_server(debug=True)
