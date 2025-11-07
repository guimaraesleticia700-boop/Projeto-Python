import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("material/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("material/datasets/Top-100 Trending Books.csv")

st.write(df_reviews)

dfFiltrado = df_reviews[df_reviews["reviewer rating"] > 4]
dfTopBooks = df_top100_books[df_top100_books["book price"] < 50]

priceMax = dfTopBooks["book price"].max()
priceMin = dfTopBooks["book price"].min()

price_slider = st.slider(
    "Selecione o preço máximo",  # Texto exibido acima do slider
    min_value=int(priceMin),     # Valor mínimo
    max_value=int(priceMax),     # Valor máximo
    value=int(priceMax)          # Valor inicial
)

fig = px.bar(df_top100_books['year of publication'].value_counts())
fig2 = px.histogram(df_top100_books, x='book price')

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

