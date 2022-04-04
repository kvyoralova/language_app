import streamlit as st
from googletrans import Translator

st.title("My translator")
translator = Translator()

word = st.text_input("gimme a word to translate, or write 'nothing' to stop me: ")
destlang = st.selectbox('Which language do you choose?',
('it', 'en', 'de', 'cs', 'ru', 'fr', 'es', 'zu', 'hu', 'uk', 'sk'))
abc = translator.translate(text=word, dest=destlang) 
st.balloons()
st.write("You chose a word in", abc.src, "and the", destlang, "translation is", abc.text)
