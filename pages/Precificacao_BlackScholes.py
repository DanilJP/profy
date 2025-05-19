import streamlit as st
from scipy.stats import norm
import numpy as np

st.title("Precificação de Opções com Black-Scholes")

S = st.number_input("Preço do ativo (S)", value=100.0)
K = st.number_input("Preço de exercício (K)", value=100.0)
T = st.number_input("Tempo até vencimento (anos)", value=1.0)
r = st.number_input("Taxa livre de risco (%)", value=5.0) / 100
sigma = st.number_input("Volatilidade (%)", value=20.0) / 100
option_type = st.selectbox("Tipo de opção", ["Call", "Put"])

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "Call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price

if st.button("Calcular preço da opção"):
    price = black_scholes(S, K, T, r, sigma, option_type)
    st.success(f"Preço da opção {option_type}: R$ {price:.2f}")
