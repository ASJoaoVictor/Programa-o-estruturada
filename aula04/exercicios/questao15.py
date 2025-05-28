#Escreva um programa que solicite ao usuário um nome e um número inteiro e imprima uma mensagem formatada repetindo o nome o número de vezes especificado. 
# Por exemplo, se o nome for "João" e o número for 3, o programa deve imprimir "JoãoJoãoJoão".

nome = input("Nome: ")
num = int(input("Número: "))

for i in range(0, num):
    print(f"{nome}", end="")