import streamlit as st
import pickle
import numpy as np

# Load data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# Title
st.title('Top 50 Books📚')

books_per_row = 4
top_n = 50  # Show top 50 books

for i in range(0, min(top_n, len(popular_df)), books_per_row):
    cols = st.columns(books_per_row)
    for j in range(books_per_row):
        if i + j < len(popular_df):
            with cols[j]:
                st.image(popular_df['Image-URL-M'].values[i + j], width=120)
                st.markdown(f"**{popular_df['Book-Title'].values[i + j]}**")
                st.markdown(f"Author: {popular_df['Book-Author'].values[i + j]}")
                st.markdown(f"Votes: {popular_df['num_ratings'].values[i + j]}")
                st.markdown(f"Avg Rating: {round(popular_df['avg_rating'].values[i + j], 2)}")

# Sidebar Recommendation System
st.sidebar.header("Get Book Recommendations")

user_input = st.sidebar.selectbox(
    "Select a book you like:",
    pt.index
)

if st.sidebar.button('Recommend'):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    st.sidebar.subheader("You might also like:")
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        book_title = temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0]
        book_author = temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0]
        book_image = temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]

        st.sidebar.image(book_image, width=100)
        st.sidebar.markdown(f"**{book_title}**")
        st.sidebar.markdown(f"_by {book_author}_")
        st.sidebar.markdown("---")
