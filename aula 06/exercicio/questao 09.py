"""Exercício 9: Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. 
Em seguida, calcule e imprima a média dos números digitados."""

negativo = False
i = 0
soma = 0
while(not negativo):
    numero = int(input("Digite um número: "))
    
    if(numero < 0):
        negativo = True
        break
    
    soma += numero
    i += 1

print(f"A média dos números digitado é {(soma/i):.2f}")