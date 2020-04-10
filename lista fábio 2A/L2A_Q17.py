'''Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
escreva o quadrado dos números lidos.'''

var1= int(input('Digite o primeiro valor inteiro:\n'))
var2= int(input('Digite o segundo valor inteiro:\n'))

res1 = var1 % var2
soma1 = (var1 + var2) + res1

par1=var1%2 
par2=var2%2

mult = (var1+var2)*var1

quad1 = var1**2
quad2 = var2**2


if res1==1:
    print(20*('_'))
    print(f'{soma1}')
    print(20*('_'))

elif res1==2:
    if par1==0 and par2==0:
        print(20*('_'))
        print(f'As duas variáveis ({var1} e {var2}) são par.')
        print(20*('_'))

    elif par1==0 and par2 !=0:
        print(20*('_'))
        print(f'a primeira variável ({var1}) é par e a segunda variável ({var2}) é impar.')
        print(20*('_'))

    elif par2==0 and par1 !=0:
        print(20*('_'))
        print(f'a primeira variável ({var1}) é ímpar e a segunda variável ({var2}) é par.')
        print(20*('_'))

    elif par1!=0 and par2 !=0:
        print(20*('_'))
        print(f'As duas variáveis({var1} e {var2}) são impar.')
        print(20*('_'))

elif res1==3:
    print(20*('_'))
    print(f'{mult}')
    print(20*('_'))

elif res1==4:
    if var2==0:
        div = (var1+var2)/var2
        print(20*('_'))
        print(f'{div}')
        print(20*('_'))

else:
    print(f'O qudrado dos numeros digitados são:\n {quad1} para o primeiro valor \n {quad2} para o segundo valor')