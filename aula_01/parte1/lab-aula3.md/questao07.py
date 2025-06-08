"""Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. 
Calcule e imprima o salário anual. Imprima os valores em um arquivo."""

salarioMensal = float(input("Salário mensal: "))
meses = int(input("Meses trabalhados: "))

salarioAnual = salarioMensal * meses

print(f"Salário anual: R${salarioAnual:.2f}")

with open('parte1/lab-aula3.md/questao07.txt','w') as f:
    print(f"Salário mensal: R${salarioMensal} | meses: {meses} | salário anual: R${salarioAnual}",file=f)