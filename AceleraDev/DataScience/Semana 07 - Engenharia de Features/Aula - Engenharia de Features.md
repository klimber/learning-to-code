# Engenharia de Features

## Aula 01 - Introdução

Grande parte da habilidade do cientista é conversar com pessoas, identificar o problema delas, e converter em um modelo matemático. As features desse modelo matemático são os componentes chave que darão ao modelo uma boa acertividade.

## Aula 02 - Arquitetura padrão

Esta aula descreve uma das arquitetura de código recomendada na hora de desenvolver os modelos.

É importante padronizar a forma de desenvolver os modelos, pois facilita a comunicação entre os cientistas, e facilita a manutenção do código.

## Aula 03 - Arquitetura padrão II

Vide pasta `projeto padrão`

- Projeto Padrão
    - Data: `Utilizada para gravar os dados (csv, excel, etc) que serão utilizados`
    - Output: `Utilizada para as saídas do código`
    - Source: `Onde fica o código`

## Aulas 04, 05, 06 - Continuação da arquitetura padrão

Falando basicamente sobre padrões de Clean Code e orientação à objetos

## Aula 07 - Variáveis Categóricas

- Sem aplicações matemáticas
- Agrupadores, classificadores
- Possuem um limite de valores
- "Encode"
    - Label Encode
        - Maçã = 1
        - Galinha = 2
        - Broccoli = 3
    - One-hot encode
        - Coluna maçã (0/1)
        - Coluna Galinha (0/1)
        - Coluna Broccoli (0/1)

### Binarização

- Transforma valores escalares em binários
- Por padrão, tudo que é positivo recebe valor 1
- Boa prática normalizar/padronizar valores

### Quantização (Binning)

- Separa as amostras em quartis de quantidades iguais.
- **Bins**: Qunatidade de separações
- Permite o agrupamento e criação de ranges

## Aula 08 - Variáveis Numéricas e Outliers

- StandardScaler
    - Z-score
    - (X - Média) / (Desvio Padrão)
- MinMaxScaler
    - X_std = (X - X.min(axis=0))/(X.max(axis=0) - X.min(axis=0))
    - X_scaled = X_std * (max - min) + min

### Normalização, Transformação, Escala

- Aplicação de técnicas de normalização dos dados, de forma automática.
    - Preenchimento de valores faltantes;
    - Aplicação de padronização e normalização;
    - Transformação de colunas, por valores ou encode
- O agrupamento permite a criação de pipelines
    - Reaproveitamento dos cálculos
    - Aplicação Simultânea

### Remoção de Outliers

- Procurando por Outliers
- IQR
    - Menores que o Q1
    - Maiores que o Q3
    - Fórmula:
        - IQR: Q3 - Q1
        - Abaixo: Q1 - x*IQR
        - Acima: Q3 + x*IQR
        - x normalmente é 1.5

## Aula 09 - Features de Texto

- Categóricas por padrão
- Contagem
    - Palavras
    - Expressões
- TF-IDF
    - **Frequência do Termo:**  
    O peso de um termo que ocorre em um documento é diretamente proporcional à sua frequência
    - **Inverso da Frequência no documento:**  
    A especificidade de um termo pode ser quantificada por uma função inversa do número de documentos em que ela ocorre
- Agrupamentos de termos
- Ordenação
- N-gram
    - Agrupamento de 2 ou mais palavras, onde o a partir deste agrupamento passam a ser tratadas com um 1 elemento único
    - Stop-words:  
    Palavras ou composições que não impactam em valor o entendimento. Normalmente são palavras de ligação como artigos, advérbios, sufixos, prefixos e radicais.