import matplotlib.pyplot as plt

# Cria uma lista de valores
dados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7]

# Cria o boxplot
plt.boxplot(dados)

# Define o título e os rótulos dos eixos
plt.title('Boxplot de dados')
plt.ylabel('Valores')

# Mostra o gráfico
plt.show()
