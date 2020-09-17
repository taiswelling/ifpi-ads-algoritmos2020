n= int(input('Quantas vezes deseja dividir? '))

a=0
lista=[]
while a<n:
    a+=1
    s=(1/a)
    lista.append(s)

soma=0

for i in lista:
    soma+=i

print(f'{soma}')

