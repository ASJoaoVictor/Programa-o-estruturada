"""Q16: Escreva um programa que imprime na tela os n primeiros números perfeitos. 
Um número perfeito é aquele que é igual à soma dos seus divisores. Por exemplo, 6 = 1 + 2 + 3."""

n = int(input("Digite quantos números perfeitos quer ver: "))
cont = 0
numero = 2
while(cont < n):
    soma = 0
    for i in range(1, numero//2+1):
        if(numero % i == 0):
            soma += i
    if(soma == numero):
        cont += 1
        print(numero)
    numero += 1