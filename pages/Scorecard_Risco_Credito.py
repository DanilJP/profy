import streamlit as st

st.title("Análise de Risco de Crédito com Scorecard")

st.markdown("Simulação simples de score para avaliação de risco.")

idade = st.slider("Idade", 18, 75, 30)
renda = st.number_input("Renda mensal (R$)", value=3000)
emprestimos_abertos = st.number_input("Número de empréstimos ativos", value=1)
inadimplente = st.selectbox("Já teve inadimplência?", ["Não", "Sim"])

score = 100
score += (idade - 18) * 0.5
score += renda / 100
score -= emprestimos_abertos * 10
score -= 30 if inadimplente == "Sim" else 0

if st.button("Calcular score"):
    st.write(f"Score de crédito estimado: {score:.1f}")
    if score > 120:
        st.success("Risco baixo")
    elif score > 80:
        st.warning("Risco médio")
    else:
        st.error("Risco alto")
