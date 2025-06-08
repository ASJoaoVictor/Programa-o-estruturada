#Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). 
# Em seguida, imprima a frase formatada.

frase = input("Digite uma frase: ")

frase_sem_vogais = frase.replace("a", "*")
frase_sem_vogais = frase_sem_vogais.replace("e", "*")
frase_sem_vogais = frase_sem_vogais.replace("i", "*")
frase_sem_vogais = frase_sem_vogais.replace("o", "*")
frase_sem_vogais = frase_sem_vogais.replace("u", "*")


print(frase_sem_vogais)