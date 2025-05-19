import streamlit as st
import numpy as np

st.title("📊 Modelagem de Risco de Crédito")

# Input: Probabilidade de inadimplência (PD)
pd = st.slider("Probabilidade de inadimplência (PD) [%]", 0.0, 100.0, 5.0) / 100
# Input: Exposição ao risco (EAD)
ead = st.number_input("Exposição ao risco (EAD) [R$]", min_value=0.0, value=100000.0, step=1000.0)
# Input: Perda dado inadimplência (LGD)
lgd = st.slider("Perda dado inadimplência (LGD) [%]", 0.0, 100.0, 45.0) / 100

# Cálculo do Valor em Risco esperado (Expected Loss)
expected_loss = pd * ead * lgd

st.write(f"### Expected Loss (Perda Esperada): R$ {expected_loss:,.2f}")

# Simulação simples do valor em risco para 1 ano com incerteza (exemplo)
simulations = 10000
random_pd = np.random.beta(2, 50, simulations)  # distribuição beta como exemplo
simulated_losses = random_pd * ead * lgd

st.write(f"Simulação - Média das perdas: R$ {np.mean(simulated_losses):,.2f}")
st.write(f"Simulação - Valor em risco (95% quantil): R$ {np.percentile(simulated_losses, 95):,.2f}")
