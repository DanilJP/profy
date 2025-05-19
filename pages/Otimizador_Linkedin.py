import streamlit as st

st.set_page_config(page_title="Otimizador de LinkedIn", layout="centered")
st.title("💼 Otimizador de Perfil no LinkedIn")

st.markdown("Verifique os itens abaixo para melhorar seu perfil:")

itens = [
    "Foto de perfil profissional",
    "Título claro e objetivo",
    "Resumo com palavras-chave da sua área",
    "Experiências bem descritas com resultados",
    "Seção de projetos com links",
    "Educação e certificações atualizadas",
    "Personalização da URL do perfil",
    "Postagens regulares ou artigos publicados",
]

for item in itens:
    st.checkbox(item)

st.success("Revise seus itens acima para melhorar sua presença profissional!")
