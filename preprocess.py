import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


data = pd.read_csv('spam.csv', encoding='latin1')


if 'v1' in data.columns and 'v2' in data.columns:
    data = data.rename(columns={'v1': 'label', 'v2': 'text'})

data = data[['label', 'text']]


data['label'] = data['label'].map({'ham': 0, 'spam': 1, 'legit': 0, 'phishing': 1})


data = data.dropna(subset=['text', 'label'])


X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


with open('preprocessed.pkl', 'wb') as f:
    pickle.dump({
        'X_train': X_train_vec,
        'X_test': X_test_vec,
        'y_train': y_train,
        'y_test': y_test,
        'vectorizer': vectorizer
    }, f)

print("Preprocessing complete.")
