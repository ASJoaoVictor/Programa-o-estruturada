#Escreva um programa que peça ao usuário para digitar seu nome completo e, em seguida, imprima apenas o sobrenome.

nome_completo = input("Nome completo: ")

nomes = nome_completo.split()

sobrenome = nomes[-1]

print(f"sobrenome: {sobrenome}")