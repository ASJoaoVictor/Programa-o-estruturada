#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.

frase = input("Frase: ")

if(frase[-1] == "."):
    print("termina com ponto final")
else:
    print("Não termina com ponto final")
