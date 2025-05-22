import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🔎 Análise Exploratória de Risco de Crédito")

# Dataset fictício
def criar_dataset():
    data = {
        "idade": [25, 45, 35, 50, 23, 40, 60, 37, 48, 33],
        "renda_mensal": [3000, 8000, 5000, 10000, 2500, 7000, 12000, 5200, 7800, 4800],
        "score_credito": [600, 720, 680, 730, 590, 710, 750, 690, 720, 670],
        "inadimplente": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    }
    return pd.DataFrame(data)

df = criar_dataset()
st.write(df)

st.write("Distribuição de inadimplência")
fig, ax = plt.subplots()
sns.countplot(x="inadimplente", data=df, ax=ax)
st.pyplot(fig)

st.write("Boxplot da idade por inadimplência")
fig, ax = plt.subplots()
sns.boxplot(x="inadimplente", y="idade", data=df, ax=ax)
st.pyplot(fig)

st.write("Correlação entre variáveis")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
