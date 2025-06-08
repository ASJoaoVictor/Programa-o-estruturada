#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".

palavra = input("Digite um paravra: ")

if(not (palavra == palavra[::-1])):
    print("não", end=" ")

print("é um palíndromo")
