#Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.

#Como o usuário poderia digitar mais de uma linha, sem utilizar um biblioteca

frase = input("Frase: ")

quat_carac = len(frase.replace(" ", ""))
quat_palatras = len(frase.split())

print(f"Quantidade de caracteres: {quat_carac} \nQuantidade de palavras: {quat_palatras}")
