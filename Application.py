import streamlit as st
import pickle
import requests


df = pickle.load(open('movies_df.pkl', 'rb'))
indices = pickle.load(open('neighbors_indices.pkl', 'rb'))

st.title('Movie Recommender System')

movie_titles = df['title'].values
selected_movie = st.selectbox('Type the Movie Title', movie_titles)


def get_posters(movie_title):
    url = f'http://www.omdbapi.com/?apikey=b535b379&t={movie_title}'
    response = requests.get(url)
    data = response.json()

    return data.get('Poster', 'https://via.placeholder.com/150?text=No+Image')


def get_recommendations(movie_name):
    index_list = df.index[df['title'].str.lower() == movie_name.lower()].tolist()
    if not index_list:
        return f"Movie '{movie_name}' not found in the dataset."

    recommendations = []
    posters = []
    index = index_list[0]
    similar_indices = indices[index][1:]

    for idx in similar_indices:
        title = df['title'].iloc[idx]
        recommendations.append(title)
        posters.append(get_posters(title))
    return recommendations, posters


if st.button('Recommend Movie'):
    result = get_recommendations(selected_movie)
    if isinstance(result, tuple):
        recommendations, posters = result

        cols=st.columns(len(recommendations))
        for col,movie, poster in zip(cols,recommendations, posters):
            col.write(movie)
            col.image(poster, width=150)
    else:
        st.write(result)

