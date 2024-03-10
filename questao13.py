import matplotlib.pyplot as plt
import numpy as np

# Definindo o número complexo c
n1=complex(input('escreva um numero complexo da forma a+ bj\n'))

# Definindo valores para a parte imaginária (i)
valoresimaginarios = np.linspace(-5, 5, 100)

# Calculando os novos números complexos c + i para cada valor de i
novonumero = [n1 + (1j * i) for i in valoresimaginarios]

# Extraindo as partes real e imaginária dos novos números complexos1+1j
real_parts = [z.real for z in novonumero]
imag_parts = [z.imag for z in novonumero]

# Plotando o gráfico
plt.plot(real_parts, imag_parts)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Variação de c + i para diferentes valores de i')
plt.grid(True)
plt.show()