l_inf= int(input('DIGITE O LIMITE INFERIOR: '))
l_sup= int(input('DIGITE O LIMITE SUPERIOR: '))


lista=[0]
resultado=[]

while l_inf<=l_sup:
    lista.append(l_inf)
    l_inf+=1

for i in range (len(lista)):
    resto= i % 2
    if resto!=0 and i<=l_sup:
        resultado.append(i)

print(f'{resultado}')