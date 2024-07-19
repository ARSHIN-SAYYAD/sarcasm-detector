# save_model.py
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

# Assuming these variables are defined after training
cv = CountVectorizer()
model = BernoulliNB()

# Save the model and vectorizer
joblib.dump(cv, 'vectorizer.pkl')
joblib.dump(model, 'sarcasm_model.pkl')
