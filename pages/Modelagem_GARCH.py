import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model

st.title("Modelagem de Volatilidade Estocástica (GARCH)")

st.markdown("Simulação de modelo GARCH(1,1) para retornos financeiros.")

np.random.seed(42)
n = st.number_input("Número de pontos na simulação", value=1000)

if st.button("Gerar simulação GARCH"):
    am = arch_model(None, vol='Garch', p=1, q=1)
    sim_data = am.simulate([0.1, 0.15, 0.8, 0.1], n)
    fig, ax = plt.subplots()
    ax.plot(sim_data['data'])
    ax.set_title("Simulação de Retornos GARCH(1,1)")
    st.pyplot(fig)
