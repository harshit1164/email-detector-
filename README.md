🚀 Quick Start
1. Preprocessing the Data
First, clean and vectorize the data:



2. Training the Model
Train the model on the preprocessed data:


Trains a Random Forest Classifier with 100 trees

Evaluates model using classification metrics (precision, recall, f1-score)

Saves the model and vectorizer to /data/phishing_detector.pkl

✅ Output: /data/phishing_detector.pkl

3. Making Predictions
Run the interactive prediction script:


Accepts email content via input

Predicts whether the email is PHISHING or LEGIT

Threshold: If phishing probability > 0.4 → PHISHING, else LEGIT

📊 Model Details
Algorithm: Random Forest Classifier

Text Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency)

Dataset: spam.csv (standard spam/ham dataset)

Performance Metrics: Precision, Recall, F1-Score (printed after training)

📦 Requirements
Install the required Python libraries:


📚 How It Works
Preprocessing

Remove missing values

Normalize labels

Convert text data into TF-IDF vectors

Training

Use Random Forest (good for handling text features and overfitting)

Model learns to distinguish between phishing and legit emails

Prediction

New emails are vectorized using the same TF-IDF vectorizer

Model outputs probability for phishing

📈 Example

Paste the email content (or type 'exit' to quit):
👉 "Congratulations! You've won a free iPhone. Click here to claim now."

🔎 Prediction: PHISHING



Paste the email content (or type 'exit' to quit):
👉 "Meeting scheduled at 3 PM regarding quarterly report."

🔎 Prediction: LEGIT




✨ Future Improvements
Add deep learning models like LSTM

Use word embeddings (Word2Vec, GloVe)

Deploy as a Flask web application

Add more phishing-specific datasets

👨‍💻 Author
Made with ❤️ by Harshit Tiwari
