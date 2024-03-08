import matplotlib.pyplot as plt

# Vetores
vetor1 = (2, -1)
vetor2 = (1, 1)

# Soma dos vetores
soma_vetores = (vetor1[0] + vetor2[0], vetor1[1] + vetor2[1])

# Diferença dos vetores
diferenca_vetores = (vetor1[0] - vetor2[0], vetor1[1] - vetor2[1])

# Plotagem
plt.figure(figsize=(10, 5))

# Plotando o vetor a
plt.quiver(0, 0, vetor1[0], vetor1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor a (2, -1)')

# Plotando o vetor b
plt.quiver(0, 0, vetor2[0], vetor2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vetor b (1, 1)')

# Plotando a soma dos vetores
plt.quiver(0, 0, soma_vetores[0], soma_vetores[1], angles='xy', scale_units='xy', scale=1, color='g', label='Soma dos vetores')

# Plotando a diferença dos vetores
plt.quiver(0, 0, diferenca_vetores[0], diferenca_vetores[1], angles='xy', scale_units='xy', scale=1, color='y', label='Diferença dos vetores')

# Configurações do gráfico
plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Operações com Vetores')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
