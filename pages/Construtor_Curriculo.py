import streamlit as st

st.title("📝 Construtor de Currículo")

st.header("Informações Pessoais")
nome = st.text_input("Nome completo")
email = st.text_input("Email")
telefone = st.text_input("Telefone")

st.header("Objetivo Profissional")
objetivo = st.text_area("Digite seu objetivo profissional")

st.header("Experiência Profissional")
experiencia = st.text_area("Liste suas experiências profissionais")

st.header("Formação Acadêmica")
formacao = st.text_area("Liste sua formação acadêmica")

if st.button("Gerar Currículo"):
    st.subheader("📄 Currículo Gerado")
    st.markdown(f"**Nome:** {nome}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Telefone:** {telefone}")
    st.markdown("---")
    st.markdown(f"### 🎯 Objetivo\n{objetivo}")
    st.markdown(f"### 💼 Experiência\n{experiencia}")
    st.markdown(f"### 🎓 Formação\n{formacao}")
