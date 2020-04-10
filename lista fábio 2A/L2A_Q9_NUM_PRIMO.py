#Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.


n = int(input('Digite um número inteiro entre 1 e 100:  '))
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

if n in primos:
    print('O número digitado é primo.')

else:
    print('O número digitado não é primo.')

