import streamlit as st
import numpy as np

st.title("Estratégias de Arbitragem Estatística")

st.markdown("Simulação simples de arbitragem entre dois ativos correlacionados.")

preco_ativo1 = st.number_input("Preço ativo 1", value=100.0)
preco_ativo2 = st.number_input("Preço ativo 2", value=100.0)
corr = st.slider("Correlação entre ativos", -1.0, 1.0, 0.8)

spread = preco_ativo1 - preco_ativo2
st.write(f"Spread atual: {spread:.2f}")

if abs(spread) > 5:
    st.success("Sinal de arbitragem! Considere comprar o ativo barato e vender o caro.")
else:
    st.info("Sem oportunidade clara de arbitragem no momento.")
