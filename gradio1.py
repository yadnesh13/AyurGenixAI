import gradio as gr
import pandas as pd
import pickle
from xgboost import XGBClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Load the model and data
def load_model_and_data():
    # Load the pickle file
    with open('data.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load the model
data = load_model_and_data()

# Setup your model and vectorizer based on the loaded data
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
ml_model = XGBClassifier()

# Assuming you have the model saved in some way or train it here
# (you might want to save the model separately to avoid retraining)
# Example: ml_model = pickle.load(open("model.pkl", "rb"))

# Gradio Interface
def predict_disease(symptoms):
    # Transform the user input using the trained TF-IDF vectorizer
    user_input_tfidf = tfidf_vectorizer.transform([symptoms])
   
    # Predict the disease using the trained model
    predicted_class = ml_model.predict(user_input_tfidf)
   
    # Assuming le is your LabelEncoder instance
    predicted_disease = le.inverse_transform(predicted_class)
    return predicted_disease[0]

iface = gr.Interface(fn=predict_disease, inputs="text", outputs="text")
iface.launch()