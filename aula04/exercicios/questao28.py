#Escreva um programa que solicite ao usuário para digitar uma frase e, em seguida, divida a frase em palavras individuais e as imprima em linhas separadas.

frase = input("Frase: ")

frase_separada = frase.split()

for i in frase_separada:
    print(i)