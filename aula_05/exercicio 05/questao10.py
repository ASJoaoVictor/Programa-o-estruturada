#Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.

ano = int(input("Digite o ano: "))

if(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
    print("Ano bissesto")
else:
    print("Não é bissesto")