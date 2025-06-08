#Escreva um programa que substitua todas as ocorrências de uma determinada palavra em uma frase por outra palavra fornecida pelo usuário.

frase = "chuva, chuva e mais chuva. A chuva não parava, e todos falavam da chuva."
print(frase)

palavra = input("Digite um palavra para substituir chuva: ")

print(frase.replace("chuva", palavra))
