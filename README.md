# Sarcasm Detector

## Overview

This project demonstrates the use of machine learning to detect sarcasm in text. The sarcasm detection model is built using Python, leveraging libraries such as Pandas, NumPy, and scikit-learn. The dataset used for training and testing the model consists of headlines labeled as sarcastic or non-sarcastic. The model is trained using the Bernoulli Naive Bayes algorithm and achieves an accuracy of approximately 84%.

Additionally, a simple web application is built using Streamlit to provide an interactive interface for users to input text and receive predictions on whether the text is sarcastic or not.

## Tech Stack

- **Python**: Core programming language for development.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **scikit-learn**: Machine learning library for text vectorization and model training.
- **Streamlit**: Framework for building and deploying the web application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Sarcasm-Detector.git
    cd Sarcasm-Detector
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Enter a text in the web interface to check if it is sarcastic.

## Dataset

The dataset used for this project consists of headlines labeled as sarcastic or non-sarcastic. It is sourced from Kaggle and can be downloaded from [here](https://www.kaggle.com).

## How It Works

1. **Data Preparation**: The dataset is loaded and the relevant columns are selected.
2. **Text Vectorization**: The headlines are converted into numerical features using `CountVectorizer`.
3. **Model Training**: A Bernoulli Naive Bayes model is trained on the transformed data.
4. **Prediction**: The trained model predicts whether a given text is sarcastic or not based on the input provided in the web app.

## Example
Enter a Text: Cows lose their jobs as milk prices drop
Output: Sarcasm
---

<p align="center">
  <img src="path/to/your/favicon.ico" alt="Sarcasm Detector" width="100" height="100">
</p>
