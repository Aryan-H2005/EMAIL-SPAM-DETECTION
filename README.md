# 📧 Spam Email Detection System

🚀 **Live Demo:** https://aryan-spam-detector.streamlit.app/


## 🚀 Overview

An end-to-end **Spam Detection System** that classifies messages as **Spam or Not Spam** using Natural Language Processing (NLP) and Machine Learning.

The system processes raw text input, applies preprocessing techniques, and uses a trained model to predict whether the message is spam in real-time via an interactive Streamlit web application.

---

## 🎯 Problem Statement

Spam messages are a major issue in communication systems, leading to:

* Security risks (phishing, scams)
* Reduced productivity
* Poor user experience

This project aims to build an intelligent system to automatically filter spam messages.

---

## 🧠 Key Features

* 🔍 Text preprocessing (cleaning, stopword removal)
* 📊 TF-IDF vectorization with n-grams
* 🤖 Machine Learning model (Logistic Regression)
* ⚡ Real-time prediction using Streamlit
* 🎯 Confidence score for predictions
* 🎛️ Interactive UI with example inputs
* 🧹 Cleaned text visualization

---

## 🏗️ Tech Stack

* **Python**
* **Scikit-learn**
* **NLTK**
* **Streamlit**
* **Pandas**

---

## 📂 Project Structure

```
spam_project/
│── train.py              # Model training script
│── app.py                # Streamlit application
│── model.pkl            # Trained ML model
│── vectorizer.pkl       # TF-IDF vectorizer
│── spam.csv             # Dataset
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-H2005/spam-detection.git
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model

```bash
python train.py
```

### 4️⃣ Run the application

```bash
python -m streamlit run app.py
```

---

## 📊 Model Details

* **Algorithm:** Logistic Regression
* **Feature Extraction:** TF-IDF (unigrams + bigrams)
* **Dataset:** SMS Spam Dataset
* **Evaluation Metrics:**

  * Accuracy
  * Precision
  * Recall
  * F1-score

---

## 📈 Results

The model achieves strong performance on the test dataset with high precision and recall, making it effective for spam detection tasks.

---

## 🧪 Example Inputs

**Spam:**

> "Congratulations! You have won a free prize. Call now!"

**Not Spam:**

> "Hey, are we meeting tomorrow?"

---

## ⚠️ Limitations

* Works best on short text messages (SMS-like data)
* Does not handle complex phishing emails or HTML content
* Limited contextual understanding compared to deep learning models

---

## 🔥 Future Improvements

* Add multiple model comparison (Naive Bayes, Random Forest)
* Implement explainability (top contributing words)
* Upgrade to deep learning models (BERT)
* Deploy on cloud (Streamlit Cloud / AWS)
* Add real-time email API integration

---

## 📌 Conclusion

This project demonstrates a complete ML pipeline from data preprocessing to deployment, showcasing practical skills in NLP, machine learning, and web application development.

---

## 🙌 Author

Aryan Harke

---

## ⭐ If you found this useful, give it a star!
