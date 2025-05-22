import streamlit as st

# Página principal otimizada para celular
st.set_page_config(page_title="Projetos Quant", layout="centered")

st.title("📊 Projetos Quant Interativos")
st.markdown("Explore projetos práticos em **Finanças Quantitativas**.")

# Agrupamento simples e direto, sem expanders
st.subheader("💳 Crédito")
st.page_link("pages/Modelagem_Risco_Credito.py", label="👉 Modelagem de Risco de Crédito")
st.page_link("pages/Analise_Risco_Credito.py", label="👉 Análise Exp. de Risco de Crédito")

st.subheader("💹 Derivativos")
st.page_link("pages/Precificacao_BlackScholes.py", label="👉 Precificação com Black-Scholes")
st.page_link("pages/Simulacao_MonteCarlo.py", label="👉 Simulação de Monte Carlo")
st.page_link("pages/Precificacao_Binomial.py", label="👉 Precificação Binomial de Opções")
st.page_link("pages/Greeks_Opcoes.py", label="👉 Cálculo dos Greeks")

st.subheader("📈 Gestão de Risco")
st.page_link("pages/Value_at_Risk.py", label="👉 Cálculo de VaR")
st.page_link("pages/Stress_Testing.py", label="👉 Stress Testing de Carteiras")
st.page_link("pages/PFE_Calculation.py", label="👉 Cálculo de PFE")

st.subheader("📊 Análise Quantitativa de Dados")
st.page_link("pages/Series_Temporais.py", label="👉 Séries Temporais")
st.page_link("pages/Backtesting_Modelos.py", label="👉 Backtesting de Modelos")
st.page_link("pages/Optimizacao_Portfolio.py", label="👉 Otimização de Portfólio")

st.markdown("---")
st.markdown("<center><small>Desenvolvido por Daniel Juliano | Versão Beta 🚧</small></center>", unsafe_allow_html=True)
