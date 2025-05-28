#Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").

email = input("E-mail: ")

posicao = email.find("@")
nome = email[0:posicao]
dominio = email[posicao+1:]

print(f"Nome: {nome} \nDominio: {dominio}")