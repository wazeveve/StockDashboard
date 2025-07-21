import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Stock Market Dashboard")

# Entrada do usuário
ticker = st.text_input("Digite o código da ação: ", "PETR4.SA")
period = st.selectbox("Período", ["7d", "1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

# Coleta os dados
data = yf.download(ticker, period=period)

if data.empty:
    st.error("Não foi possível obter os dados. Verifique o código da ação.")
else:
    st.success(f"Dados carregados para {ticker}")


    data.columns = ['_'.join(col).strip() for col in data.columns.values]

    close_col = f'Close_{ticker}'

    # Cria o gráfico com Plotly Express
    fig = px.line(
    data,
    x=data.index, 
    y=close_col,
    title=f'{ticker} - Preço de Fechamento',
    labels={close_col: 'Preço (R$)', 'index': 'Data'}
)
    fig.update_layout(xaxis_title='Data', yaxis_title='Preço (R$)')
    st.plotly_chart(fig, use_container_width=True)

    # === TABELA DE VARIAÇÃO ===
    close_col = f'Close_{ticker}'

    # Calcula a variação percentual
    data['Retorno (%)'] = data[close_col].pct_change() * 100

    # Cria novo DataFrame para exibir
    variacao = pd.DataFrame({
        'Data': data.index,
        'Preço de Fechamento (R$)': data[close_col].round(2),
        'Retorno (%)': data['Retorno (%)'].round(2)
    }).dropna()

    st.subheader("📊 Variação percentual diária")
    st.dataframe(variacao)
