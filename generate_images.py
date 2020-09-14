import pandas
import plotly.graph_objects as go
import os
from datetime import datetime

# This script generates images of plots to create a GIF of your typeracer stats over time.
# Check https://github.com/varkon256/type-racer-scraper for more information.

# CSV_PATH: (string) path to the csv file containing the typing stats.
# Example: /Users/kondavarsha/Documents/Python/type-racer-graph-pretty/output.csv
CSV_PATH = ''
df = pandas.read_csv(CSV_PATH)

# IMAGE_PATH: (string) path to folder where the images will be output.
# Example : /Users/kondavarsha/Documents/Python/type-racer-graph-pretty/images/
IMAGE_PATH = ''

for i in range(1, len(df['Race #'] + 1)):
    datetime_obj = datetime.strptime(df["Date"][i], "%m/%d/%y")
    fig = go.Figure(
        data=go.Scatter(
            y = df['Speed'][0:i],
            x = df['Race #'][0:i],
            mode = 'markers',
            marker=dict(
                size=8,
                color=df['Accuracy'], #set color equal to a variable
                colorscale='Magma', # one of plotly colorscales
                showscale=True,
                colorbar=dict(title="Accuracy")
            )
        )
    )
    fig.update_layout({
        "title": {"text": "Speed in Races over time (2016-2019)"},
        "xaxis": {"title": "Race #"},
        "yaxis": {"title": "Speed (WPM)"}
    })
    fig.update_layout(
    annotations=[
        go.layout.Annotation(
            x=1,
            y=1,
            xref = 'paper',
            yref = 'paper',
            xanchor = 'right',
            yanchor = 'top',
            text = datetime_obj.strftime("%B %Y"),
            font = go.layout.annotation.Font(size = 20),
            showarrow=False
        )
    ]
    )
    fig.write_image(IMAGE_PATH + ("fig%s.jpeg" % i))