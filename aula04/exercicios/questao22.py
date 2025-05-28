#Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas vezes uma determinada letra aparece na frase.

frase = input("Frase: ")
count:int = 0

tipo_a = ["a", "á", "à", "â", "ã"]

for i in frase:
    for j in tipo_a:
        if(i == j):
            count += 1
            break
print(f"A frase tem {count} \"a\"")