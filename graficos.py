import matplotlib.pyplot as plt
import streamlit as st

def grafico_barras_exposicao(df):
    contagem = df['exposicao'].value_counts().sort_index()

    plt.figure()
    contagem.plot(kind='bar')
    plt.title("Distribuição de Exposição")
    plt.xlabel("Exposição (0=Não, 1=Sim)")
    plt.ylabel("Número de indivíduos")

    st.pyplot(plt)


def grafico_barras_doenca(df):
    contagem = df['doenca'].value_counts().sort_index()

    plt.figure()
    contagem.plot(kind='bar')
    plt.title("Distribuição de Doença")
    plt.xlabel("Doença (0=Não, 1=Sim)")
    plt.ylabel("Número de indivíduos")

    st.pyplot(plt)


def grafico_relacao_exposicao_doenca(df):
    tabela = df.groupby(['exposicao', 'doenca']).size().unstack()

    plt.figure()
    tabela.plot(kind='bar', stacked=True)
    plt.title("Exposição vs Doença")
    plt.xlabel("Exposição")
    plt.ylabel("Número de indivíduos")

    st.pyplot(plt)
