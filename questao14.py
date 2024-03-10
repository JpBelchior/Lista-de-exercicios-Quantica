import matplotlib.pyplot as plt
import numpy as np

def mobius_transform(z):
    return (z + 1) / (z + 1)

# Criando uma grade de pontos no plano complexo
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Aplicando a transformação de Möbius a cada ponto na grade
W = mobius_transform(Z)

# Plotando os resultados
plt.figure(figsize=(8, 6))
plt.imshow(np.angle(W), extent=(-10, 10, -10, 10), cmap='hsv')
plt.colorbar(label='Argumento de f(z)')
plt.title('Transformação de Möbius com a = d = 0, b = c = 1')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)
plt.show()