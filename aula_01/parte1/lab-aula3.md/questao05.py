"""Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área e o perímetro desse círculo. 
Imprima os resultados formatados.Imprima os valores em um arquivo."""

from math import pi

def area(raio):
    return pi * (raio**2)

def perimetro(raio):
    return 2 * pi * raio

raio = float(input("Digite o raio: "))

print(f"area: {area(raio):.2f}\nperimetro: {perimetro(raio):.2f}")

with open('parte1/lab-aula3.md/questao05.txt','w') as f:
    print(f"area: {area(raio):.2f}\nperimetro: {perimetro(raio):.2f}",file=f)