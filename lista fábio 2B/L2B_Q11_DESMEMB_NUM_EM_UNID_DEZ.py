'''11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do número. Observando os termos no plural a colocação do "e",
da vírgula entre outros.
Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades '''

num = int(input('Digite um número entre zero e 1000:\n'))

cent = num//100
rest1 = num%100
dez = rest1//10
uni = rest1%10


if num<0 or num>1000:
    print('################################')
    print('ERRO!\nVocê digitou um valor inválido!\nTente novamente!')
    print('################################')

elif num==1000:
    print('################################')
    print('10 centenas,0 dezena e 0 unidade.')
    print('################################')

elif num>=0 and num<=99:
    print('#############################################################')
    print(f'O {num} =  {dez} dezena(s) e {uni} unidade(s)')
    print('##############################################################')

elif num<1000 and num>=100:
    print('#############################################################')
    print(f'O {num} = {cent} centena(s), {dez} dezena(s) e {uni} unidade(s)')
    print('##############################################################')