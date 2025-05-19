import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Backtest de Estratégias de ETF")

st.markdown("""
Simule uma estratégia de investimento simples com ETFs utilizando médias móveis.
""")

# Simulando dados
np.random.seed(42)
dates = pd.date_range("2020-01-01", periods=500)
prices = pd.Series(np.random.normal(0.001, 0.02, size=500)).cumsum() + 100
data = pd.DataFrame({"Date": dates, "Price": prices})
data.set_index("Date", inplace=True)

# Inputs do usuário
fast = st.slider("Média móvel curta", 5, 30, 10)
slow = st.slider("Média móvel longa", 20, 100, 50)

# Estratégia
if fast < slow:
    data["SMA_fast"] = data["Price"].rolling(window=fast).mean()
    data["SMA_slow"] = data["Price"].rolling(window=slow).mean()
    data["Signal"] = 0
    data.loc[data["SMA_fast"] > data["SMA_slow"], "Signal"] = 1
    data.loc[data["SMA_fast"] < data["SMA_slow"], "Signal"] = -1
    data["Returns"] = data["Price"].pct_change()
    data["Strategy"] = data["Returns"] * data["Signal"].shift(1)

    st.line_chart(data[["Price", "SMA_fast", "SMA_slow"]])
    st.line_chart(data[["Strategy"]].cumsum())
    
    st.metric("Retorno acumulado da estratégia", f"{100*data['Strategy'].cumsum()[-1]:.2f}%")
else:
    st.warning("A média móvel curta deve ser menor que a longa.")