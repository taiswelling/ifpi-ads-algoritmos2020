n=int(input('Quantos habitantes deseja analisar? '))
a=0
lista1=[]
lista2=[]

while a<n:
    a+=1

    print('______________________________________')
    print(f'PREENCHA A FICHA do {a}º HABITANTE')
    print('______________________________________')

    salario=int(input(' Qual seu salário?  '))
    lista1.append(salario)
    dependentes=int(input(' Quantos filhos possui? '))
    lista2.append(dependentes)
    print('                                     ')
    print('                                     ')

total_salário=0
porcentagem=0

for i in lista1:
    total_salário+=i
    if i>1000:
        porcentagem+=1
    else:
        None
média_salário = (total_salário)/n

porcento=(porcentagem*100)/n

total_filhos=0
for i in lista2:
    total_filhos+=i

média_filhos = (total_filhos)/n

print(f"A média salarial é de {média_salário} reais por habitante;")
print(f'A média de filhos é de {média_filhos} filho(s) por habitante; ')
print(f'A porcentagem de habitantes que recebe acima de R$ 1000.00 é de {porcento}%')