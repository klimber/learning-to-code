import pandas as pd
from scipy import stats

moda = lambda x: stats.mode(x)[0]

df = pd.read_csv("AceleraDev/DataScience/Semana 3/desafio/desafio1.csv")
result = df.groupby("estado_residencia").agg(
    moda=("pontuacao_credito", moda),
    mediana=("pontuacao_credito", "median"),
    media=("pontuacao_credito", "mean"),
    desvio_padrao=("pontuacao_credito", "std"),
)
result.to_json('AceleraDev/DataScience/Semana 3/desafio/submission.json', orient='index')