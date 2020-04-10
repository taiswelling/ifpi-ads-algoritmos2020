# Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if num1==num2==num3:
    print('Existem 3 numeros iguais.')

elif num1==num3:
    print('Existem 2 numeros iguais.')

elif num2==num3:
     print('Existem 2 numeros iguais.')

elif num1==num2:
     print('Existem 2 numeros iguais.')

else:
    print('Os números digitados são todos diferentes')