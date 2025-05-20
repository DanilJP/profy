import streamlit as st
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

st.title("🧠 Clustering - Segmentos de Clientes")
st.markdown("Utilize KMeans para agrupar clientes com base em dados simulados.")

n_samples = st.slider("Número de clientes", 50, 500, 200)
n_clusters = st.slider("Número de segmentos (clusters)", 2, 10, 3)

X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=1.2, random_state=42)
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red')
ax.set_title("Segmentos de Clientes")
st.pyplot(fig)

