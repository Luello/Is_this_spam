import streamlit as st
import pickle 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


st.title("MODULE DE DETECTION DES SPAM")

search_done = st.session_state.get('search_done', False)





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





import base64




def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls="hidden"  autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )








if st.button("IS THIS SPAM???"):
    st.session_state['search_done'] = True
    if prediction == "spam":
        st.subheader("Votre message est classé comme spam.")
        autoplay_audio("dehors.mp3")
        st.image('spam.gif')
        
     
    else:
        st.subheader("Votre message n'est pas classé comme spam.")
        st.image("jam.gif")