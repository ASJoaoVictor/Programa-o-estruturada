#Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem formatada no seguinte formato: "Olá, {nome}! Você tem {idade} anos."

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos.")