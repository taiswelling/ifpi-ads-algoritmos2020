'''Um número é um quadrado perfeito quando a raiz quadrada do número
é igual à soma das dezenas formadas pelos seus dois primeiros e dois
últimos dígitos. Exemplo: √9801 = 99 = 98 + 01.
O número 9801 é um quadrado perfeito. Escreva um algoritmo que leia um
número de 4 dígitos e verifique se ele é um quadrado perfeito.'''

num = int(input('Digite um número de 4 dígitos:\n'))

import math

raiz=math.sqrt(num)
#print(f'{raiz}')

a= num//100
#print(f'{a}') (usado para conferir se resulta nos dois primeiros algarismos)

b=num%100
#print(f'{b}') (usado para conferir se resulta nos dois ultimos algarismos)

soma = a+b

if raiz==soma:
    print(40*'_')
    print("O número digitado é quadrado perfeito")
    print(40*'_')

else:
    print(50*'_')
    print('O número digitado não é um quadrado perfeito')
    print(50*'_')