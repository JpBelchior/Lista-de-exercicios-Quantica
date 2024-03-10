import numpy as np

def produtokronecker(matriz1, matriz2):
    """
    Calcula o produto cartesiano de duas matrizes complexas.
    """
    # Calcula as dimensões das matrizes
    m, n = matriz1.shape
    p, q = matriz2.shape
    
    
    resultado = np.zeros((m * p, n * q), dtype=complex)#matrizes de zeros das dimensoes que queremos
    
    # Preenche a matriz resultante de acordo com kronecker
    for i in range(m):
        for j in range(n):
            resultado[i*p:(i+1)*p, j*q:(j+1)*q] = matriz1[i,j] * matriz2
    
    return resultado


n = int(input("Digite o número de linhas da primeira matriz: "))
m = int(input("Digite o número de colunas da primeira matriz: "))
p = int(input("Digite o número de linhas da segunda matriz: "))
q = int(input("Digite o número de colunas da segunda matriz: "))

# Leitura das matrizes fornecidas pelo usuário
matriz1 = np.array([[complex(input(f"Matriz 1 [{i}][{j}]): ")) for j in range(m)] for i in range(n)])
matriz2 = np.array([[complex(input(f"Matriz 2 [{i}][{j}]): ")) for j in range(q)] for i in range(p)])

# Calcula o produto cartesiano das matrizes fornecidas
resultado = produtokronecker(matriz1, matriz2)

# Exibe o resultado
print("\nProduto Cartesiano das Matrizes:")
print(resultado)
