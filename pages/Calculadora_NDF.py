import streamlit as st
import datetime
st.set_page_config(page_title="Calculadora NDF", layout="wide")

st.title("💱 Calculadora NDF - Non-Deliverable Forward")

st.write("""
Esta calculadora ajuda a estimar o resultado financeiro de uma operação de NDF, 
comparando a taxa contratada com a taxa de liquidação.
""")

st.header("📋 Parâmetros do Contrato")

col1, col2 = st.columns(2)

with col1:
    notional = st.number_input("Valor Notional (USD)", min_value=0.0, step=1000.0, format="%.2f")
    taxa_contratada = st.number_input("Taxa Contratada (ex: 5.20)", min_value=0.0, format="%.4f")
with col2:
    taxa_liquidacao = st.number_input("Taxa de Liquidação (ex: 5.30)", min_value=0.0, format="%.4f")
    data_liquidacao = st.date_input("Data de Liquidação", value=datetime.date.today())

if st.button("📊 Calcular Resultado"):
    if notional > 0 and taxa_contratada > 0 and taxa_liquidacao > 0:
        resultado = notional * (taxa_liquidacao - taxa_contratada)
        
        st.subheader("💰 Resultado da Operação")
        if resultado > 0:
            st.success(f"Lucro de R$ {resultado:,.2f}")
        elif resultado < 0:
            st.error(f"Prejuízo de R$ {abs(resultado):,.2f}")
        else:
            st.info("Sem lucro ou prejuízo. A taxa de liquidação foi igual à contratada.")
    else:
        st.warning("Preencha todos os campos corretamente.")

st.markdown("---")
st.caption("Essa é uma simulação simples e não considera impostos, spreads, ajustes de contrato ou valor presente.")
