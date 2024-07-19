import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import joblib

def prepare_data(file_path='Sarcasm.json'):
    """Load and prepare the dataset."""
    data = pd.read_json(file_path, lines=True)
    data['is_sarcastic'] = data['is_sarcastic'].map({0: 'Not Sarcastic', 1: 'Sarcastic'})
    data = data[['headline', 'is_sarcastic']]
    x = np.array(data['headline'])
    y = np.array(data['is_sarcastic'])
    return x, y

def train_model(x, y):
    """Train the Bernoulli Naive Bayes model and save it along with the vectorizer."""
    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    model = BernoulliNB()
    model.fit(X_train, y_train)
    
    # Save the model and vectorizer
    joblib.dump(cv, 'vectorizer.pkl')
    joblib.dump(model, 'sarcasm_model.pkl')
    
    return cv, model

def detect_sarcasm(text):
    """Detect sarcasm in the provided text."""
    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('sarcasm_model.pkl')
    text_vector = vectorizer.transform([text]).toarray()
    prediction = model.predict(text_vector)
    return "Sarcastic" if prediction[0] == "Sarcastic" else "Not Sarcastic"

if __name__ == "__main__":
    x, y = prepare_data()
    train_model(x, y)
