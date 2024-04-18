import streamlit as st
import pickle 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
st.title("Texte arc-en-ciel clignotant")

# Embed the HTML content in an iframe
html_file = open('ok.html', 'r').read()





with open('spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)


def preprocess(text):

    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text) if word not in stop_words])
    return text





user_message = st.text_input("Entrez votre message:")

preprocessed_text = preprocess(user_message)  



prediction = model.predict([preprocessed_text])[0]
print(f"Before: {user_message}\n After: {preprocessed_text}")
print(prediction)


if st.button("IS THIS SPAM???"):
    if prediction == "spam":
        st.subheader("Votre message est classé comme spam.")
        st.image('spam.gif')
    else:
        st.subheader("Votre message n'est pas classé comme spam.")
        st.image("jam.gif")