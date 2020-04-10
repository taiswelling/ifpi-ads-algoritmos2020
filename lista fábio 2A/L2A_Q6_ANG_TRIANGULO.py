'''Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).'''

ang1 = int(input("Primeiro ângulo: "))
ang2 = int(input("Segundo ângulo: "))
ang3 = int(input("Terceiro ângulo: "))

n = ang1 + ang2 + ang3

if n!=180:
    print('Os angulos informados não formam um triâgulo')
elif(n==180) and (ang1==90 or ang2==90 or ang3==90):
    print('Os angulos informados formam um triânulo retângulo;')
elif(n==180) and (ang1>90 or ang2>90 or ang3>90):
    print('Os angulos informados formam um obtusângulo;')
elif(n==180) and (ang1<90 or ang2<90 or ang3<90):
    print('Os angulos informados formam um acutângulo;')
