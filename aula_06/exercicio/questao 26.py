"""Q26: Faça um programa que simula uma calculadora que aceita as seguintes operações: soma, subtração, divisão e multiplicação. 
O programa inicia pedindo para o usuário escolher uma opção do menu

Somar
Subtrair
Dividir
Multiplicar
Sair

Ao escolher a opção, o programa solicita os dois números a serem operados (exceto se a opção escolhida for a 5), 
efetua a operação, mostra o resultado na tela e volta para o menu para que o usuário escolha outra opção."""

opcao = -1


while(opcao != 5):
    print("1 - Somar \n2 - Subtrair \n3 - Dividir \n4 - Multiplicar \n5 - Sair")
    
    opcao = int(input("Escolha uma das opções: "))

    if(opcao != 5):
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
    
    match(opcao):
        case 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        case 3:
            print(f"{num1} / {num2} = {num1 / num2}")
        case 4:
            print(f"{num1} * {num2} = {num1 * num2}")
        case 5:
            break
