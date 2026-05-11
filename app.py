import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gestão de Bares", layout="centered")

st.title("📊 Gestão de Bares - Performance")

st.subheader("📝 Registar Valores do Dia")
c1, c2 = st.columns(2)
with c1:
    v_costa = st.number_input("Venda Bar Costa (€)", min_value=0.0, value=1250.0)
    k_costa = st.number_input("Custos Bar Costa (€)", min_value=0.0, value=450.0)
with c2:
    v_praia = st.number_input("Venda Bar Praia (€)", min_value=0.0, value=1420.0)
    k_praia = st.number_input("Custos Bar Praia (€)", min_value=0.0, value=510.0)

data = {
    'Local': ['Bar Costa', 'Bar Praia'],
    'Vendas': [v_costa, v_praia],
    'Custos': [k_costa, k_praia],
    'Lucro': [(v_costa - k_costa), (v_praia - k_praia)]
}
df = pd.DataFrame(data)

st.divider()
m1, m2 = st.columns(2)
m1.metric("Faturação Total", f"{df['Vendas'].sum():,.2f}€")
m2.metric("Lucro Real", f"{df['Lucro'].sum():,.2f}€")

fig = px.bar(df, x='Local', y=['Custos', 'Lucro'], 
             title="Análise de Rentabilidade",
             barmode='stack',
             color_discrete_map={'Custos': '#ef553b', 'Lucro': '#00cc96'},
             template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)
