'''Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.'''

print("Para acesso ao sistema,você necessita de uma senha;")

senha = int(input('Digite uma senha de 4 dígitos:\n'))

if senha == 1234:
    print('_________________')
    print('Acesso liberado!')
    print('_________________')

else:
    print('XXXXXXXXXXXXXXXXXX')
    print('  Acesso negado!')
    print('XXXXXXXXXXXXXXXXXX')
