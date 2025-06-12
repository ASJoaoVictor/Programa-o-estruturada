"""Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, 
em seu programa o usuário deverá inserir uma sequência de valores que representam a 
temperatura em graus Fahrenheit, seu programa deve receber esses valores e armazenar em uma 
lista até que o valor inserido pelo usuário seja um valor em branco (uma string vazia). 
Converta todos os valores presentes na lista para graus Celsius usando a função map e imprima 
na tela em uma formatação amigável ao usuário.

Utilize o while e no bloco de repetição leia dados de temperatura do usuário
Acrescente os dados na lista
Crie uma função para converter temperatura de Farenheint para Celcius
Use a função map com a função e a lista
Imprima todas os valores da nova lista"""

temperaturasF = []

def farenheintForCelsius(temperatura):
    celsius = (temperatura - 32) * 5/9
    return round(celsius, 2)

while True:
    temperatura = input("DIgite o valor da temperatura: ")

    if temperatura == "":
        break

    temperaturasF.append(float(temperatura))

temperaturasC = list(map(farenheintForCelsius, temperaturasF))

print(temperaturasC)