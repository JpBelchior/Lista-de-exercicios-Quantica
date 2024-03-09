import matplotlib.pyplot as plt
import numpy as np

# Vetores
vetor1 = (2, -1)
vetor2= (1, 1)

# Função para converter coordenadas cartesianas para polares
def cartesian_to_polar(x, y):
    rho = np.sqrt(x**2 + y**2)  # Magnitude
    phi = np.arctan2(y, x)      # Ângulo em relação ao eixo x
    return (rho, phi)

# Convertendo os vetores para coordenadas polares
rho1, phi1 = cartesian_to_polar(*vetor1)
rho2, phi2 = cartesian_to_polar(*vetor2)

soma_rho = rho1 + rho2
soma_phi = phi1 + phi2

dif_rho = rho1 - rho2
dif_phi = phi1 - phi2
# Plotagem
plt.figure(figsize=(10, 5))

# Plotando o vetor a
plt.polar([0, phi1], [0, rho1], marker='o', color='r', label='Vetor a (2, -1)')

# Plotando o vetor b
plt.polar([0, phi2], [0, rho2], marker='o', color='b', label='Vetor b (1, 1)')

# Plotando a soma dos vetores
plt.polar([0, soma_phi], [0, soma_rho], marker='o', color='g', label='Soma dos vetores')

# Plotando a diferença dos vetores
plt.polar([0, dif_phi], [0, dif_rho], marker='o', color='y', label='Diferença dos vetores')

# Configurações do gráfico polar
plt.grid(True)
plt.legend()
plt.title('Representação Polar dos Vetores')
plt.show()