import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração para Telemóvel
st.set_page_config(page_title="Wealth Engine", layout="centered")

st.title("📊 Dashboard de Lucratividade")

# Dados exemplo (Pode editar os valores aqui)
data = {
    'Local': ['Bar Costa', 'Bar Praia'],
    'Vendas': [58.20, 65.80],
    'Lucro': [61.50, 62.50]
}

df = pd.DataFrame(data)

# Indicadores Rápidos
col1, col2 = st.columns(2)
col1.metric("Venda Total", f"{df['Vendas'].sum():.2f}€")
col2.metric("Lucro Total", f"{df['Lucro'].sum():.2f}€")

# Gráfico
fig = px.bar(df, x='Local', y='Lucro', color='Local', text_auto='.2f', title="Performance por Local")
st.plotly_chart(fig, use_container_width=True)

# Tabela
st.dataframe(df, use_container_width=True)
