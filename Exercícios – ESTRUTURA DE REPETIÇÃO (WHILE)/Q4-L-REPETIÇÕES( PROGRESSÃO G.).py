A0= int(input('Digite o valor inicial da P.A: '))
r= int(input('Digite a razão da P.A: '))
limite=int(input('Digite o limite da P.A: '))

n=1
valor=0

while valor<limite:
    valor = A0*(r**(n-1))
    print(f'{valor}')
    n+=1