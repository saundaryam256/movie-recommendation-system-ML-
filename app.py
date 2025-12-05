import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl

st.title("Movie Recommendation System")

df = pd.read_csv('cleaned_dataa.csv')  # Assuming a CSV file with movie data
similarity = pkl.load(open('similarity.pkl', 'rb'))  # Assuming a pickle file with similarity matrix

#Lets write function get name of movie by index
def get_name_by_index(i):
    if i < len(df) and i >= 0:
        return df.loc[i, 'title']
    else:
        return ''

#Lets write function to get index from movie name
def get_index_from_name(name):
    found_index = -1
    for i in df.index:
        if df.loc[i, 'title'].strip().lower() == name.strip().lower():
            found_index = i
            break
    return found_index

name = st.selectbox("Select movie you watched:", df['title'].values)
if st.button("Recommend"):
    index = get_index_from_name(name)
    if index != -1:
        similarity_indexes =  list(enumerate(similarity[index]))
        similarity_indexes = sorted(similarity_indexes, key=lambda x: x[1], reverse=True)
        st.success("You must watch following movies:")
        for i in range(1, 6):
            st.write(i, ":", get_name_by_index(similarity_indexes[i][0]))
    else:
        st.error("Movie Not Found")    
