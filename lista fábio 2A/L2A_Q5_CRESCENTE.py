#Leia 3 (três) números e escreva-os em ordem crescente.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))


lista = (num1,num2,num3)

print('A ordem crescente destes números é:', sorted(lista))
