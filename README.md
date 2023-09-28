# Projeto de Dashboard de Vendas

Este projeto é um aplicativo de painel de vendas construído usando Dash, uma estrutura Python para construção de aplicações web analíticas. O aplicativo exibe um gráfico de barras que mostra a quantidade de produtos vendidos, agrupados por loja.

## Como usar

1. **Instale as dependências necessárias**: Este projeto requer as bibliotecas Python Dash, Plotly e Pandas. Você pode instalá-las usando pip:

```bash
pip install dash plotly pandas
```

2. **Prepare seus dados**: Este aplicativo usa um arquivo Excel chamado "Vendas.xlsx" como fonte de dados. Certifique-se de que este arquivo está no mesmo diretório que o arquivo do aplicativo e que contém as colunas "Produto", "Quantidade" e "ID Loja".

3. **Execute o aplicativo**: Você pode executar o aplicativo usando o seguinte comando no terminal:

```bash
python app.py
```

4. **Acesse o aplicativo**: Após executar o aplicativo, você pode acessá-lo em seu navegador web em `http://127.0.0.1:8050/`.

## Descrição do Código

O código começa importando as bibliotecas necessárias e iniciando o aplicativo Dash.

Em seguida, ele lê os dados do arquivo Excel e cria um gráfico de barras usando Plotly Express.

O layout do aplicativo é definido usando componentes HTML e Dash Core. Ele consiste em um título, uma descrição, um menu suspenso para selecionar a loja e um gráfico para exibir os dados.

A função de retorno de chamada `update_output` é usada para atualizar a figura do gráfico com base na loja selecionada no menu suspenso.

Finalmente, o servidor do aplicativo é iniciado com a função `run`.
