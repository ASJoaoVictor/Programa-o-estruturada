"""Escreva um programa que solicite ao usuário dois números e verifique se o primeiro número é maior que o segundo. 
Imprima uma mensagem informando o resultado da comparação. Imprima os valores em um arquivo."""

num1 = float(input("Primeiro numero: ")) 
num2 = float(input("Segundo numero: "))

if(num1 > num2):
    msg = "O primeiro número é maior"
else:
    msg = "O segundo número é maior"

print(msg)

with open('parte1/lab-aula3.md/questao11.txt','w') as f:
    print(msg,file=f)