n = int(input("QUANTOS PESOS DESEJA COMPARAR? "))
i=1
lista=[]


while i<=n:
    n1=float(input(f'Qual o valor do {i}º animal em kg? '))
    lista.append(n1)
    i+=1

maior= max(lista)
menor=min(lista)

print('**************************************')
print(f'*  O BOI MAIS GORDO PESA: {maior} kgs  ')
print(f'*  O BOI MAIS MAGRO PESA: {menor} kgs  ')
print('**************************************')
