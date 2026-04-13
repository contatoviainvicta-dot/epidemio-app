import streamlit as st
import pandas as pd
from epidemiologia import tabela_2x2, calcular_medidas
from graficos import (
    grafico_barras_exposicao,
    grafico_barras_doenca,
    grafico_relacao_exposicao_doenca
)
st.set_page_config(page_title="Epidemiologia Clínica", layout="centered")

st.title("📊 Calculadora Epidemiológica")

st.write("Faça upload de uma planilha Excel com colunas: exposicao e doenca")

arquivo = st.file_uploader("Upload do Excel", type=["xlsx"])

if arquivo:
    df = pd.read_excel(arquivo)

    st.subheader("📄 Dados carregados")
    st.dataframe(df)

    a, b, c, d = tabela_2x2(df)

    st.subheader("📊 Tabela 2x2")
    st.write(f"""
    Expostos doentes (a): {a}  
    Expostos não doentes (b): {b}  
    Não expostos doentes (c): {c}  
    Não expostos não doentes (d): {d}
    """)

    resultados = calcular_medidas(a, b, c, d)

    st.subheader("📈 Resultados")
    for k, v in resultados.items():
        if v is not None:
            st.write(f"**{k}:** {v:.4f}")
        else:
            st.write(f"**{k}:** indefinido")

    # Interpretação clínica automática
    st.subheader("🧠 Interpretação clínica")

    if resultados['RR']:
        if resultados['RR'] > 1:
            st.write("👉 Associação positiva (fator de risco)")
        elif resultados['RR'] < 1:
            st.write("👉 Possível fator protetor")
        else:
            st.write("👉 Sem associação")

    if resultados['Sensibilidade'] > 0.8:
        st.write("👉 Teste bom para triagem")

    if resultados['Especificidade'] > 0.8:
        st.write("👉 Teste bom para confirmação")
st.subheader("📊 Visualizações")

grafico_barras_exposicao(df)
grafico_barras_doenca(df)
grafico_relacao_exposicao_doenca(df)
