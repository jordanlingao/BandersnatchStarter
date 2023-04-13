'''This module holds a function to generate a graph using altair.'''

from altair import Chart, Tooltip, X, Y, TitleParams, Color, Scale
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    '''
    Generates an altair Chart

    Parameters
    ----------
    df: DataFrame
        data to be graphed
    x: str
        column to go on x-axis
    y: str
        column to go on y-axis
    target: str
        column to be shown in color

    Returns
    -------
    vis: Chart
    '''

    vis = Chart(
        df,
        title=f"{y} by {x} for {target}"
    ).mark_circle(size=80).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=400,
        height=400,
        padding=50,
        background="#202020"
    ).configure(
        legend={
            "titleColor": "#D0D0D0",
            "labelColor": "#D0D0D0",
            "padding": 10
        },
        title={
            "color": "#D0D0D0",
            "fontSize": 25,
            "offset": 30
        },
        axis={
            "titlePadding": 20,
            "titleColor": "#D0D0D0",
            "labelPadding": 5,
            "labelColor": "#D0D0D0",
            "gridColor": "#C8C8C8",
            "tickColor": "#D0D0D0",
            "tickSize": 10
        },
        view={
            "stroke": "black"
        }
    )

    return vis
