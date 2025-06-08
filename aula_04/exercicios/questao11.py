#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos.
#  Por exemplo: "O total de segundos é {total_segundos}."

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_segundos = horas*3600 + minutos*60 + segundos

print(f"O total de segundos é {total_segundos}.")