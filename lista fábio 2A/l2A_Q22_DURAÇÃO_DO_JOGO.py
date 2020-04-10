'''Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
seguinte.'''

h_inicio = int(input('A que horas iniciou o jogo?\n'))
m_inicio =int(input('E quantos minutos?\n'))
h_fim =int(input('A que horas finalizou o jogo?\n'))
m_fim = int(input('E quantos minutos?\n'))

horas =  h_fim-h_inicio
minutos =  m_fim-m_inicio
hora1 = 24-horas


if h_fim < h_inicio:
    print(f'O jogo teve {hora1}horas e {minutos} minutos de duração;')

elif h_fim > h_inicio:
    
    print(f'O jogo teve {horas}horas e {minutos} minutos de duração;')


  #incorreta
