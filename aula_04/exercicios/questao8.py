#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números.
#  Por exemplo: "A soma de {num1} e {num2} é {soma}."

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"A soma de {num1} e {num2} é {soma}.")
print(f"A subtração de {num1} e {num2} é {subt}.")
print(f"A multiplicação de {num1} e {num2} é {mult}.")
print(f"A divisão de {num1} e {num2} é {div}.")