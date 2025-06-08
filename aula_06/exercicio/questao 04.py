"""Exercício 4: Escreva um programa que utilize um loop "for" para calcular a soma de todos os números ímpares de 1 a 100."""

soma:int = 0

for i in range(1, 100, 2):
    soma += i

print(soma)