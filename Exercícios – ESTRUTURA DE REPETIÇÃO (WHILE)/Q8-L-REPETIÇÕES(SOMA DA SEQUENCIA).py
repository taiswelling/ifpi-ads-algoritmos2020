n=int(input('Digite um valor: '))

a=0
lista=[]
total=0

while a<n:
    a+=1
    lista.append(a) #adiciona cada valor à uma lista

for i in range(len(lista)):
    total+=lista[i] #soma todos os valores da lista

print(f'{total}')