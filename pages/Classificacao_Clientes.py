import streamlit as st
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

st.title("🧮 Classificação de Clientes para Marketing")

# Gerar dataset sintético
X, y = make_classification(n_samples=500, n_features=5, random_state=42)
df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(X.shape[1])])
df['Target'] = y

st.write("Dataset:")
st.write(df.head())

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treino modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Previsões
y_pred = model.predict(X_test)

# Relatório
report = classification_report(y_test, y_pred, output_dict=True)
st.write("Relatório de Classificação:")
st.json(report)
