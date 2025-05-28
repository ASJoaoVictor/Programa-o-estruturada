"""Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit. 
Imprima o resultado formatado."""


celsius = float(input("Temperatura em celsius: "))

fahr = (9/5)*celsius + 32

print(f"Celsius: {celsius}°C \nfahrenheit: {fahr}°F")