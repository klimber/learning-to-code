#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:


# Imprime as primeiras 10 linhas do dataFrame para visualizarmos os dados
black_friday.head(10)


# In[ ]:


# Quantidade de Linhas e Colunas do DataFrame
black_friday.shape


# In[ ]:


# Tipos de dados atuais das colunas
black_friday.info()


# In[ ]:


# Armazenando a resposta para a Q4 antes de realizar modificações no DataFrame
R4 = black_friday.dtypes.nunique()


# In[ ]:


# Verificando a quantidade de dados únicos em cada coluna
black_friday.nunique()


# In[ ]:


# Gênero é um tipo de dados categórico, ajustando o tipo de dados
black_friday.Gender = black_friday.Gender.astype("category")
black_friday.Gender
# Vemos aqui que são utilizadas as letras M (Male) e F (Female) para designar os sexos.


# In[ ]:


# Age neste DataFrame represeta faixa-etária, portanto também é categórico
black_friday.Age = black_friday.Age.astype("category")
black_friday.Age
# Aqui podemos ver que são utilizadas as faixas etárias: 0-17, 18-25, 26-35, 36-45, 46-50, 51-55, 55+


# In[ ]:


# Existen número finito de tipos de produtos, este também representa uma categoria
black_friday.Product_ID = black_friday.Product_ID.astype("category")
black_friday.Product_ID
# Vemos então que foram vendidos um total de 3623 produtos distintos


# In[ ]:


# Cada User_ID representa um usuário único, portanto também é uma informação categórica
black_friday.User_ID = black_friday.User_ID.astype("category")
black_friday.User_ID
# Aqui percebemos que há 5891 usuários distintos no DataFrame


# In[ ]:


# Occupation provavelmente representa o código de uma determinada ocupação no sistema, sendo também categórico
black_friday.Occupation = black_friday.Occupation.astype("category")
black_friday.Occupation
# Vemos aqui que há 21 ocupações distintas


# In[ ]:


# Analisando a coluna Marital_Status através do método unique(), podemos ver que só há 2 valores possíveis: 0 e 1.
black_friday.Marital_Status.unique()


# In[ ]:


# A coluna provavelmente se trata de um valor booleano onde 0 = "Solteiro" e 1 = "Casado", adequanto o dataType:
black_friday.Marital_Status = black_friday.Marital_Status.astype("bool")
black_friday.Marital_Status


# In[ ]:


# As colunas Product_Category_1, Product_Category_2 e Product_Category_3, como o próprio nome sugere, então realizando a análise de value_counts, representam categorias
black_friday.Product_Category_3.value_counts() # Realizar a checagem para as 3 colunas


# In[ ]:


# Realizando o ajuste no tipo de dados, realizado cast para int pois não há números decimais, e então categorizado os dados
# Como não há muitas categorias, e elas possuem valores vazios, utilizarei "Int8"
black_friday.Product_Category_1 = black_friday.Product_Category_1.astype("Int8").astype("category")
black_friday.Product_Category_2 = black_friday.Product_Category_2.astype("Int8").astype("category")
black_friday.Product_Category_3 = black_friday.Product_Category_3.astype("Int8").astype("category")


# In[ ]:


# Realizando tratamento similar para as colunas City_Category e Stay_In_Current_City_Years
black_friday.City_Category = black_friday.City_Category.astype("category")
black_friday.City_Category


# In[ ]:


black_friday.Stay_In_Current_City_Years = black_friday.Stay_In_Current_City_Years.astype("category")
black_friday.Stay_In_Current_City_Years


# In[ ]:


# Ao verificar novamente as informações do dataFrame, verificamos uma redução significativa no uso de memória
black_friday.info()
# De 49,2 Mb para 11,2 Mb, isso tornará a computação dos dados mais fácil


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[ ]:


def q1():
    # A resposta é o retorno do método shape:
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[ ]:


def q2():
    # Filtrando pelo Gênero e Faixa Etária, e então retornando a contagem de usuários únicos
    # return black_friday[(black_friday.Gender == "F") & (black_friday.Age == "26-35")].User_ID.nunique()
    # Trocado pela contagem de observações para adequar ao teste da codenation
    return int(black_friday[(black_friday.Gender == "F") & (black_friday.Age == "26-35")].User_ID.count())


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[ ]:


def q3():
    # Número de valores únicos na coluna User_ID
    return black_friday.User_ID.nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[ ]:


def q4():
    # A resposta pra essa pergunta depende dos tipos de transformações que foram realizadas no dataset... não acho uma pergunta apropriada.
    # Vou responder com o número dtypes antes das transformações...
    return R4


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[ ]:


def q5():
    # O número de registros completos é a quantidade de linhas do DataFrame.dropna()
    # O número de registros completos sobre o total de registros é a porcentagem de completos
    # Subtraindo este valor de 1, obtemos a resposta
    return 1 - black_friday.dropna().shape[0]/black_friday.shape[0]


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[ ]:


def q6():
    # Verifica coluna a coluna o número de valores faltantes, retorna o maior
    return int(black_friday.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[ ]:


def q7():
    # Realiza a contagem dos valores da série, considerando ordem decrescente, e retorna o primeiro índice.
    return black_friday.Product_Category_3.value_counts(ascending=False).first_valid_index()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[ ]:


def q8():
    # Normaliza a coluna Purchase e retorna a sua média
    purchaseMin = black_friday.Purchase.min()
    purchaseMax = black_friday.Purchase.max()
    normalizedPurchase = (black_friday.Purchase - purchaseMin)/(purchaseMax - purchaseMin)
    return float(normalizedPurchase.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[ ]:


def q9():
    # Padroniza a coluna Purchase e retona a quantidade de registros entre -1 e 1
    purchaseStd = black_friday.Purchase.std()
    purchaseMean = black_friday.Purchase.mean()
    standardizedPurchase = (black_friday.Purchase - purchaseMean)/purchaseStd
    return int(standardizedPurchase[standardizedPurchase.abs() <= 1].count())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[ ]:


def q10():
    # Filtra o dataFrame onde Product_Category_2 é nulo
    # Para satisfazer à condição, o número de observações válidas de Product_Category_3 deve ser 0
    return bool(black_friday[black_friday.Product_Category_2.isna()].Product_Category_3.count() == 0)

