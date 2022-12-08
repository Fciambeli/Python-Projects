from random import randint
from time import sleep
itens =('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
\033[37m[0] PEDRA\033[m
[1] PAPEL
\033[35m[2] TESOURA\033[m''')
jogador = int(input('Qual é a sua jogada?'))
print('\033[33mJO\033[m')
sleep(1)
print('\033[33mKEN\033[m')
sleep(1)
print('\033[33mPÔ\033[m!!!')
print('-=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0: ##PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[34mJOGADOR VENCE\033[m')
    elif jogador ==2:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: ##PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[34mJOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: ##TESOURA
    if jogador == 0:
        print('\033[34mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
