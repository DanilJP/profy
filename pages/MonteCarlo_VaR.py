import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎲 Simulação de Monte Carlo para Preços de Opções - Call Europeia (Trajetórias Temporais)")

# Parâmetros de entrada
S0 = st.number_input("Preço inicial da ação (S₀)", value=100.0, step=1.0, format="%.2f")
K = st.number_input("Preço de exercício da opção (K)", value=105.0, step=1.0, format="%.2f")
T = st.number_input("Tempo até o vencimento (anos)", value=1.0, step=0.1, format="%.2f")
r = st.number_input("Taxa livre de risco anual (%)", value=5.0, step=0.1, format="%.2f") / 100
sigma = st.number_input("Volatilidade anual (%)", value=20.0, step=0.1, format="%.2f") / 100
n_sim = st.number_input("Número de simulações", min_value=1000, max_value=100000, value=10000, step=1000)
n_steps = st.number_input("Número de passos na simulação", min_value=10, max_value=500, value=100, step=10)

# Definindo passos de tempo
dt = T / n_steps

np.random.seed(42)  # Reprodutibilidade

# Simulação dos preços ao longo do tempo (caminhos)
# Geramos uma matriz de incrementos normais: shape (n_sim, n_steps)
Z = np.random.standard_normal((n_sim, n_steps))

# Inicializa a matriz de preços: (n_sim, n_steps+1)
S = np.zeros((n_sim, n_steps + 1))
S[:, 0] = S0

# Calcula os preços ao longo do tempo para cada simulação
for t in range(1, n_steps + 1):
    S[:, t] = S[:, t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, t-1])

# Preço da ação no vencimento para cada simulação (última coluna)
ST = S[:, -1]

# Payoff da opção
payoff = np.maximum(ST - K, 0)

# Preço presente estimado da opção
option_price = np.exp(-r * T) * np.mean(payoff)

st.write(f"### Preço estimado da opção Call: **R$ {option_price:.2f}**")

# Plot algumas trajetórias
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(min(20, n_sim)):  # Mostra até 20 trajetórias
    ax.plot(np.linspace(0, T, n_steps + 1), S[i, :], lw=1, alpha=0.7)

ax.axhline(K, color='red', linestyle='--', label="Preço de Exercício (K)")
ax.set_xlabel("Tempo (anos)")
ax.set_ylabel("Preço da ação")
ax.set_title("Trajetórias simuladas dos preços da ação")
ax.legend()

st.pyplot(fig)

# Explicação resumida
st.markdown("""
---
**Como funciona a simulação com trajetórias temporais:**  
- O preço da ação é modelado como um movimento geométrico Browniano ao longo do tempo.  
- Simulamos vários caminhos do preço da ação, passo a passo, até o vencimento.  
- Calculamos o payoff da opção com base no preço final de cada trajetória e descontamos para valor presente.  
- A média desses payoffs descontados é o preço estimado da opção.  
""")
