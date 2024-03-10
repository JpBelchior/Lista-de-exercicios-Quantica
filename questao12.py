import matplotlib.pyplot as plt
import numpy as np

# Definindo o número complexo c
n1=complex(input('escreva um numero complexo da forma a+ bj\n'))

# Definindo os valores de n de 1 a 10
n_values = np.arange(1, 11)

# Calculando os valores correspondentes de c^n para cada valor de n
n1potencia = [n1**n for n in n_values]

# Extraindo as partes real e imaginária dos valores
real_parts = [z.real for z in n1potencia]
imag_parts = [z.imag for z in n1potencia]

# Plotando o gráfico
plt.plot(real_parts, imag_parts, marker='o')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Variação de c^n com n de 1 a 10')
plt.grid(True)
plt.show()