import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="📊 Análise de Carteiras com KPIs de Risco", layout="wide")

if st.session_state.logged_in == True:

    st.markdown("""
    Insira os retornos de ativos e pesos da carteira para visualizar indicadores como volatilidade, Sharpe e retorno esperado.
    """)

    # Simula retornos aleatórios
    n_assets = st.slider("Quantidade de ativos", 2, 10, 4)
    n_periods = 252
    returns = np.random.normal(0.0005, 0.01, size=(n_periods, n_assets))
    ret_df = pd.DataFrame(returns, columns=[f"Ativo {i+1}" for i in range(n_assets)])

    # Pesos
    weights = st.slider("Peso dos ativos (soma = 100%)", 0, 100, [25]*n_assets)
    weights = np.array(weights) / 100
    if np.sum(weights) != 1:
        st.warning("A soma dos pesos deve ser 100%.")

    # KPIs
    portfolio_returns = np.dot(ret_df.mean(), weights)
    portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(ret_df.cov(), weights)))
    sharpe_ratio = portfolio_returns / portfolio_vol * np.sqrt(252)

    st.write(f"**Retorno esperado anualizado:** {portfolio_returns*252:.2%}")
    st.write(f"**Volatilidade anualizada:** {portfolio_vol*np.sqrt(252):.2%}")
    st.write(f"**Sharpe Ratio:** {sharpe_ratio:.2f}")

else:
    st.header('Realize seu login para ter acesso')
