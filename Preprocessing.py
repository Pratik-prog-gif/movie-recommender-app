import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

df = pickle.load(open('movie.pkl', 'rb'))

vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['tags'].astype(str))

model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(X)

distances, indices = model.kneighbors(X, n_neighbors=6)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('neighbors_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('neighbors_indices.pkl', 'wb') as f:
    pickle.dump(indices, f)
with open('movies_df.pkl', 'wb') as f:
    pickle.dump(df, f)

