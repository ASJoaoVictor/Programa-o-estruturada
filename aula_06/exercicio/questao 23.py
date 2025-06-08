"""Q23: Numa lanchonete, uma pessoa pode comprar Nuggets apenas em pacotes contendo 6, 9 ou 20 pedaços. 
Escreva um programa em Python que lê um valor inteiro num e que imprima True se é possível comprar num Nuggets nessa lanchonete, ou Falso, caso contrário. 
Por exemplo, se num = 44, o programa deve retornar True (seria um pacote de 6, dois de 9 e 1 um de 20, por exemplo). Mas se num = 34, o programa deve retornar False"""

num = int(input("Digite o número de nuggets: "))

pacotes20 = 0
pacotes9 = 0
pacotes6 = 0

retorno = False

while(num - 20 >= 0 or num - 20 >= 9):
    pacotes20 += 1
    num -= 20

while(num - 9 >= 0):
    pacotes9 += 1
    num -= 9

while(num - 6 >= 0):
    pacotes6 += 1
    num -= 6

if(num == 0):
    print(f"seria {pacotes6} pacote de 6, {pacotes9} de 9 e {pacotes20} de 20")
    retorno = True

print(retorno)