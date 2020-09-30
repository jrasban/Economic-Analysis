import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
from plotly import graph_objs as go
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


'''Unemployment'''
dataset = pd.read_csv('StateUnemployment.csv')
dataset.rename(columns={'Unnamed: 0':'StateUnemp'},inplace=True)
dataset['State'] = dataset['StateUnemp'].str[:-2]
dataset.set_index('State',inplace=True)
dataset.reset_index(inplace=True)
dataset.columns = [*dataset.columns[:-1], 'Newest Values']
data = dict(type='choropleth'
            ,locations=dataset['State']
           ,locationmode='USA-states'
           ,colorscale='Portland'

            ,z=dataset['Newest Values']
           ,colorbar={'title':'Unemployment Scale'}
)

layout =dict(title= 'Unemployment by State', geo={'scope':'usa'})
choromap = go.Figure(data, layout)


'''T-Bills 10Y2Y Spread'''
data = pd.read_excel('t10y2y.xlsx')
t10y2y = px.line(data, x="index", y="Difference", title='10Y2Y T-bills')
'''T-Bills 10Y3M Spread'''
data = pd.read_excel('t10y3m.xlsx')
t10y3m = px.line(data, x="index", y="Difference", title='10Y2Y T-bills')
'''CPI'''
data = pd.read_excel('CPI.xlsx')
fig2= px.bar(data, x='Unnamed: 0', y='m_pct_change')
'''PMI'''
data = pd.read_excel('PMI.xlsx')
fig3 = px.bar(data,x='Date',y='PMI')
'''HOUSING STARTS'''
data = pd.read_excel('HousingStarts.xlsx')
housing = px.line(data, x="Unnamed: 0", y="HOUST", title='HousingStarts')




app.layout = html.Div(
    children=[
    html.H1(children='Economic Indicators Dashboard'),
    html.H2(children='Unemployment'),
    # html.Div(children='''
    #     Unemployment
    #     '''),

    dcc.Graph(
        id='example-graph',
        figure=choromap
    ),
    html.H2(children='10Y2Y T-Bill Spread'),
    dcc.Graph(
        id='t10y2y',
        figure=t10y2y
    ),
    html.H2(children='10Y3M T-Bill Spread'),
    dcc.Graph(
        id='t10y3m',
        figure=t10y3m
    ),
    html.H2(children='Consumer Price Index'),
    dcc.Graph(
        id='example-graph3',
        figure=fig2
    ),
    html.H2(children='Purchasing Managers Index'),
    dcc.Graph(
        id='example-graph4',
        figure=fig3
    ),
    html.H2(children='United States Housing Starts'),
    dcc.Graph(
        id='housingstarts',
        figure=housing
    )


])

if __name__ == '__main__':
    app.run_server(debug=True)