import numpy as np

def produto_hadamard(matriz1, matriz2):
    """
    Calcula o produto de Hadamard entre duas matrizes complexas.
    """
    if matriz1.shape != matriz2.shape:
        raise ValueError("As matrizes devem ter o mesmo tamanho")

    return matriz1 * matriz2

n = int(input("Digite o número de linhas e colunas das matrizes: "))
matriz1 = np.array([[complex(input(f"Matriz 1 [{i}][{j}]): ")) for j in range(n)] for i in range(n)])
matriz2 = np.array([[complex(input(f"Matriz 2 [{i}][{j}]): ")) for j in range(n)] for i in range(n)])

# Calcula o produto de Hadamard das matrizes fornecidas
resultado = produto_hadamard(matriz1, matriz2)

# Exibe o resultado
print("\nProduto de Hadamard das Matrizes:")
print(resultado)