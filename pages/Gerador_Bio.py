import streamlit as st

st.title("💼 Gerador de Bio para LinkedIn e Instagram")
st.markdown("Crie uma bio profissional personalizada com base em suas preferências e área de atuação.")

nome = st.text_input("Seu nome")
area = st.selectbox("Área de atuação", ["Dados", "Finanças", "Tecnologia", "Marketing"])
personalidade = st.selectbox("Estilo da bio", ["Profissional", "Criativa", "Inspiradora"])

if nome:
    st.subheader("🧾 Sua Bio Gerada")
    if personalidade == "Profissional":
        st.write(f"{nome} | Especialista em {area}, apaixonado por resultados e inovação.")
    elif personalidade == "Criativa":
        st.write(f"{nome} | Transformando {area.lower()} em arte com dados e ideias.")
    elif personalidade == "Inspiradora":
        st.write(f"{nome} | Em busca de impactar o mundo através de {area.lower()}.")

