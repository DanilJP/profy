import streamlit as st
from textblob import TextBlob

st.title("💬 Análise de Sentimentos em Redes Sociais")

text = st.text_area("Cole aqui o texto de uma rede social para analisar:")

if text:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    st.write(f"Polaridade: {polarity:.2f} (de -1 negativo a +1 positivo)")
    st.write(f"Subjetividade: {subjectivity:.2f} (de 0 objetivo a 1 subjetivo)")
else:
    st.write("Digite ou cole um texto para analisar.")
