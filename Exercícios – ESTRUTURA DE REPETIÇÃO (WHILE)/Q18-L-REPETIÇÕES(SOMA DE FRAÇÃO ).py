n = int(input('Por qual valor deseja começar? '))

a=1
lista=[]

while n>=1:
    s=(a/n)
    lista.append(s)
    n-=1
    a+=1
    

soma=0

for i in lista:
    soma+=i

print(f'{soma}')