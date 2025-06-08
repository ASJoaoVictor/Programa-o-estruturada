"""Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for"."""

frase = input("Digite uma frase: ").lower()
quantVogais = 0

for letra in frase:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        quantVogais += 1
print(f"Tem {quantVogais} vogais") 