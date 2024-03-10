import numpy as np
def traco(matriz):
    traco=0
    i=0
    for i in range(n):
        traco+=matriz[i][i]
    return traco
    
n = int(input("Digite o número de linhas e colunas da matriz: "))

matriz1 = np.array([[complex(input(f"Matriz 1 [{i}][{j}]): ")) for j in range(n)] for i in range(n)])

traco=traco(matriz1)
print(f"\n o traco da matriz é:\n {traco}")
