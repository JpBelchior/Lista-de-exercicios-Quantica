import math 
def conjugate(numcomplex):
    partR=numcomplex.real
    partI=numcomplex.imag
    conjugatenum=complex(partR,-partI)
    return conjugatenum

n1=complex(input('escolha um numero complexo:'))
n2=complex(input('escolha outro numero complexo:'))
n3=conjugate(n1)
n4=conjugate(n2)
n5=conjugate(n1+n2)
n6=conjugate(n1*n2)
if n3+n4==n5:
    print(f'a soma dos conjugados é o conjugado da soma e vale {n5}')
else:
    print('propriedade invalida')
if n3*n4==n6:
    print(f'a multiplicaçao dos conjugados é o conjugado da multiplicaçao e vale {n6}')
else:
    print('a propriedade nao é valida')

