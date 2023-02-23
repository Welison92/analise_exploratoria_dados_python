import matplotlib.pyplot as plt

# Cria duas listas de valores
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 15, 5, 20, 12]

# Cria o gráfico de barras
plt.bar(categorias, valores)

# Define o título e os rótulos dos eixos
plt.title('Gráfico de barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Mostra o gráfico
plt.show()
