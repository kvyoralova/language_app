import streamlit as st
from googletrans import Translator

st.title("My translator")
translator = Translator()

word = st.text_input("Write a word to translate:", "insert yourr word here")
destlang = st.selectbox('Which language do you choose?',
('af', 'sq', 'ar', 'ca', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'el', 'ht', 'haw', 'he', 'hi', 'is', 'ga', 'it', 'ko', 'no', 'pl', 'sk', 'sv', 'uz', 'vi', 'yi'))
abc = translator.translate(text=word, dest=destlang) 
#st.balloons()
st.write("You chose a word in", abc.src, "and the", destlang, "translation is:")
st.info(abc.text)
