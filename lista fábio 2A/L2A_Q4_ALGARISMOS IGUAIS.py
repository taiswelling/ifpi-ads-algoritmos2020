#Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.

num1 = int(input("Digite um número de dois algarismos "))

dez = num1//10
res = num1%10

if dez==res:
    print('_______________________________________________________________')
    print('O algasrimo da dezena é igual ao algarismo da unidade')
    print('_______________________________________________________________')
else:
    print('_______________________________________________________________')
    print('O número possui os algarismos da dezena e centena diferentes.')
    print('_______________________________________________________________')