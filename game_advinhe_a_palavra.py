"""
##### jogo de avivinhar as palavras ######

- O objetivo do jogo é você tentar adivinhar qual palavra foi sorteada.Você tera como chance a primeira letra já exposta
para ficar mais facil de advinhar.
"""
import random

nome = input('\nDigite seu nome: ')

print('\nBoa sorte!', nome)


palavras = ['carro', 'bicicleta', 'arvore', 'televisão','dinheiro', 'paisagem', 'gato' 
                        'elefante', 'rio', 'humano']


palavra = random.choice(palavras)

print('\nQual é a palavra? ')


palpites = " "

total = 12


while total > 0:


    falha = 0

    for char in palavra:

        if char in palpites:
           print(char)
        else:
             print('_')
             falha += 1

    if falha == 0:
        print('Parabéns você venceu.')

        print('A palavra é', palavra)
        break


    adivinhe = input('Adivinhe a palavra: ')

    palpites += adivinhe


    if adivinhe not in palavras:
     total -= 1

    print('\nNão tem essa letra, tente outra! ')

    print('\nVocê tem', + total, 'mais palpites')

    if total == 0:
            print('Fim de jogo, você não tem mais chances.')
