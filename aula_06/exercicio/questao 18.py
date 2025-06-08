"""Q18: Elabore um programa que leia n valores e mostre a soma de seus quadrados.."""

quantNum = int(input("Quantos números deseja digitar: "))
soma = 0
for i in range(1, quantNum+1):
    numero = int(input(f"Digite o {i}° número: "))

    soma += numero**2

print(f"A soma dos quadrados é {soma}")