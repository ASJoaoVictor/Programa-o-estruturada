#Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.

num = int(input("Digite um número: "))

if(num > 0):
    print("Número é positivo")
elif(num < 0):
    print("Número é negativo")
else:
    print("Número é zero")