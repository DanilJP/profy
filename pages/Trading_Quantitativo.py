import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("🤖 Estratégias de Trading Quantitativo")

# Gerar dados sintéticos de preços
np.random.seed(42)
n_days = 200
prices = 100 + np.cumsum(np.random.normal(0, 1, n_days))
dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days)
df = pd.DataFrame({"Data": dates, "Preço": prices})

# Parâmetros da estratégia
short_window = st.slider("Janela Curta (dias)", 1, 50, 20)
long_window = st.slider("Janela Longa (dias)", 10, 100, 50)

# Cálculo das médias móveis
df['SMA Curta'] = df['Preço'].rolling(window=short_window).mean()
df['SMA Longa'] = df['Preço'].rolling(window=long_window).mean()

# Sinal de compra e venda
df['Sinal'] = 0
df.loc[df['SMA Curta'] > df['SMA Longa'], 'Sinal'] = 1
df.loc[df['SMA Curta'] < df['SMA Longa'], 'Sinal'] = -1

# Visualização
fig, ax = plt.subplots()
ax.plot(df['Data'], df['Preço'], label='Preço')
ax.plot(df['Data'], df['SMA Curta'], label='SMA Curta')
ax.plot(df['Data'], df['SMA Longa'], label='SMA Longa')
ax.legend()
st.pyplot(fig)

st.write("Sinal (1 = compra, -1 = venda):")
st.write(df[['Data', 'Sinal']].tail(10))
