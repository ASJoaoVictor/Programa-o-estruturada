"""Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados. Imprima os valores em um arquivo.

Instruções:

Solicite ao usuário o primeiro número inteiro e armazene-o em uma variável chamada numero1. Solicite ao usuário o segundo número inteiro e armazene-o em uma variável chamada numero2. 
Troque os valores das variáveis numero1 e numero2 utilizando atribuição múltipla. 
Imprima os valores atualizados das variáveis utilizando a função print()."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"Valores antes da troca: numero1 = {num1}, numero2 = {num2}")
with open("parte1/lab-aula3.md/questao13.txt", "w") as f:
    print(f"Valores antes da troca: numero1 = {num1}, numero2 = {num2}", file=f)

num1, num2 = num2, num1

print(f"Valores depois da troca: numero1 = {num1}, numero2 = {num2}")

with open("parte1/lab-aula3.md/questao13.txt", "a") as f:
    print(f"Valores depois da troca: numero1 = {num1}, numero2 = {num2}", file=f)
