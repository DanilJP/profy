import streamlit as st

st.set_page_config(page_title="Analisador de GitHub", layout="centered")
st.title("🔍 Analisador de Portfólio no GitHub")

usuario = st.text_input("Digite seu nome de usuário do GitHub")

if usuario:
    st.markdown(f"📂 Avaliando perfil: `{usuario}`")
    
    # Simulação de análise
    st.markdown("🔎 **Checklist de Portfólio:**")
    st.checkbox("Repositórios com README bem descrito")
    st.checkbox("Projetos com Jupyter/Streamlit")
    st.checkbox("Commits recentes (últimos 30 dias)")
    st.checkbox("Organização por temas")
    st.checkbox("Utilização de GitHub Pages ou Actions")

    st.info("Dica: mantenha pelo menos 3 projetos públicos que representem seu foco profissional.")
