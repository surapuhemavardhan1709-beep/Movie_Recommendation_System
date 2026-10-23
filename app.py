import streamlit as st
import pickle
import requests

# Load saved files
movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API key
API_KEY = "753418bccc7ed79b56092369641228b0"


# Function to get movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

    return None


# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

# Title
st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get 5 similar movie recommendations.")

# Movie selection
selected_movie = st.selectbox(
    "Choose a movie:",
    movies['title'].values
)

# Recommend button
if st.button("Recommend Movies"):

    index = movies[movies['title'] == selected_movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    st.subheader("🍿 Recommended Movies")

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_name = movies.iloc[i[0]].title

        poster = fetch_poster(movie_id)

        st.write(f"### {movie_name}")

        if poster:
            st.image(poster, width=200)
        else:
            st.write("Poster not available.")