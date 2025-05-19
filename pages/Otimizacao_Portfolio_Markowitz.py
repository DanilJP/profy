import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Construção e Otimização de Portfólio com Markowitz")

num_ativos = st.number_input("Número de ativos", min_value=2, max_value=10, value=4)

if st.button("Otimizar portfólio"):
    np.random.seed(42)
    retornos = np.random.normal(0.001, 0.02, (252, num_ativos))
    cov_matrix = np.cov(retornos, rowvar=False)
    pesos = np.random.dirichlet(np.ones(num_ativos), size=10000)
    retornos_esperados = pesos @ retornos.mean(axis=0)
    riscos = np.sqrt(np.einsum('ij,jk,ik->i', pesos, cov_matrix, pesos))
    sharpe = retornos_esperados / riscos
    melhor = np.argmax(sharpe)
    st.write("Melhor combinação de pesos:")
    for i, p in enumerate(pesos[melhor]):
        st.write(f"Ativo {i+1}: {p:.2%}")
    st.write(f"Retorno esperado: {retornos_esperados[melhor]:.2%}")
    st.write(f"Risco (desvio padrão): {riscos[melhor]:.2%}")
