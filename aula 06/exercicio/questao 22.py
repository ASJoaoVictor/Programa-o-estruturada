"""Q22: Faça um programa em Python que calcule o valor de Pi, utilizando a fórmula de Leibniz: π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 + ... 
Adicione parcelas no cálculo até que a diferença de uma interação para a seguinte seja menor do que um valor de erro aceitável x informado pelo usuário."""

piCalc = 0
alternar = True

for i in range(1, 100000, 2):
    if alternar:
        piCalc -= 1/i
    else:
        piCalc += 1/i
    alternar = not alternar

print(4*piCalc)