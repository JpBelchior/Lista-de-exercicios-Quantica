import numpy as np

def verificar_unitaria(matriz):
    """
    Verifica se uma matriz é unitária.
    """
    # Verifica se a matriz é quadrada
    n, m = matriz.shape
    if n != m:
        return False

    # Calcula o produto da matriz pelo seu conjugado transposto
    produto = np.dot(matriz, np.conj(np.transpose(matriz)))

    # Verifica se o produto é uma matriz de identidade
    return np.array_equal(produto, np.eye(n))

# Exemplo de uso da função:
n = int(input("Digite o tamanho da matriz (n): "))
matriz = np.array([[complex(input(f"Matriz [{i}][{j}]): ")) for j in range(n)] for i in range(n)])

# Verifica se a matriz é unitária
unitaria = verificar_unitaria(matriz)

# Exibe o resultado
if unitaria:
    print("\nA matriz é unitária.")
else:
    print("\nA matriz não é unitária.")
