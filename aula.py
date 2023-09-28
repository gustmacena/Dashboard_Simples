from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Grafico com o faturamento de todos os produtos separados por loja'),
    html.Div(children='''
        Obs: Esse grafico mostra a quantidade de produtos vendidos
    '''),
   
    dcc.Dropdown(opcoes, value='Todas as Lojas',id='lista_lojas'),
    
    dcc.Graph(
        id='grafico_quantidade_de_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_de_vendas', 'figure'),
    Input('lista_lojas', 'value'),
)
def update_output(value):
    if value == "todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)