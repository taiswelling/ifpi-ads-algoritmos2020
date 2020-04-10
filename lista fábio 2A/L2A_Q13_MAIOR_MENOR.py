'''Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
diferentes.'''


print('Digite 5 números diferente:')
num1 = int(input(" "))
num2 = int(input(" "))
num3 = int(input(" "))
num4 = int(input(" "))
num5 = int(input(" "))

#descobrir o maior
maior = num1

if num2 > maior:
    maior = num2

elif num3 > maior:
    maior = num3

elif num4 > maior:
    maior = num4

elif num5 > maior:
    maior = num5
print(20*'░')
print(f'O maior número é {maior}')

#Descobrir o menor número

menor = num1

if num2 < menor:
    menor = num2

elif num3 < maior:
    menor = num3

elif num4 < maior:
    menor = num4

elif num5 < maior:
    menor = num5


print(f'O menor número é {menor}')
print(20*'░')



#incorreta
