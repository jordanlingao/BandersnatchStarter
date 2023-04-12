'''This module holds a function to generate a graph using altair.'''
from altair import Chart, Tooltip, X, Y, TitleParams
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

    vis = Chart(df.drop(columns="_id"),
                title=TitleParams(
                    f"{y} by {x} for {target}", fontSize=25),
                width=400,
                height=450,
                padding=50,
                background="#eeeeee").mark_circle(size=60).encode(
        x=X(x),
        y=Y(y),
        color=target,
        tooltip=Tooltip(df.drop(columns="_id").columns.to_list()))

    return vis
