import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎲 Simulação de Monte Carlo para Preços de Opções - Call Europeia")

# Parâmetros de entrada
S0 = st.number_input("Preço inicial da ação (S₀)", value=100.0, step=1.0, format="%.2f")
K = st.number_input("Preço de exercício da opção (K)", value=105.0, step=1.0, format="%.2f")
T = st.number_input("Tempo até o vencimento (anos)", value=1.0, step=0.1, format="%.2f")
r = st.number_input("Taxa livre de risco anual (%)", value=5.0, step=0.1, format="%.2f") / 100
sigma = st.number_input("Volatilidade anual (%)", value=20.0, step=0.1, format="%.2f") / 100
n_sim = st.number_input("Número de simulações", min_value=1000, max_value=100000, value=10000, step=1000)

# Simulação de Monte Carlo
np.random.seed(42)  # Para reproducibilidade

# Gera números aleatórios normais para simulação dos preços no vencimento
Z = np.random.standard_normal(n_sim)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# Calcula payoff da opção Call
payoff = np.maximum(ST - K, 0)

# Calcula preço presente da opção pela média descontada dos payoffs
option_price = np.exp(-r * T) * np.mean(payoff)

# Mostra resultado
st.write(f"### Preço estimado da opção Call: **R$ {option_price:.2f}**")

# Plot histograma dos preços no vencimento
fig, ax = plt.subplots()
ax.hist(ST, bins=50, alpha=0.7, color='skyblue')
ax.axvline(K, color='red', linestyle='--', label="Preço de Exercício (K)")
ax.set_xlabel("Preço da ação no vencimento (S_T)")
ax.set_ylabel("Frequência")
ax.set_title("Distribuição dos preços simulados da ação no vencimento")
ax.legend()

st.pyplot(fig)

# Explicação resumida
st.markdown("""
---
**Como funciona a simulação:**  
- O modelo assume que o preço da ação segue um movimento geométrico Browniano.  
- Simulamos vários possíveis preços no vencimento usando números aleatórios normais.  
- Calculamos o payoff da opção para cada simulação e descontamos para o valor presente.  
- A média desses payoffs descontados é o preço estimado da opção.  
""")
