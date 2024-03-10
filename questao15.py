import numpy as np

def matriz_adicao(matriz1, matriz2):
    """
    Realiza a adição de duas matrizes nxn.
    """
    if matriz1.shape != matriz2.shape:
        raise ValueError("As matrizes devem ter o mesmo tamanho")

    return matriz1 + matriz2

def matriz_inversa(matriz):
    A_inv = np.linalg.inv(matriz) #função capaz de inverter uma matriz
    return A_inv

def matriz_multiplicacao_escalar(matriz, escalar):
    """
    Realiza a multiplicação de uma matriz nxn por um escalar.
    """
    return matriz * escalar


# Leitura das matrizes fornecidas pelo usuário
n = int(input("Digite o tamanho das matrizes (n): "))
matriz1 = np.array([[int(input(f"Matriz 1 [{i}][{j}]: ")) for j in range(n)] for i in range(n)])
matriz2 = np.array([[int(input(f"Matriz 2 [{i}][{j}]: ")) for j in range(n)] for i in range(n)])

# Operações com as matrizes
resultado_adicao = matriz_adicao(matriz1, matriz2)
resultado_inversa = matriz_inversa(matriz1)
escalar = int(input("Digite o escalar para multiplicação: "))
resultado_multiplicacao = matriz_multiplicacao_escalar(matriz1, escalar)

# Exibindo resultados
print("\nResultado da adição das matrizes:")
print(resultado_adicao)
print("\nInversa da matriz 1:")
print(resultado_inversa)
print("\nResultado da multiplicação da matriz 1 pelo escalar:")
print(resultado_multiplicacao)