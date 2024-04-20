import numpy as np
import pandas as pd
import streamlit as st
from get_embeddings import get_embeddings
from sklearn.metrics.pairwise import cosine_similarity

# Load data
song_embeddings_2d = np.load('Song_Embeddings.npy')
df = pd.read_csv('Labeled_Song_Dataset.csv')

# Function to recommend songs
def recommend_songs(user_query=None, label=None, num_songs=25,song_embeddings_2d=song_embeddings_2d):
    if user_query != "":
        query_embedding = get_embeddings(user_query)
        query_embedding_2d = query_embedding.reshape(1, -1)
    else:
        if label == 'All Themes':
            return []
        query_embedding_2d = np.random.rand(1, 384)
    
    if label != "All Themes":
        filtered_df = df[df['kmeans_label_text'] == label]
        if filtered_df.empty:
            return []
        song_embeddings_2d = song_embeddings_2d[filtered_df.index]
    else:
        filtered_df = df
    
    similarity_scores = cosine_similarity(query_embedding_2d, song_embeddings_2d)
    top_recommendations = np.argsort(similarity_scores.flatten())[::-1][:num_songs]
    
    recommendations = []
    for i in top_recommendations:
        song_title = filtered_df['song'].iloc[i]
        artist = filtered_df['artist'].iloc[i]
        recommendations.append((song_title, artist))
    return recommendations


# Streamlit UI
st.title('Build a Playlist!')
labels = ['All Themes'] + df['kmeans_label_text'].unique().tolist()
selected_label = st.selectbox("Select a theme for your playlist:", labels)
user_query = st.text_input("Give some input for your playlist:")


recommendations = recommend_songs(user_query=user_query,label=selected_label)


if len(recommendations) > 0:
    st.markdown("#### **Top recommended songs:**/n *Click on the song to listen to it!*")
    for song, artist in recommendations:
        text = song + " by " + artist
        # link_text = "https://open.spotify.com/search/" + text
        link_text = "https://music.youtube.com/search?q=" + text.replace(" ", "+")
        st.page_link(link_text, label=text)

