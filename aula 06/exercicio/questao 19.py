"""Q19: Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y, além do resto da divisão. 
Não é permitido usar as operações de divisão e resto de divisão do Python (use apenas soma e subtração)"""

x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
resto = 0
resultado = 0

while(resultado * y < x):
    if (resultado+1) * y > x:
        resto = x - (resultado * y)
        break
    resultado += 1

print(f"{x} divido por {y} é {resultado} e o resto é {resto}")

