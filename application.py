from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import plotly.express as px


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

app = Dash(__name__)
application = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

print(df.head())

fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


mapBoxKey = 'pk.eyJ1IjoibWlrZXF1YW4iLCJhIjoiY2psMzBuNW05MDJ4bDNxcngzdmZqa3R3diJ9.8sYaudSMNUutIvkKwqJS0Q'

mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"

app.layout = html.Div(children=[
    html.H1(children='Test Platform'),

    dcc.Graph(
        id='example-graph',
        figure=fig,
    ),
    
    




  
])



if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
