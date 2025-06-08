"""Exercício 2: Escreva um programa que peça ao usuário para digitar um número e, em seguida, imprima a tabuada desse número (de 1 a 10) utilizando um loop "for"."""

num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{i} x {num} = {i*num}")