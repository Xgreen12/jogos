import random
import math

print('\n------- Game de advinhação -------  ')
""" O objetivo do jogo será escolher um número menor e um maior dentre eles será
 sorteado um número que o jogador tentará adivinhar, qual número foi sorteado.
"""

menor = int(input("\nEscolha um número de baixo valor: "))

maior = int(input("\nAgora escolha um número com valor alto: "))

print('\nTente adivinhar qual número foi sorteado entre o valor menor e o maior que você escolheu!')

x = random.randint(menor, maior)
print("\n\tVocê tem apenas ", round(math.log(maior - menor + 1, 2)), " chances para tentar adivinhar qual foi o número sorteado!\n")
contar = 0

while contar < math.log(maior - menor + 1, 2):
    contar += 1

    adivinhar = int(input("\nO número sorteado foi? "))

    if x == adivinhar:
        print("Parabéns você fez isso em ", contar, " tentativa(s). ✌ ")

        break
    elif x > adivinhar:
        print("O seu palpite foi muito baixo!")
        print('Tente novamente!')
    elif x < adivinhar:
        print("O seu palpite foi muito alto!")
        print('\nTente mais uma vez!')

if contar >= math.log(maior - menor + 1, 2):
    print("\nO número sorteado foi %d" % x)
    print("\tMais sorte da próxima vez! ")
