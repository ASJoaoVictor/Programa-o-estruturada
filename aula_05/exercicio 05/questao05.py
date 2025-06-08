#Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).

idade = int(input("Digite sua idade: "))

if(idade <= 12):
    print("Criança")
elif(idade <= 19):
    print("Adolescente")
elif(idade <= 59):
    print("Adulto")
else:
    print("Idoso")