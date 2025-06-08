"""1- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição 
em que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, 
o programa deve imprimir o valor -1

Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
Leia um número do teclado
Compare se este número está na lista"""

def listFind(lista: list, x) -> int:
    for i, value in enumerate(lista):
        if value == x:
            return i
    return -1


lista = []

for i in range(0, 5):
    lista.append(input(f"Digite o {i+1}° valor: "))

x = input("Valor a ser encontrado: ")

print(listFind(lista, x))