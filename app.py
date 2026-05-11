import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Motor de Riqueza", layout="centered")
st.title("📊 Dashboard de Lucratividade")

data = {'Local': ['Bar Costa', 'Bar Praia'], 'Vendas': [58.20, 65.80], 'Lucro': [61.50, 62.50]}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)
col1.metric("Venda Total", f"{df['Vendas'].sum():.2f}€")
col2.metric("Lucro Total", f"{df['Lucro'].sum():.2f}€")

fig = px.bar(df, x='Local', y='Lucro', color='Local', text_auto='.2f')
st.plotly_chart(fig, use_container_width=True)
