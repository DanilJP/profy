import streamlit as st

st.set_page_config(page_title="Catálogo de Projetos", layout="wide")

st.title("📊 Catálogo de Projetos Interativos")
st.markdown("Explore projetos práticos nas áreas de **Quant**, **Ciência de Dados**, **Marca Pessoal** e **Psicologia**. Clique em um tema para ver os projetos disponíveis.")

# Colunas dos macro temas
macro_temas = st.columns(3)
macro_temas_2 = st.columns(3)

# Quant
with macro_temas[0]:
    st.header('📈 Quant')
    with st.expander("> Projetos"):
        st.markdown("Projetos voltados à área financeira, com foco em modelagens, precificação e análise quantitativa.")
        st.page_link("pages/Analise_Carteiras_KPI.py", label="👉 Análise de Carteiras com KPIs de Risco")
        st.page_link("pages/Estrategias_Arbitragem.py", label="👉 Estratégias de Arbitragem Estatística")
        st.page_link("pages/Backtest_Momentum.py", label="👉 Backtesting de Estratégias Momentum")
        st.page_link("pages/Backtest_ETF.py", label="👉 Backtest de Estratégias de ETF")
        st.page_link("pages/Modelagem_GARCH.py", label="👉 Modelagem de Volatilidade Estocástica (GARCH)")
        st.page_link("pages/Modelagem_Risco_Credito.py", label="👉 Modelagem de Risco de Crédito")
        st.page_link("pages/MonteCarlo_VaR.py", label="👉 Simulação de Monte Carlo para VaR")
        st.page_link("pages/Otimizacao_Portfolio_Markowitz.py", label="👉 Construção e Otimização de Portfólio com Markowitz")
        st.page_link("pages/Precificacao_BlackScholes.py", label="👉 Precificação de Opções com Black-Scholes")
        st.page_link("pages/Scorecard_Risco_Credito.py", label="👉 Análise de Risco de Crédito com Scorecard")
        st.page_link("pages/Simulacao_MonteCarlo_Opcoes.py", label="👉 Simulação de Monte Carlo para Preços de Opções")
        st.page_link("pages/Trading_Quantitativo.py", label="👉 Estratégias de Trading Quantitativo")
        st.page_link("pages/Analise_Series_Temporais.py", label="👉 Análise de Séries Temporais Financeiras")
        st.page_link("pages/Calculadora_NDF.py", label="👉 Calculadora de NDF")

# Ciência de Dados
with macro_temas[1]:
    st.header('🧠 Ciência de Dados')
    with st.expander("> Projetos"):
        st.markdown("Projetos focados em dados, estatística, machine learning e visualizações.")
        st.page_link("pages/Analise_Sentimentos.py", label="👉 Análise de Sentimentos em Redes Sociais")
        st.page_link("pages/Classificacao_Clientes.py", label="👉 Classificação de Clientes para Marketing")
        st.page_link("pages/Clustering_Clientes.py", label="👉 Clustering de Segmentos de Clientes")
        st.page_link("pages/Deteccao_Fraudes.py", label="👉 Detecção de Fraudes com Machine Learning")
        st.page_link("pages/Dashboard_KPIs.py", label="👉 Dashboard Interativo de KPIs")
        st.page_link("pages/Previsao_Vendas.py", label="👉 Previsão de Vendas com Regressão")

# Marca Pessoal
with macro_temas[2]:
    st.header("💼 Marca Pessoal")
    with st.expander("> Projetos"):
        st.markdown("Ferramentas para destacar sua trajetória profissional e criar presença digital.")
        st.page_link("pages/Analise_Portfolio_Github.py", label="👉 Análise de Portfólio Profissional")
        st.page_link("pages/Construtor_Curriculo.py", label="👉 Construtor de Currículo Profissional")
        st.page_link("pages/Gerador_Bio.py", label="👉 Gerador de Bio para LinkedIn e Instagram")
        st.page_link("pages/Otimizador_Linkedin.py", label="👉 Analisador de Perfil LinkedIn")
        st.page_link("pages/Simulador_Entrevista.py", label="👉 Simulador de Entrevistas")

# Psicologia
with macro_temas_2[0]:
    st.header("🧩 Psicologia")
    with st.expander("> Projetos"):
        st.markdown("Projetos para análise, autoconhecimento e suporte psicológico.")
        st.page_link("pages/Teste_Perfil_Comportamental.py", label="👉 Teste de Perfil Comportamental")
        # Adicione os links abaixo quando tiver os arquivos:
        # st.page_link("pages/Analise_Estresse.py", label="👉 Análise de Estresse e Coping")
        # st.page_link("pages/Autoavaliacao_Ansiedade.py", label="👉 Autoavaliação de Ansiedade")
        # st.page_link("pages/Diario_Humor.py", label="👉 Diário de Humor e Emoções")
        # st.page_link("pages/Mindfulness_Meditacao.py", label="👉 Mindfulness e Meditação Guiada")
        # st.page_link("pages/Planejamento_Desenvolvimento.py", label="👉 Planejamento de Desenvolvimento Pessoal")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Daniel Juliano | Versão Beta 🚧")
