#Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: 
# A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

nota = int(input("Digite a nota: "))

if(nota < 60):
    print("Conceito F")
elif(nota < 70):
    print("Conceito D")
elif(nota < 80):
    print("Conceito C")
elif(nota < 90):
    print("Conceito B")
else: 
    print("Conceito A")