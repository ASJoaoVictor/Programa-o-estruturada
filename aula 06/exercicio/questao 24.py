"""Q24: O quadrado de um numero natural n é dado pela soma dos n primeiros números impares consecutivos. Por exemplo, 1^2=1, 2^2=1+3, 3^2=1+3+5, 4^2=1+3+5+7, etc. 
Escreva um programa que dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto."""

n = int(input("Digite um número: "))

i = 1
impar = 1
quadrado = 0
while(i <= n):
    quadrado += impar
    impar += 2
    i+=1

print(f"1^{n}={quadrado}")