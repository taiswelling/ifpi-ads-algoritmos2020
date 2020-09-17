n= int(input('Quantos valores você deseja?'))

n1=0
n2=1
print(f'{n1}, {n2}', end='')

n3=n1+n2

contador=3

while contador<=n:
    n3=n1+n2
    print(f', {n3}', end='')
    n1=n2
    n2=n3
    contador+=1