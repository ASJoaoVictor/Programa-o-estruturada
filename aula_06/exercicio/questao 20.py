"""Q20: Faça um programa que calcule o número de dias corridos entre duas datas, para vários pares de datas, considerando a possibilidade de ocorrência de anos bissextos, sendo que:

A primeira data é sempre a mais antiga
O ano é fornecido com 4 dígitos
A data fornecida com ZERO dias é o sinal para encerrar a entrada de dados"""

from math import dist

diasAnterior = 1
mesesAnterior = 0
anosAnterior = 0

diasPosterior = 1
mesesPosterior = 0
anosPosterior = 0

dias = 0

while(diasAnterior != 0 or diasPosterior != 0):
    diasAnterior = int(input("Insira o dia da sua data mais antiga: "))
    mesesAnterior = int(input("Insira o meses da sua data mais antiga: "))
    anosAnterior = int(input("Insira o ano da sua data mais antiga: "))

    diasPosterior = int(input("Insira o dia da sua data mais recente: "))
    mesesPosterior = int(input("Insira o mês da sua data mais recente: "))
    anosPosterior = int(input("Insira o ano da sua data mais recente: "))


    print(f"{dias}")


