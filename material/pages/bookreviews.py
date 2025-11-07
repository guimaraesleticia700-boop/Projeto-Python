import streamlit as st

import pandas as pd
import plotly.express as px

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Escolha um livro", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_filtered = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.write(f"**Gênero:** {book_genre}")
st.write(f"**Preço:** ${book_price:.2f}")
st.write(f"**Avaliação:** {book_rating}/5")
st.write(f"**Ano de Publicação:** {book_year}")

st.write("---")
for _, review in df_reviews_filtered.iterrows():
    st.write(f"**Usuário:** {review['reviewer']}")
    st.write(f"**Título:** {review['review title']}")
    st.write(f"**Comentário:** {review['review description']}")
    st.write("---")