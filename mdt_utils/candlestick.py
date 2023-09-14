import sqlite3, time, logging
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)
app.layout = html.Div([
    html.H4('Bitcoin candlestick chart'),
    dcc.Checklist(
        id='toggle-rangeslider',
        # options=[{'label': 'Include Rangeslider', 'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
    dcc.Interval(
        id='update-interval',
        interval=1000,  # Update every 1 second (1000 milliseconds)
        n_intervals=0  # Initialize the counter
    )
])

@app.callback(
    Output("graph", "figure"), 
    Input("toggle-rangeslider", "value"),
    Input("update-interval", "n_intervals"))
def display_candlestick(value, n_intervals):

    conn = sqlite3.connect('../sqlite.db')
    df = pd.read_sql_query('SELECT * FROM kline ORDER BY close_time DESC LIMIT 150;', conn)
    conn.close()

    fig = go.Figure(go.Candlestick(
        x=pd.to_datetime(df['close_time'], unit='ms'),
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    ))

    fig.update_layout(
        xaxis_rangeslider_visible='False' in value
    )

    return fig

def main():
    app.run_server(debug=True)

if __name__ == '__main__':
    main()