#propriedade comutativa:
n1=complex(input('escreva um numero complexo da forma a+ bj\n'))
n2=complex(input('escreva um numero complexo da forma a+ bj\n'))
n3=n1+n2
n4=n1*n2
n5=(n1+n2)+n3
n6=(n1*n2)*n3
if n1+n2==n2+n1 and n1*n2==n2*n1:
    print(f'a propriedade comutativa é valida e a soma vale{n3} e a multiplicação vale{n4}')
else:
    print('não é valida a propriedade comutativa')
#propriedade associativa:
if (n1+n2)+n3==n1+(n2+n3) and (n1*n2)*n3==n1*(n2*n3):
    print(f'a propriedade associativa é valida e a soma vale{n5} e a multiplicação vale{n6}')
else:
    print('não é valida a propriedade associativa')
#propriedade distributiva
if n1*(n2+n3) == n1*n2 + n3*n1:
    print(' é valida a propriedade distributiva')
else:
    print('não é valida a propriedade distributiva')

