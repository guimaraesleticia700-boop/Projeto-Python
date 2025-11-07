import streamlit as st #importando biblioteca streamlit

import pandas as pd #importando a biblioteca Pandas
import plotly.express as px #importando a biblioteca plotly, com express

st.set_page_config(layout="wide") #expandir a largura
 
df_reviews = pd.read_csv("material/datasets/customer reviews.csv") #variável reviews, o pd csv (le o arquivo csv, transforma em DataFrame)
df_top100_books = pd.read_csv("material/datasets/Top-100 Trending Books.csv") #variável top 100 books

st.write(df_reviews) #exibe o conteúdo do DataFrame de maneira interativa, estou usando streamlit

dfFiltrado = df_reviews[df_reviews["reviewer rating"] > 4]
dfTopBooks = df_top100_books[df_top100_books["book price"] < 50] #realizando um filtro, através do colchete

priceMax = dfTopBooks["book price"].max() #valor máximo da coluna
priceMin = dfTopBooks["book price"].min() #valor mínimo da coluna

price_slider = st.slider(
    "Selecione o preço máximo",  # Texto exibido acima do slider
    min_value=int(priceMin),     # Valor mínimo
    max_value=int(priceMax),     # Valor máximo
    value=int(priceMax)          # Valor inicial
)

fig = px.bar(df_top100_books['year of publication'].value_counts()) #o "bar" do tipo gráfico de barra
fig2 = px.histogram(df_top100_books, x='book price') #criando um histograma com plotly de preços

col1, col2 = st.columns(2) #organizando os gráficos em colunas
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

