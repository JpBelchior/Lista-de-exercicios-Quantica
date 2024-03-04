#sabemos que as potencias de i seguem um padrao de repetição de modulo 4, então:

n=int(input('escolha um numero pra elevar i \n'))
if n%4==1:
    print('i elevado a {} é i' .format(n))
elif n%4==2:
    print('i elevado a {} é -1' .format(n))
elif n%4==3:
    print('i elevado a {} é -i' .format(n))
else :
    print('i elevado a {} é 1' .format(n))
