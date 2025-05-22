import streamlit as st

# Página principal
st.set_page_config(page_title="Catálogo de Projetos Quant", layout="wide")

st.title("📊 Catálogo de Projetos Interativos")
st.markdown("Explore projetos práticos nas áreas de **Quant** e **Ciência de Dados**.")

st.header("📈 Temas e Projetos Quant")

with st.expander("💳 Crédito"):
    st.page_link("pages/Modelagem_Risco_Credito.py", label="👉 Modelagem de Risco de Crédito")
    st.page_link("pages/Analise_Risco_Credito.py", label="👉 Análise Exploratória de Risco de Crédito")

with st.expander("💹 Derivativos"):
    st.page_link("pages/Precificacao_BlackScholes.py", label="👉 Precificação de Opções com Black-Scholes")
    st.page_link("pages/Simulacao_MonteCarlo.py", label="👉 Simulação de Monte Carlo")
    st.page_link("pages/Precificacao_Binomial.py", label="👉 Precificação Binomial de Opções")
    st.page_link("pages/Greeks_Opcoes.py", label="👉 Cálculo dos Greeks")

with st.expander("📈 Gestão de Risco"):
    st.page_link("pages/Value_at_Risk.py", label="👉 Cálculo de VaR (Value at Risk)")
    st.page_link("pages/Stress_Testing.py", label="👉 Stress Testing para Carteiras")
    st.page_link("pages/PFE_Calculation.py", label="👉 Cálculo de PFE (Potential Future Exposure)")

with st.expander("📊 Análise Quantitativa de Dados"):
    st.page_link("pages/Series_Temporais.py", label="👉 Análise de Séries Temporais Financeiras")
    st.page_link("pages/Backtesting_Modelos.py", label="👉 Backtesting de Modelos Quantitativos")
    st.page_link("pages/Optimizacao_Portfolio.py", label="👉 Otimização de Portfólio")

st.markdown("---")
st.markdown("Desenvolvido por Daniel Juliano | Versão Beta 🚧")
