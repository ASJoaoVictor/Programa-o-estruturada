"""Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. 
Imprima uma mensagem informando o resultado."""

num = int(input("Digite um número: "))

if(num%2 == 0):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")