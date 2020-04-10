'''Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
coeficiente A deve ser diferente de 0 (zero).'''

print (' Vamos calcular as raízes da sua equação de primeiro grau:')

a = float(input('Digite o valor de "a", diferente de zero:\n'))
b = float(input('Digite o valor de "b":\n'))
c = float(input('Digite o valor de "c":\n'))

# se todos os coeficientes forem diferentes de zero

delta = ((b**2)-(4*a*c))

x1 = (((-b) + (((b**2)-(4*a*c))**0.5))/2*a)
x2 = (((-b) - (((b**2)-(4*a*c))**0.5))/2*a)

# se b=0
xb1= ((+1)* (((-1)*(c/a))**0.5))
xb2= ((-1)* (((-1)*(c/a))**0.5))

#se c=0
xc1= 0
xc2= (-1)*(b/a)


if delta<0:
    print('A equação não possui raizes reais;')

elif a==0:
    print('ERRO! Digite o valor de "a", diferente de zero')

elif b==0:
    print(f'As raízes são {xb1} e {xb2}')

elif c==0:
    print(f'As raízes são {xc1} e {xc2}')

elif (a!=0) and (b!=0) and (c!=0):
    print(f'As raízes são {x1} e {x2}')


