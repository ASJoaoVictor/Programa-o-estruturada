#Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. 
# Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

lado1 = int(input("comprimero do 1° lado: "))
lado2 = int(input("comprimero do 2° lado: "))
lado3 = int(input("comprimero do 3° lado: "))

if(lado1 == lado2 == lado3):
    print("equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("Isósceles")
else:
    print("Escaleno")