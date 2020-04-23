'''5-Leia o preço de três produtos e informe qual produto deve ser comprado,
sabendo que a decisão é sempre pelo mais barato.'''

val1 = float(input("Primeiro valor: "))
val2 = float(input("Segundo valor: "))
val3 = float(input("Terceiro valor: "))


if val1==val2==val3:
    print('Todos os valores digitados são iguais.\nAssim, não existirá um menor valor.')

elif val1==val2 and val1<val3:
    print(f'O menor valor é R${val1}')

elif val1==val3 and val1<val2:
    print(f'O menor valor é R${val1}')

elif val2==val3 and val2<val1:
    print(f'O menor valor é R${val2}')

elif val1<val2 and val1<val3:
    print(f'O menor valor é R${val1};')

elif val2<val1 and val2<val3:
    print(f'O menor valor é R${val2};')

elif val3<val1 and val3<val2:
    print(f'O menor valor é R${val3};')