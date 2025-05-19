import streamlit as st
import pandas as pd

st.title("💼 Análise de Portfólio Profissional")

st.markdown("Cole seu portfólio ou currículo para uma análise automática dos pontos fortes e sugestões de melhoria.")

texto = st.text_area("Cole aqui seu texto/currículo")

if texto:
    st.subheader("🔍 Análise Preliminar")
    st.write("**Forças Detectadas:**")
    if "dados" in texto.lower():
        st.write("✅ Experiência com dados")
    if "python" in texto.lower():
        st.write("✅ Domínio de Python")
    if "liderança" in texto.lower():
        st.write("✅ Perfil de liderança")

    st.write("**Sugestões:**")
    if "resultados" not in texto.lower():
        st.write("🔧 Incluir resultados mensuráveis alcançados")
    if "projetos" not in texto.lower():
        st.write("🔧 Citar projetos realizados (acadêmicos ou profissionais)")
