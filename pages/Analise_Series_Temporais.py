import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Análise de Séries Temporais Financeiras")

# Geração de série temporal sintética
np.random.seed(42)
n_days = st.slider("Número de dias", 30, 365, 100)
dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days)
prices = 100 + np.cumsum(np.random.normal(0, 1, n_days))

df = pd.DataFrame({"Data": dates, "Preço": prices})

st.line_chart(df.set_index("Data")["Preço"])

# Média móvel
window = st.slider("Janela da média móvel (dias)", 1, 30, 5)
df['Média Móvel'] = df['Preço'].rolling(window=window).mean()

st.line_chart(df.set_index("Data")[['Preço', 'Média Móvel']])
