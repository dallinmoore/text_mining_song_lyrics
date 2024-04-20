# Playlist Recommender App

This is a Streamlit web application for generating song recommendations based on user input or selected theme. The app utilizes song embeddings and cosine similarity to suggest songs that are similar to the user's query or belong to a specific theme, and clustering with KMeans to divide the songs into 20 distinct themes.

## How to Use

1. **Select a Theme**: Choose a theme from the dropdown menu. You can choose from the list of themes or select 'All Themes' to get recommendations from all themes if you provide input.

2. **Provide Input**: Optionally, you can input some text to refine your playlist.

4. **Listen on Spotify/YT Music**: Once recommendations are generated, you can click on the song titles to open them directly and listen to them.

## Access the App Online

You can access the app online through [https://textminingsonglyrics.streamlit.app/](https://textminingsonglyrics.streamlit.app/). Simply click the link to visit the web application and start building your playlist right away! 🎵

## Installation

To run this app locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/dallinmoore/text_mining_song_lyrics.git
```

2. Navigate to the project directory:

```bash
cd ext_mining_song_lyrics
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run main.py
```

## Data

The app utilizes song embeddings and a labeled song dataset. The song embeddings are loaded from the file `Song_Embeddings.npy`, while the labeled song dataset is loaded from `Labeled_Song_Dataset.csv`.

## Dependencies

- NumPy
- Pandas
- Streamlit
- SciKit-Learn
- Sentence-Transformers
- Torch
- Transformers

## Credits

- This app is developed by Dallin Moore.
- The song embeddings are generated using SBERT.
- The labeled song dataset is sourced from a subset of Million Song Dataset.

