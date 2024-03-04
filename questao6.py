n1=complex(input('escolha um numero complexo\n'))
n2=complex(input('escolha outro numero complexo\n'))
n3=abs(n1)*abs(n2)
n4=abs(n1)+abs(n2)
n5= abs(n1+n2)
if abs(n1)*abs(n2)==abs(n1*n2):
    print(f'a multiplicação dos modulos é o modulo da multiplicação e vale {n3}')
if abs(n1)+abs(n2)>= abs(n1+n2):
        print(f'a soma dos modulos é sempre maior ou igual ao modulo da soma\n soma dos modulos: {n4}\n modulo da soma: {n5}')