"""Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. 
Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados. Imprima os valores em um arquivo."""

valor1 = bool(int(input("Insira qualquer coisa para True: ")))
valor2 = bool(input("Deixe em branco para False: ")))

print(f"{valor1} and {valor2} = {valor1 and valor2} \n{valor1} or {valor2} = {valor1 or valor2} \nnot {valor1} = {not valor1} | not {valor2} = {not valor2}")

with open('parte1/lab-aula3.md/questao09.txt','w') as f:
    print(f"{valor1} and {valor2} = {valor1 and valor2} \n{valor1} or {valor2} = {valor1 or valor2} \nnot {valor1} = {not valor1} | not {valor2} = {not valor2}",file=f)