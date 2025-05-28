"""Escreva um programa que solicite ao usuário o seu nome e a sua idade, armazenando esses valores em variáveis. 
Em seguida, imprima uma mensagem formatada mostrando o nome e a idade do usuário. Imprima os valores em um arquivo."""

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

print(f"nome: {nome}\nidade: {idade}")

with open('parte1/lab-aula3.md/questao03.txt','w') as f:
    print(f"nome: {nome}|idade: {idade}",file=f)