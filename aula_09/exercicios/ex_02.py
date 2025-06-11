"""2 - Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 
lançamentos.

Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
Faça uma iteração na lista para verificar quantos destes números são iguais à 6"""

from random import randint

quantLancamentos = int(input("Digite a quantidade de lançametos: "))
lancamentos = []

def verificar(lista: list, num:int) -> int:
    count = 0
    for i in lista:
        if i == num:
            count += 1
    return count

for i in range(0, quantLancamentos):
    lancamentos.append(randint(1, 6))


print(f"A frequência esperada é {(1/6)*quantLancamentos}")
print(f"1 => {verificar(lancamentos, 1)}")
print(f"2 => {verificar(lancamentos, 2)}")
print(f"3 => {verificar(lancamentos, 3)}")
print(f"4 => {verificar(lancamentos, 4)}")
print(f"5 => {verificar(lancamentos, 5)}")
print(f"6 => {verificar(lancamentos, 6)}")

