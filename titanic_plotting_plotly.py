""" plots useful information about titanic-dataset
"""
# pylint: disable=too-many-locals
from plotly.offline import iplot


import plotly.express as px
import plotly.graph_objs as go

import pandas as pd

# colours
import colorlover as cl

def main():
    """ main-function
    """

    # importing the training dataset
    train_df = pd.read_csv('data/train.csv')

    # plotting gender
    fig = px.bar(train_df, x='Sex')
    fig.show()

    # sex against survived
    fig2 = px.bar(train_df, x='Sex', y='Survived')
    fig2.show()

    # Pclass against survived
    fig3 = px.bar(train_df, x='Pclass', y='Survived')
    fig3.show()

    # parch against survived
    fig4 = px.bar(train_df, x='Parch', y='Survived',
                  color_discrete_sequence=px.colors.qualitative.G10)
    fig4.show()

    fig5 = px.bar(train_df, x='Embarked', y='Survived')
    fig5.show()

    # survived vs. not survived by age/Pclass

    # dataframes with age and Pclass, seperated by Survived
    df_age_plcass_not_survived = train_df.loc[train_df['Survived'] == 0, ['Age', 'Pclass']]
    df_age_plcass_survived = train_df.loc[train_df['Survived'] == 1, ['Age', 'Pclass']]

    # age-list of not-survived, seperated by Pclass
    age_not_survived_p1 = df_age_plcass_not_survived[df_age_plcass_not_survived.Pclass == 1]['Age']
    age_not_survived_p2 = df_age_plcass_not_survived[df_age_plcass_not_survived.Pclass == 2]['Age']
    age_not_survived_p3 = df_age_plcass_not_survived[df_age_plcass_not_survived.Pclass == 3]['Age']

    # age-list of survived, seperated by Pclass
    age_survived_p1 = df_age_plcass_survived[df_age_plcass_survived.Pclass == 1]['Age']
    age_survived_p2 = df_age_plcass_survived[df_age_plcass_survived.Pclass == 2]['Age']
    age_survived_p3 = df_age_plcass_survived[df_age_plcass_survived.Pclass == 3]['Age']

    # colors
    color = cl.scales['9']['seq']['BuPu']

    # defining all traces
    trace1 = go_hist_trace(data=age_not_survived_p1, name='Pclass 1 Not Survived', colour=color[2])
    trace2 = go_hist_trace(data=age_not_survived_p2, name='Pclass 2 Not Survived', colour=color[3])
    trace3 = go_hist_trace(data=age_not_survived_p3, name='Pclass 3 Not Survived', colour=color[4])
    trace4 = go_hist_trace(data=age_survived_p1, name='Pclass 1 Survived', colour=color[6])
    trace5 = go_hist_trace(data=age_survived_p2, name='Pclass 2 Survived', colour=color[7])
    trace6 = go_hist_trace(data=age_survived_p3, name='Pclass 3 Survived', colour=color[8])

    # plot histogramm with all traces
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(barmode='overlay',
                    title='Survived vs not survived by age/Pclass',
                    xaxis=dict(title='Survival ratio'),
                    yaxis=dict(title='Count'),
                    )
    fig6 = dict(data=data, layout=layout)
    iplot(fig6)

    # survived vs not survived by age

    # age of all survived and not survived
    age_survived = train_df[train_df.Survived == 1]['Age']
    age_not_survived = train_df[train_df.Survived == 0]['Age']

    # traces of age from the survived/not-survived
    trace8 = go_hist_trace(data=age_survived, name='Survived',
                           colour='rgba(171, 50, 96, 0.6)')
    trace9 = go_hist_trace(data=age_not_survived, name='Not survived',
                           colour='rgba(12, 50, 196, 0.6)')

    # plot histogramm with both traces
    data2 = [trace8, trace9]
    layout2 = go.Layout(barmode='overlay',
                        title='Survived vs not survived by age',
                        xaxis=dict(title='Survival ratio'),
                        yaxis=dict(title='Count'),
                    )
    fig7 = dict(data=data2, layout=layout2)
    iplot(fig7)

def go_hist_trace(data, name, colour='rgba(171, 50, 96, 0.6)'):
    """ hist trace
    """
    trace = go.Histogram(x=data,
                        opacity=0.75,
                        name=name,
                        xbins=dict(start=0,
                                    end=80,
                                    size=4
                                    ),
                        autobinx=False,
                        marker=dict(color=colour))
    return trace

if __name__ == "__main__":
    main()
