#Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

print('Digite 5 números inteiros:')
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
num4 = int(input(""))
num5 = int(input(""))

med = (num1 + num2 + num3 + num4 + num5)/5
maior = med
print(20*'-')
print(f'A média é: {med}')
print(20*'-')

print('Os números maiores que a média dos valores digitados, são:')
print('......')

if num1 > med:
    maior = num1
    print(f'{num1}')

if num2 > med:
    maior = num2
    print(f'{num2}')

if num3 > med:
    maior = num3
    print(f'{num3}')

if num4 > med:
    maior = num4
    print(f'{num4}')

if num5 > med:
    maior = num5
    print(f'{num5}')

print('......')