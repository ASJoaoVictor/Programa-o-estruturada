#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python".

frase = input("Frase: ")

if(frase.find("python") != -1):
    print("Tem a palavra python")
else:
    print("Não tem a palavra python")