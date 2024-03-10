import numpy as np

def matriz_transposta_conjugada_dagger(matriz):
    """
    Calcula a transposta, conjugada e adjunta (dagger) de uma matriz complexa.
    Retorna a transposta, conjugada e adjunta da matriz fornecida.
    """
    # Calcula a transposta da matriz
    transposta = np.transpose(matriz)
    
    # Calcula a conjugada da matriz
    conjugada = np.conj(matriz)
    
    # Calcula a adjunta (dagger) da matriz (transposta da conjugada)
    dagger = np.transpose(conjugada)

    return transposta, conjugada, dagger

# Exemplo de uso da função:
n = int(input("Digite o tamanho das matrizes (n): "))
matriz_complexa = np.array([[complex(input(f"Matriz [{i}][{j}] (real, imaginário): ")) for j in range(n)] for i in range(n)])

# Calcula a transposta, conjugada e adjunta da matriz complexa fornecida
transposta, conjugada, dagger = matriz_transposta_conjugada_dagger(matriz_complexa)

# Exibe os resultados
print("\nTransposta da matriz:")
print(transposta)
print("\nConjugada da matriz:")
print(conjugada)
print("\nAdjunta (Dagger) da matriz:")
print(dagger)