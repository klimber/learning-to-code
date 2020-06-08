# Regressão e Cloud

É importante que o cientista de dados entenda sobre Cloud.
As exigências do mercado para um cientista de dados são bastante pesados.

Os papéis dentro de um time de dados não costumam ser bem definidas, sendo assim, é importante a multidisciplinaridade.

# Data Life Cycle

Ciclo de estágios que um dado passa desde sua captura até seu eventual arquivamento/deleção ao final de sua vida útil.

Criação
Processamento
Análise
Preservamento
Acesso
Re-utilização

# Trade Off Bias x Variance

## Viés (Bias)
- Se deve à escolha do modelo, que pode ter sido muito simples para o problema em mãos
- É relacionado ao underfitting dos dados

## Variância
- Está relacionada à complexidade do modelo
- Qualquer dado externo do conjunto de treino é considerado ruído

# Overfitting
- Um modelo complexo
- Reduz o erro a praticamente 0 no treinamento
- Viés Baixo
- Alta Variância
- Só funciona nos dados de treino

# Underfitting
- Um modelo genérico ou desajustado
- Alto erro
- Viés mais alto
- Baixa Variância
- Funciona com alto erro tanto em treino como em teste

# Se tiver ALTO PROBLEMA DE VARIEDADE
- Obter mais exemplos de treinamento, porque quanto maior o conjunto de dados, maior a probabilidade de obter previsões mais assertivas
- Experimente conjuntos menores de features (porque está ajustando demais)

# Se tiver ALTO PROBLEMA DE BIAS
- Tente obter recursos adicionais, você está generalizando os conjuntos de dados
- Tente adicionar recursos polinomiais, torne o modelo mais complicado.