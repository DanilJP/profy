# ndf_calculator.py

import streamlit as st
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# ======================
# Funções auxiliares
# ======================

brazil_holidays = [
    "2025-01-01", "2025-03-03", "2025-03-04", "2025-04-18", "2025-04-21",
    "2025-05-01", "2025-06-19", "2025-09-07", "2025-10-12", "2025-11-02",
    "2025-11-15", "2025-12-25", "2026-01-01", "2026-02-16", "2026-02-17",
    "2026-04-03", "2026-04-21", "2026-05-01", "2026-06-04", "2026-09-07",
    "2026-10-12", "2026-11-02", "2026-11-15", "2026-12-25"
]

def business_days_diff(start_date, end_date):
    start_str = np.datetime64(start_date)
    end_str = np.datetime64(end_date)
    return np.busday_count(start_str, end_str, holidays=brazil_holidays)

def diferenca_dias(data1: str, data2: str, formato: str = "%Y-%m-%d") -> int:
    d1 = datetime.strptime(data1, formato)
    d2 = datetime.strptime(data2, formato)
    return abs((d2 - d1).days)

# ======================
# Interface Streamlit
# ======================

st.title("Calculadora de NDF (Non-Deliverable Forward)")

with st.sidebar:
    st.header("Parâmetros do Contrato")

    notional = st.number_input("Notional (USD)", value=1_000_000)
    pre = st.number_input("Taxa de juros pré (BRL)", value=0.15, step=0.01)
    cupom = st.number_input("Cupom cambial (USD)", value=0.05, step=0.01)
    spot = st.number_input("Spot atual (BRL/USD)", value=5.75)
    data_ref = st.date_input("Data de referência", value=datetime(2025, 2, 19))
    vencimento = st.date_input("Vencimento", value=datetime(2026, 2, 19))

# ======================
# Cálculo do FWD
# ======================

ndu = business_days_diff(str(data_ref), str(vencimento))
ndc = diferenca_dias(str(data_ref), str(vencimento))

fwd = spot * ((1 + pre) ** (ndu / 252)) / (1 + cupom * ndc / 360)
fwd = fwd * 0.98  # Haircut

st.markdown(f"**Dias úteis (ndu)**: {ndu}")
st.markdown(f"**Dias corridos (ndc)**: {ndc}")
st.markdown(f"**Forward calculado (fwd)**: `{fwd:.4f}`")

# ======================
# Cálculo dos Payoffs
# ======================

spots_vencimento = list(range(1, 10))
valores_recebidos = [notional * (s - 5) for s in spots_vencimento]
valores_recebidos_ndf = [notional * (fwd - s) for s in spots_vencimento]
payouts = list(np.array(valores_recebidos) + np.array(valores_recebidos_ndf))

# ======================
# Gráfico
# ======================

fig, ax = plt.subplots()
ax.plot(spots_vencimento, valores_recebidos, marker='o', label='Fluxo 1')
ax.plot(spots_vencimento, valores_recebidos_ndf, marker='x', label='NDF')
ax.plot(spots_vencimento, payouts, marker='s', label='Payout total')

ax.set_title("Spot x Valor Ajustado")
ax.set_xlabel("Spot no vencimento")
ax.set_ylabel("Valor em BRL")
ax.legend()
st.pyplot(fig)

# ======================
# Exibir tabelas numéricas
# ======================

st.subheader("Tabela de Resultados")
st.write("### Spots vs Resultados")
st.dataframe({
    "Spot Vencimento": spots_vencimento,
    "Fluxo 1 (USD convertido)": valores_recebidos,
    "NDF (ajuste BRL)": valores_recebidos_ndf,
    "Payout Total": payouts
})
