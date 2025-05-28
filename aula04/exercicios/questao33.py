#Escreva um programa que solicite ao usuário para digitar seu nome e, em seguida, imprima as iniciais do nome em letras maiúsculas.

nome_completo = input("Digite seu nome: ")

nome_separado = nome_completo.split()

for nome in nome_separado:
    print(f"{nome[0].upper()}.", end="")