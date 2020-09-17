n= int(input("quantos votos deseja contar? "))

votos=0
soma_de_cada_candidato=[]
voto1=0
voto2=0
voto3=0
nulo=0
branco=0

print('DIGITE:\n 1 - Para Candidato 1 \n 2 - Para Candidato 2 \n 3 - Para Candidato 3 \n 9 - Para Nulo \n 0 - Para Branco ')
print('                                                           ')


while votos<n:
    votos+=1
    candidato=int(input(f'{votos}º VOTO: '))
    if candidato==1:
        voto1+=1
    if candidato==2:
        voto2+=1
    if candidato==3:
        voto3+=1
    if candidato==9:
        nulo+=1
    if candidato==0:
        branco+=1

soma_de_cada_candidato.append(voto1)
soma_de_cada_candidato.append(voto2)
soma_de_cada_candidato.append(voto3)

vencedor=max(soma_de_cada_candidato)

if vencedor== voto1:
    ganhou='Candidato 1'

if vencedor== voto2:
    ganhou='Candidato 2'

if vencedor== voto3:
    ganhou='Candidato 3'

print(f'Candidato 1 teve {voto1} votos')
print('                                                           ')
print(f'Candidato 2 teve {voto2} votos')
print('                                                           ')
print(f'Candidato 3 teve {voto3} votos')
print('                                                           ')
print(f'Total de votos nulos:{nulo} votos')
print('                                                           ')
print(f'Total de votos em branco: {branco} votos')
print('                                                           ')
print(f'O vencedor é {ganhou} ;')


