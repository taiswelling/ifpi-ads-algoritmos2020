'''6. Leia o  turno em que um aluno estuda, sendo M para matutino,
V para Vespertino ou N para Noturno e escreva a mensagem
"Bom Dia!","Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno=str(input('Em que turno você estuda?\nDigite "M" para o turno manhã;\nDigite "T" para o turno da tarde;\nDigite "N" para o turno manhã\n'))
nome=str(input('Qual seu nome?\n'))

if turno=='m' or turno=='M':
    print(f'Bom dia, {nome}!')
    
elif turno=='t' or turno=='T':
    print(f'Boa tarde, {nome}!')

elif turno=='n' or turno=='N':
    print(f'Boa noite, {nome}!')

else:
    print('Erro! Observe o valor digitado e tente novamente!\n(OBS: Os valores válidos para o turno são apenas "M,T ou N")' )