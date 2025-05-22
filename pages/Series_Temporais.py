import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📈 Análise de Séries Temporais Financeiras")

# Gerar série de preços simulados
np.random.seed(42)
dias = pd.date_range(start='2023-01-01', periods=250)
retornos = np.random.normal(0, 0.01, 250)
precos = 100 * (1 + pd.Series(retornos)).cumprod()

df = pd.DataFrame({"Data": dias, "Preço": precos})
fig = px.line(df, x="Data", y="Preço", title="Preço Simulado")

st.plotly_chart(fig)

st.write("Estatísticas básicas:")
st.write(df.describe())
