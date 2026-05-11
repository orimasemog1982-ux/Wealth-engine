import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Motor de Riqueza", layout="wide")

st.title("🍹 Gestão Operacional - Bares")

# --- ENTRADA DE DADOS ---
with st.expander("📝 Lançamentos Diários", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        v_total = st.number_input("Faturação Bruta (€)", value=2670.0)
    with c2:
        c_fornec = st.number_input("Fornecedores (€)", value=450.0)
    with c3:
        c_staff = st.number_input("Staff/Empregados (€)", value=200.0)
    with c4:
        n_mesas = st.number_input("Número de Mesas", value=45)

# --- CÁLCULOS ---
lucro = v_total - c_fornec - c_staff
ticket_medio = v_total / n_mesas if n_mesas > 0 else 0

# --- MÉTRICAS ---
st.divider()
idx1, idx2, idx3 = st.columns(3)
idx1.metric("Lucro Líquido", f"{lucro:,.2f}€")
idx2.metric("Ticket Médio", f"{ticket_medio:,.2f}€")
idx3.metric("Custos Totais", f"{(c_fornec + c_staff):,.2f}€")

# --- GRÁFICOS DE LINHA HORIZONTAL (INDICADORES) ---
st.subheader("📈 Performance em Linha")

# Criar dados para as linhas
df_plot = pd.DataFrame({
    'Indicador': ['Vendas', 'Custos', 'Lucro'],
    'Valor': [v_total, (c_fornec + c_staff), lucro]
})

# Gráfico de barras horizontais (que funcionam como linhas de progresso)
fig = px.bar(df_plot, 
             x='Valor', 
             y='Indicador', 
             orientation='h', 
             text='Valor',
             color='Indicador',
             color_discrete_map={'Vendas': '#00CC96', 'Custos': '#EF553B', 'Lucro': '#636EFA'},
             template="plotly_dark")

fig.update_traces(texttemplate='%{text:.2f}€', textposition='outside')
fig.update_layout(showlegend=False, height=300)

st.plotly_chart(fig, use_container_width=True)

# --- TABELA DE FORNECEDORES E STAFF ---
st.subheader("📋 Detalhe de Custos")
detalhe = pd.DataFrame({
    'Descrição': ['Pagamentos Fornecedores', 'Salários Staff', 'Outras Despesas'],
    'Valor Pago': [c_fornec, c_staff, 0.0]
})
st.table(detalhe)
