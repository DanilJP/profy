import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração de layout ideal para celular
st.set_page_config(page_title="Análise de Crédito", layout="centered")

st.title("🔎 Risco de Crédito")

# Criar dataset simples
def criar_dataset():
    return pd.DataFrame({
        "idade": [25, 45, 35, 50, 23, 40, 60, 37, 48, 33],
        "renda_mensal": [3000, 8000, 5000, 10000, 2500, 7000, 12000, 5200, 7800, 4800],
        "score_credito": [600, 720, 680, 730, 590, 710, 750, 690, 720, 670],
        "inadimplente": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    })

df = criar_dataset()

# Mostrar dados
st.subheader("📄 Dados Simulados")
st.dataframe(df, use_container_width=True)

# Gráfico de inadimplência
st.subheader("📊 Inadimplência")
with st.container():
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.countplot(x="inadimplente", data=df, ax=ax)
    ax.set_title("Distribuição de Inadimplência")
    st.pyplot(fig, use_container_width=True)

# Boxplot por idade
st.subheader("📦 Idade vs Inadimplência")
with st.container():
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.boxplot(x="inadimplente", y="idade", data=df, ax=ax)
    ax.set_title("Boxplot por Idade")
    st.pyplot(fig, use_container_width=True)

# Heatmap de correlação
st.subheader("🧮 Correlação")
with st.container():
    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlação das Variáveis")
    st.pyplot(fig, use_container_width=True)
