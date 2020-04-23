# 1. Leia um número e mostre na tela se o número é positivo ou negativo.

num = float(input('Insira um número qualquer:'))

if num>0:
    print('O número digitado é positivo;')

elif num<0:
    print('O número digitado é negativo;')

elif num==0:
    print('O número digitado é nulo;')