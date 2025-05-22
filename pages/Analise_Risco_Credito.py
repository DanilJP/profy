import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Layout otimizado para celular
st.set_page_config(page_title="Análise de Crédito", layout="centered")

st.title("🔍 Análise de Risco de Crédito")

# Dados fictícios
def criar_dataset():
    return pd.DataFrame({
        "idade": [25, 45, 35, 50, 23, 40, 60, 37, 48, 33],
        "renda_mensal": [3000, 8000, 5000, 10000, 2500, 7000, 12000, 5200, 7800, 4800],
        "score_credito": [600, 720, 680, 730, 590, 710, 750, 690, 720, 670],
        "inadimplente": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    })

df = criar_dataset()

# Mostrar dados
with st.expander("📄 Ver dados simulados"):
    st.dataframe(df, use_container_width=True)

# Filtro por inadimplência
filtro = st.radio("Filtrar por:", ["Todos", "Inadimplentes", "Adimplentes"], horizontal=True)
if filtro == "Inadimplentes":
    df = df[df["inadimplente"] == 1]
elif filtro == "Adimplentes":
    df = df[df["inadimplente"] == 0]

# Análises interativas
st.subheader("📊 Análises Visuais")

if st.checkbox("🔢 Distribuição de Inadimplência"):
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.countplot(x="inadimplente", data=df, ax=ax)
    ax.set_title("Distribuição de Inadimplência")
    st.pyplot(fig, use_container_width=True)

if st.checkbox("📦 Boxplot por variável"):
    coluna = st.selectbox("Escolha a variável:", ["idade", "renda_mensal", "score_credito"])
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.boxplot(x="inadimplente", y=coluna, data=df, ax=ax)
    ax.set_title(f"Boxplot de {coluna.title()}")
    st.pyplot(fig, use_container_width=True)

if st.checkbox("📌 Mapa de Correlação"):
    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlação das Variáveis")
    st.pyplot(fig, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("<center><small>Feito por Daniel Juliano</small></center>", unsafe_allow_html=True)
