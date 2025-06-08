#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. 
#Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."

nome_completo = input("Nome completo: ")

nomes = nome_completo.upper().split()

for i in nomes:
    print(f"{i[0]}.", end="")
print()