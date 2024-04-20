import pickle
from sentence_transformers import SentenceTransformer

# Load the model from the file when your application starts
with open("embeddings_model.pkl", "rb") as f:
    model = pickle.load(f)

def get_embeddings(text):
    return model.encode(text)