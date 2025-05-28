"""Exercício 8: Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. 
O programa deve informar se o palpite é muito alto, muito baixo ou correto. 
Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while"."""

from random import randint

numSecreto = randint(1, 100)
acertou = False

while(not acertou):
    numero = int(input("Digite um número(1 a 100): "))

    if(numero == numSecreto):
        print("Parabéns, você acertou o número secreto")
        acertou = True
    elif(numero > numSecreto):
        print("Palpite alto, tente um número menor")
    else:
        print("Palpite baixo, tente um número maior") 