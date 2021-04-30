import pandas as pd
import plotly.graph_objs as go

train_df = pd.read_csv('data/sentiment_analysis/train.tsv', sep="\t")

def return_figures():

    #train_df = pd.read_csv('data/sentiment_analysis/train.tsv', sep="\t")
    graph_two = []

    class_count = train_df['Sentiment'].value_counts()
    x = class_count.index.tolist()
    y = class_count.values.tolist()

    graph_one = []


    graph_one.append(
        go.Pie(
            labels = x,
            values = y,
        )
    )

    layout_one = dict(title = 'Distribution of sentiments')

    # second chart plots ararble land for 2015 as a bar chart



    graph_two.append(
        go.Bar(
            x = x,
            y = y,
        )
    )

    layout_two = dict(title = 'Number of reviews per sentiment',
                      xaxis = dict(title = 'Sentiment',),
                      yaxis = dict(title = 'Number of reviews'),
                      )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))


    return figures


def return_figures_first():

    #train_df = pd.read_csv('data/sentiment_analysis/train.tsv', sep="\t")
    graph_two = []

    class_count = train_df['Sentiment'].value_counts()
    x = class_count.index.tolist()
    y = class_count.values.tolist()

    graph_one = []


    graph_one.append(
        go.Pie(
            labels = x,
            values = y,
        )
    )

    layout_one = dict(title = 'Distribution of tests')

    # second chart plots ararble land for 2015 as a bar chart



    graph_two.append(
        go.Bar(
            x = x,
            y = y,
        )
    )

    layout_two = dict(title = 'Number of reviews per test',
                      xaxis = dict(title = 'Test',),
                      yaxis = dict(title = 'Number of numbers'),
                      )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))


    return figures

def return_figures_second():

    #train_df = pd.read_csv('data/sentiment_analysis/train.tsv', sep="\t")
    graph_two = []

    class_count = train_df['Sentiment'].value_counts()
    x = class_count.index.tolist()
    y = class_count.values.tolist()

    graph_one = []


    graph_one.append(
        go.Pie(
            labels = x,
            values = y,
        )
    )

    layout_one = dict(title = 'Second')

    # second chart plots ararble land for 2015 as a bar chart



    graph_two.append(
        go.Bar(
            x = x,
            y = y,
        )
    )

    layout_two = dict(title = 'Number of reviews per second',
                      xaxis = dict(title = 'Test',),
                      yaxis = dict(title = 'Number of numbers'),
                      )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))


    return figures



