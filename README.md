This project is a content-based movie recommendation system that suggests movies similar to a selected movie based on tags, genres, and descriptions.
It uses CountVectorizer to convert movie tags into numeric vectors and cosine similarity to calculate how similar movies are to each other.

Features

Recommends top-N similar movies based on a selected movie.

Converts textual tags into numeric vectors for computation.

Computes similarity between movies using cosine similarity.

Allows exporting the similarity model for faster predictions in future.

Can be extended with a web interface using Streamlit.

Technologies Used

Python 3

Pandas – Data handling and manipulation

Scikit-learn – CountVectorizer, cosine similarity

NumPy – For numerical operations

Pickle – Save and load similarity matrix

Streamlit (Optional) – For building a web-based interface

Project Workflow

Data Collection & Preprocessing: Load movie dataset and clean the tags/genres.

Feature Extraction: Convert movie tags into numeric vectors using CountVectorizer.

Similarity Computation: Calculate pairwise similarity between movies using cosine similarity.

Recommendation Engine: For a selected movie, return the top-N most similar movies.

Export Model: Save similarity matrix for quick future recommendations.
