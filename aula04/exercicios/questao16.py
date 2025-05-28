#Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome.

nome_comleto = input("Digite seu nome completo: ")

nome_separado = nome_comleto.split()

print(f"primeiro nome: {nome_separado[0]}")