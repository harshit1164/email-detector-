# 🎯 Phishing Email Detection – End-to-End Machine Learning Project

Hi! I'm excited to share my project built for the hackathon — a simple and powerful **Phishing Email Detection System** that works straight from your terminal. 🚀

---

## 💡 Why I Built This

Phishing attacks are one of the most common cybersecurity threats  today. They trick users into clicking dangerous links or giving away sensitive information.

I wanted to build a tool that could:
- Read raw email content
- Analyze it using machine learning
- Predict instantly whether it's **PHISHING** or **LEGIT**

---

## 🧠 How It Works (Overview)

Here’s how I built it:

1. **Collected and cleaned a dataset** of spam and ham (non-spam) emails
2. **Converted email text into numerical features** using TF-IDF vectorization
3. **Trained a Random Forest model** to classify phishing vs legit emails
4. **Built a real-time terminal tool** to allow users to test email content instantly

Let’s walk through each part.

---

## 📊 Dataset and Preprocessing (`preprocess.py`)

- I started with the classic `spam.csv` dataset which includes thousands of labeled messages.
- I cleaned it up, renamed columns (`v1` → `label`, `v2` → `text`) and mapped labels like:
  - `spam` or `phishing` → 1
  - `ham` or `legit` → 0

Then I used `TfidfVectorizer` to extract up to 5000 important features from each email.

Once done, I saved the vectors and labels into a file called `preprocessed.pkl` so they can be reused for training.

---

## 🔍 Training the Model (`train.py`)

- I loaded the preprocessed data and trained a **Random Forest Classifier**.
- After training, I evaluated the model with precision, recall, and F1-score.
- I saved the trained model and vectorizer to `phishing_detector.pkl` for easy use during prediction.

📂 All saved models go into a folder called `/data`.

---

## 🧪 Real-Time Email Prediction (`predict.py`)

This is the fun part!

- Just run the script, paste your email content, and the model will tell you if it's **PHISHING** or **LEGIT** in real-time.
- It uses a probability threshold: anything above **0.4** is considered phishing.

```bash
$ python predict.py

Paste the email content (or type 'exit' to quit):
👉 Your account has been suspended. Click here to verify now.

Result: PHISHING

Paste the email content (or type 'exit' to quit):
👉 Hey team, please review the attached project report.

Result: LEGIT
⚙️ Tech Stack
Python 3

scikit-learn
pandas
numpy

TF-IDF for feature extraction

Random Forest Classifier

📦 Folder Structure
bash
Copy
Edit
├── spam.csv                 # Dataset
├── preprocess.py            # Text cleaning and vectorization
├── train.py                 # Model training and saving
├── predict.py               # Real-time terminal-based prediction
├── preprocessed.pkl         # Saved training data
├── requirements.txt         # Install dependencies
└── data/
    └── phishing_detector.pkl  # Trained model + vectorizer
Demo Video

🔽 The demo video is included in this repository as `demo.mp4`.  
Please click **"View Raw"** to download and watch it:  
👉 [Click here to download and watch](./demo.mp4)

🤝 Want to Contribute?
Fork it, try a different model, or use a larger dataset. Pull requests are welcome!

👤 Author
HARSHIT TIWARI

Thanks for reading! Hope this helps keep inboxes safe and spam-free. 🛡️📬

