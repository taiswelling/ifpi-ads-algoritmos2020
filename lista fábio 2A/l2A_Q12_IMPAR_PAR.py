#Leia 1 (um) número inteiro e escreva se este número é par ou impar.

num= int(input('Digite um valor inteiro: '))

resto = num % 2

if resto == 0:
    print(24*'_')
    print('O numero digitado é par.')
    print(24*'_')

else:
    print(24*'_')
    print('O número digitado é impar.')
    print(24*'_')

