# Playlist Recommender App

For my final project in my Text Mining class, I built a Streamlit web app for generating song recommendations based on user input and/or selected theme. The app utilizes song embeddings and cosine similarity to suggest songs that are similar to the user's query, and clustering with KMeans to divide the songs into 20 distinct themes.

## Project Structure

The project was initially developed and explored in `Project_Exploration_Creation.ipynb`. This notebook contains:
- Data preprocessing and cleaning steps
- Generation of song embeddings using SBERT
- Clustering analysis and theme generation
- Initial exploration and testing of the recommendation system

The processed data and embeddings were saved to static files (`Song_Embeddings.npy` and `Labeled_Song_Dataset.csv`) to optimize the web app's performance. This means when running `main.py`, no preprocessing or embedding generation is needed as it works with the pre-computed data.

## How to Use

1. **Select a Theme**: Choose a theme from the dropdown menu. You can choose from the list of themes or select 'All Themes' to get recommendations from all themes if you provide input. 

2. **Provide Input**: Input text into the textbox to refine your playlist, or leave it blank for a random subset of songs from the selected theme.

4. **Listen on Spotify/YT Music**: Once recommendations are generated, you can click on the song titles to open them directly and listen to them. (The code can be edited for options linking to Spotify/YT Music.)

## Access the App Online

You can access the app online through [textminingsonglyrics.streamlit.app/](https://textminingsonglyrics.streamlit.app/).

## Installation

To run this app locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/dallinmoore/text_mining_song_lyrics.git
```

2. Navigate to the project directory:

```bash
cd text_mining_song_lyrics
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

The app utilizes pre-computed song embeddings and a labeled song dataset:
- `Song_Embeddings.npy`: Contains pre-computed SBERT embeddings generated during the initial analysis
- `Labeled_Song_Dataset.csv`: Contains the cleaned and processed song dataset with theme labels

These files are the result of the processing steps in the Jupyter notebook and are used directly by the Streamlit app for efficient performance.

## Credits

- This app is developed by Dallin Moore.
- The song embeddings are generated using SBERT.
- The labeled song dataset is sourced from a subset of Million Song Dataset accessed [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs).

