#Escreva um código que capitalize a primeira letra de cada palavra em uma frase. Exemplo: "python é incrível" deve se tornar "Python É Incrível".

frase = input("Frase: ")

palavras = frase.split()

for i in palavras:
    print(f"{i[0].upper()}{i[1:]}", end=" ")
print()