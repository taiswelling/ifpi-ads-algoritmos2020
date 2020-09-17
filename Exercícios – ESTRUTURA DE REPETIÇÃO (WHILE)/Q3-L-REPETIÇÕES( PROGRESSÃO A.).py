A0= int(input('Digite o valor inicial da P.A: '))
r= int(input('Digite a razão da P.A: '))
limite=int(input('Digite o limite da P.A: '))

n=1
valor=0

while valor<limite:
    valor = A0+((n-1)*r)
    print(f'{valor}')
    n+=1

