# Movie Recommender System

This project is a content-based movie recommendation system built with Python and Streamlit. It allows users to receive movie suggestions based on a selected title using textual features such as genres, cast, crew, and keywords.

Live application: [Visit the Streamlit App](https://movie-recommender-appz.streamlit.app/)

---

## Dataset

The system is powered by a comprehensive dataset of over 45,000 movies, sourced from Kaggle:

**Dataset**: [The Movies Dataset – Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

This dataset includes metadata such as movie titles, release dates, language, cast, crew, genres, and plot keywords. It serves as the foundation for building the recommendation engine.

---

## Features and Methodology

### Data Preprocessing

- Merged metadata fields such as genres, keywords, cast, crew, and overview into a unified `tags` column.
- Extracted director names from the crew data and the top three cast members for each movie.
- Applied basic text normalization and cleaning techniques.
- Saved the processed dataset for model training and inference.

### Model Building

- Used TF-IDF vectorization to convert textual information into numerical vectors.
- Trained a Nearest Neighbors model using cosine similarity to identify similar movies.
- Retrieved the top five most similar movie titles for any selected input.

Artifacts saved include:
- `vectorizer.pkl`
- `neighbors_model.pkl`
- `neighbors_indices.pkl`
- `movies_df.pkl`

---

## Streamlit Web Application

The application provides an intuitive interface where users can select a movie and view a list of similar titles along with their posters. The app utilizes the OMDb API to fetch movie posters dynamically.

Key components:
- Dropdown for movie title selection
- Recommendations displayed in a clean, multi-column layout
- Poster images fetched via HTTP requests to the OMDb API

---

## Folder Structure

```
movie-recommender/

  # movie-recommender.ipynb    -> Preprocessing notebook
  # streamlit_app.py           -> Streamlit app script
  # movie.pkl                  -> Raw processed movie data
  # movies_df.pkl              -> Final DataFrame used in app
  # neighbors_model.pkl        -> Trained NearestNeighbors model
  # neighbors_indices.pkl      -> Similar movie indices
  # vectorizer.pkl             -> TF-IDF vectorizer
  # README.md                  -> Project documentation
```

---



## Credits

- Dataset: [The Movies Dataset – Kaggle (rounakbanik)](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- Poster retrieval via [OMDb API](http://www.omdbapi.com/)
- Application built using the [Streamlit](https://streamlit.io/) framework

---

## Future Enhancements

- Incorporate collaborative filtering using user ratings
- Improve title matching with fuzzy search capabilities
- Add additional filters such as genre, release year, and language
- Integrate additional content like movie trailers or synopses
