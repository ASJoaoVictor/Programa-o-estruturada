#Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

maior:int

if(num1 > num2 and num1 > num3):
    maior = num1
elif(num2 > num1 and num2 > num3):
    maior = num2
else:
    maior = num3
print(f"O maior é {maior}")