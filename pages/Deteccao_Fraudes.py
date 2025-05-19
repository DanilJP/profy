import streamlit as st
from sklearn.datasets import make_classification
from sklearn.ensemble import IsolationForest
import pandas as pd

st.title("🚨 Detecção de Fraudes com Machine Learning")

# Gera dados sintéticos com outliers
X, _ = make_classification(n_samples=500, n_features=5, random_state=42)
df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(X.shape[1])])

st.write("Dataset:")
st.write(df.head())

# Treina Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)

df['Fraude?'] = model.predict(df)
df['Fraude?'] = df['Fraude?'].map({1: 'Não', -1: 'Sim'})

st.write("Resultado da detecção de fraudes:")
st.write(df.head(10))
