import streamlit as st
import random

st.set_page_config(page_title="Simulador de Entrevista", layout="centered")
st.title("🎤 Simulador de Entrevista Técnica e Comportamental")

perguntas_tecnicas = [
    "Explique o conceito de overfitting em machine learning.",
    "Como funciona o cálculo de valor presente líquido (VPL)?",
    "Qual a diferença entre correlação e causalidade?",
    "Como você escolheria o número de clusters no K-Means?"
]

perguntas_comportamentais = [
    "Fale sobre um desafio que você superou no trabalho.",
    "Como você lida com feedbacks negativos?",
    "Descreva um projeto que você liderou.",
    "Como você organiza suas prioridades?"
]

if st.button("🎲 Nova Pergunta Técnica"):
    st.markdown(f"**Pergunta Técnica:** {random.choice(perguntas_tecnicas)}")

if st.button("🎲 Nova Pergunta Comportamental"):
    st.markdown(f"**Pergunta Comportamental:** {random.choice(perguntas_comportamentais)}")
