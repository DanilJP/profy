import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Dashboard Interativo de KPIs")

# Dados sintéticos
np.random.seed(42)
meses = pd.date_range("2023-01-01", periods=12, freq='M')
vendas = np.random.randint(1000, 5000, size=12)
clientes = np.random.randint(50, 300, size=12)
tickets = vendas / clientes

df = pd.DataFrame({"Mês": meses.strftime("%b/%Y"), "Vendas": vendas, "Clientes": clientes, "Ticket Médio": tickets})

kpi = st.selectbox("Selecione o KPI para visualizar:", df.columns[1:])

st.line_chart(df.set_index("Mês")[kpi])
