#Escreva um programa que peça ao usuário para digitar uma frase e imprima o número de caracteres na frase.

frase = input("Frase: ")
frase_sem_espaco = frase.replace(" ", "")

print(f"a frase tem {len(frase_sem_espaco)}")