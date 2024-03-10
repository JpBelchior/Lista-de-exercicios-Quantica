import numpy as np

def verificar_hermitiana(matriz):
    """
    Verifica se uma matriz é hermitiana.
    Retorna True se a matriz for hermitiana, False caso contrário.
    """
    conjugada_transposta = np.conj(np.transpose(matriz))
    
    # Calcula o produto de Kronecker entre a matriz original e sua conjugada transposta
    produto_kronecker = np.kron(matriz, conjugada_transposta)
    
    # Verifica se a matriz resultante do produto de Kronecker é igual à sua transposta
    return np.array_equal(produto_kronecker, np.transpose(produto_kronecker))

# Exemplo de uso da função:
n = int(input("Digite o número de linhas e colunas da matriz: "))
matriz = np.array([[complex(input(f"Matriz [{i}][{j}]): ")) for j in range(n)] for i in range(n)])

# Verifica se a matriz é hermitiana
hermitiana = verificar_hermitiana(matriz)

if hermitiana:
    print("\nA matriz é hermitiana.")
else:
    print("\nA matriz não é hermitiana.")
