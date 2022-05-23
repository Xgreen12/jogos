"""
1° faça um programa que leia a tabuada

print('\t ------Tabuada------ ')

numero = int(input('Informe o numero para ver a tabuada: '))

print('\t A tabuada de', numero, ':')

for i in range(1, 10):
    print(numero, 'x', i, '=', (numero * i))
"""


"""
2° Faça um algoritmo em linguagem Python que receba duas
notas e calcule a média aritmética e mostre o resultado.
print('\t-------Calcúlo de média aritmética------ ')


nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

print('Média Aritmética' '=', media)
"""

"""
3° Fazer um algoritimo que ao receber o sálario
 atual de um funcionário, calcule o valor do novo sálario
reajustado de acordo a tabela abaixo.
salário atual:                 Reajuste:
abaixo de R$500,00                15%
de R$500,00 até R$1000,00         10%
Acima de R$1000,00                5%

salario_atual = float(input('Informe o salário atual: '))

if (salario_atual<500):
    salario_novo=salario_atual+(salario_atual*0.15)
    print('Salário com reajuste' '=', salario_novo)


if((salario_atual>=500) and (salario_atual <=1000)):
    salario_novo=salario_atual+(salario_atual*0.10)
    print('Salário com reajuste' '=', salario_novo)


if(salario_atual>1000):
    salario_novo=salario_atual+(salario_atual*0.05)
    print('Salário com reajuste' '=', salario_novo)
"""


"""
4°  Escreva um programa que mostre todos os números entre 5 e 100
que são divisíveis por 7, mas não são múltiplos de 5. Os números 
obtidos devem ser impressos em sequência.

for num in range(5, 100):
    if (num % 7 == 0 and num % 5 != 0):
        print(num)
"""


"""
5° Faça um programa que receba um número digitado pelo usuário e
  calcule a soma de todos os números de 1 até ao número digitado.
   Por exemplo, se o usuário digitou o número 4, a saída deve ser
    10 (1+2+3+4=10).

soma_numeros = 0

numero = int(input('Por favor, insira um número: '))
for i in range(1, numero + 1, 1):

    soma_numeros += i

print('A soma é = ', soma_numeros)
"""


"""
6° Faça um programa que recebendo um valor inteiro,
informe se o número é positivo, negativo ou neutro.

x = int(input("Informe um número para brincar: "))

if x < 0:
        print('É um número negativo ')
elif x == 0:
        print('É um número neutro')
elif x > 0:
        print('É um número positivo')
"""


"""
 Crie um algoritmo que receba um número, conte o número
total de dígitos e mostre o resultado.
Por exemplo, se o número é 2021 , então a saída deve ser 4
"""
digitos = int(input('digite um número para contar seus dígitos: '))

contador = 0

while digitos != 0:

    digitos //= 10

    contador += 1

print('Total de dígitos = ', contador)