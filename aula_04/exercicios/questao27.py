#Escreva um programa que solicite ao usuário para digitar seu nome em letras minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula.

nome = input("Nome em letras minúsculas: ")

print(f"{nome[0].upper()}{nome[1:].lower()}")