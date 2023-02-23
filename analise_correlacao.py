import pandas as pd

# Cria um dataframe com duas colunas
df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})

# Calcula o coeficiente de correlação de Pearson
corr = df['x'].corr(df['y'])

# Imprime o coeficiente de correlação
print('Coeficiente de correlação: ', corr)
