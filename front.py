import streamlit as st
import pickle 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import base64




st.title("MODULE DE DETECTION DES SPAMS")

search_done = st.session_state.get('search_done', False)





with open('spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)
    
# with open('results_df.pkl', 'rb') as f:
#     results_df = pickle.load(f)


def preprocess(text):

    #lemmatizer = WordNetLemmatizer()
    #stop_words = set(stopwords.words('english'))
    #text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text) if word not in stop_words])
    return text





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






tab1, tab2 = st.tabs(["Module de Détection", "Resultat des tests"])

with tab1:
    user_message = st.text_input("Entrez votre message:")

    preprocessed_text = preprocess(user_message) 
    if st.button("IS THIS SPAM???"):
     
        prediction_proba = model.predict_proba([preprocessed_text])[0]
        prediction = model.predict([preprocessed_text])[0]
        print(f"Before: {user_message}\n After: {preprocessed_text}")
        print(prediction)

        st.session_state['search_done'] = True
        if prediction == "spam":
            st.subheader("Votre message est classé comme spam.")
            st.write(f"Probabilité de spam : {round(prediction_proba[1],2)}")  # Afficher la probabilité de la classe "spam"
            st.image('spam.gif')
            
        
        else:
            st.subheader("Votre message n'est pas classé comme spam.")
            st.write(f"Probabilité de spam : {round(prediction_proba[1],2)}")  # Afficher la probabilité de la classe "spam"
            st.image("jam.gif")





        
        
with tab2:
    col1, col2= st.columns(2)
    
    with col1:
        st. title("Test des modalités de prétraitement sans ajout de features")
        with open('results_df.pkl', 'rb') as df:
            model = pickle.load(df)
            st.dataframe(model)   
    with col2:
        st. title("Test avec ajout des features: Nb de caractères, % de Maj, % de chiffres")
        with open('results_df_add_features.pkl', 'rb') as df2:
            model2 = pickle.load(df2)
            st.dataframe(model2)   

