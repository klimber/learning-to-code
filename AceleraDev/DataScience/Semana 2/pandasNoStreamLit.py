import streamlit as st
import pandas as pd


def exibeDataFrame(myCsv):
    df = pd.read_csv(myCsv)
    st.subheader("Podemos exibir o dataframe utilizando o comando mágico do StreamLit")
    df

    st.subheader("Ou utilizando o st.dataframe, que nos permitirá utilizar métodos como o head()")
    qntLinhas = st.slider("Quantas linhas você deseja visualizar?", 1,len(df))
    st.dataframe(df.head(qntLinhas))

    st.subheader("Podemos exibir também em formato de tabela!")
    st.table(df.head(qntLinhas))

def main():
    st.title("Usando Pandas no StreamLit")

    st.subheader("Primeiro enviamos um arquivo csv qualquer!")
    myCsv = st.file_uploader("Selecione um arquivo .csv", "csv")

    if myCsv is not None:
        exibeDataFrame(myCsv)


if __name__ == "__main__":
    main()