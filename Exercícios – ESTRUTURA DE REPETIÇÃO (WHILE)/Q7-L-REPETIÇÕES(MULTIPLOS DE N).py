n= int(input('DIGITE O VALOR DE N: '))
l_inf= int(input('DIGITE O LIMITE INFERIOR: '))
l_sup= int(input('DIGITE O LIMITE SUPERIOR: '))


lista=[0]
resultado=[]

while l_inf<=l_sup:
    lista.append(l_inf)
    l_inf+=1

for i in range (len(lista)):
    resto= i % n
    if resto==0 and i>0:
        resultado.append(i)

print(f'{resultado}')