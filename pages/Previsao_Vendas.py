import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("🧠 Previsão de Vendas com Regressão Linear")

st.markdown("Simule a previsão de vendas com base em dias promocionais e sazonalidade.")

# Dados sintéticos
np.random.seed(0)
X = np.linspace(1, 100, 100).reshape(-1, 1)
y = 100 + 0.8 * X.flatten() + 10 * np.sin(X.flatten() / 5) + np.random.normal(0, 5, size=100)

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

fig, ax = plt.subplots()
ax.plot(X, y, label="Vendas reais")
ax.plot(X, y_pred, label="Previsão", linestyle='--')
ax.set_title("Previsão de Vendas")
ax.legend()

st.pyplot(fig)

