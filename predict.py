import pickle

with open('data/phishing_detector.pkl', 'rb') as f:
    saved = pickle.load(f)


model = saved['model']
vectorizer = saved['vectorizer']

while True:
    email = input("Paste the email content (or type 'exit' to quit):\n")
    if email.lower() == 'exit':
        break
    email_vec = vectorizer.transform([email])
    prob = model.predict_proba(email_vec)[0][1]  
    print("PHISHING" if prob > 0.4 else "LEGIT")


