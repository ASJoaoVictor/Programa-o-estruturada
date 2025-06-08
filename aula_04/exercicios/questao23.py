#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas.

frase = input("Frase: ")
msg = ""
for i in frase:
    if(i != i.upper()):
        msg = "Nem todas as palavras estão com letras maiuculas"
        break
    else:
        msg = "Todas estão em letras maisculas"
print(msg)