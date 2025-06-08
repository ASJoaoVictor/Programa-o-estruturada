import random

secreto = random.randint(0, 10)
acertou = False
tentativas = 5

while(not acertou):
    numero = int(input("Digite um número(0 a 100): "))
    tentativas -= 1
    if(tentativas == 0):
        print("Antigiu o número máximo de tentativas")
        print(f"O número secreto é {secreto}")
        break
    elif(numero == secreto):
        print("Acertou o número, Parabéns")
        acertou = True
        break;
    elif(secreto > numero):
        print("O número é maior")
    else:
        print("O número é menor")
    print(f"Faltam {tentativas} tentativas")
    

