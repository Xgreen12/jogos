print('####### jogo do dado ###########')

nome = str(input('\nQual é o seu nome? '))

jogador = str(input('\nVocê quer jogar o dado? '))

if jogador == 'sim':
    print('\nOtimo então vamos iniciar jogando o dado.')
else:
    exit()

# O objetivo do jogo é fazer mais pontos com duas tentativas ao jogar o dado,
# se obtiver pontos acima de 10 sairá como vencedor.

from random import randint
from time import sleep

dado1 = randint(1, 6)

print('\nO primeiro dado o resultado foi {}'.format(dado1))

print('\nJogando mais uma vez')

print('Aguarde...')

sleep(5)

dado2 = randint(1, 6)

print('\ne na segunda jogada saiu o {}'.format(dado2))

s = dado1 + dado2

print('\nE o resultado final foi {}'.format(dado1+dado2))

if s >= 10:
    print('\nParabéns você venceu!')
else:
    print('\nFim de jogo você perdeu!')
print('Mais sorte da proxima vez.')
