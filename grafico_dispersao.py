import matplotlib.pyplot as plt

# Cria duas listas de valores
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Cria o gráfico de dispersão
plt.scatter(x, y)

# Define o título e os rótulos dos eixos
plt.title('Gráfico de dispersão')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')

# Mostra o gráfico
plt.show()
