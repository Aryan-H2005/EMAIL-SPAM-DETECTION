import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

stop_words = set(stopwords.words('english'))

# Clean function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Spam Email Detection")
st.write("Check whether a message is Spam or Not")

# Session state for text
if "text" not in st.session_state:
    st.session_state.text = ""

# Example buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🚨 Try Spam Example"):
        st.session_state.text = "Congratulations! You won a free prize. Call now!"

with col2:
    if st.button("✅ Try Normal Example"):
        st.session_state.text = "Hey, are we meeting tomorrow?"

# Text input
user_input = st.text_area(
    "Enter your message:",
    value=st.session_state.text,
    height=150
)

# Predict
if st.button("🚀 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])

        prediction = model.predict(vectorized)[0]
        prob = model.predict_proba(vectorized)[0][1]

        st.divider()

        st.write("🧹 Cleaned Text:", cleaned)

        if prediction == 1:
            st.error(f"🚨 Spam Detected (Confidence: {prob:.2f})")
        else:
            st.success(f"✅ Not Spam (Confidence: {1 - prob:.2f})")