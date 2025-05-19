import streamlit as st
import numpy as np
import pandas as pd

st.title("Backtesting de Estratégias Momentum")

periodo = st.number_input("Período da estratégia (dias)", value=20)
dias = st.number_input("Total de dias para simulação", value=252)

if st.button("Rodar backtest"):
    np.random.seed(42)
    preços = pd.Series(100 + np.cumsum(np.random.normal(0, 1, dias)))
    momentum = preços.diff(periodo)
    sinais = momentum.apply(lambda x: 1 if x > 0 else -1)
    retornos = preços.pct_change().shift(-1)
    estrategia_retorno = (sinais * retornos).dropna()
    st.write(f"Retorno total estratégia: {estrategia_retorno.sum():.2%}")
    st.line_chart(estrategia_retorno.cumsum())
