#Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas palavras existem na frase.

frase = input("Frase: ")

frase_separada = frase.split()

print(f"{len(frase_separada)} palavras")