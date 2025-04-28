import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


with open('preprocessed.pkl', 'rb') as f:
    data = pickle.load(f)

X_train = data['X_train']
y_train = data['y_train']
X_test = data['X_test']
y_test = data['y_test']


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['LEGIT', 'PHISHING']))
import os

os.makedirs('data', exist_ok=True)  

with open('data/phishing_detector.pkl', 'wb') as f:
    pickle.dump({
        'model': model,
        'vectorizer': data['vectorizer']
    }, f)
