"""Q17: Um número inteiro é considerado triangular se este for o produto de 3 números inteiros consecutivos, como, por exemplo, 120 = 4 x 5 x 6. 
Elabore um programa que, após ler um número n do teclado, verifique se n é triangular."""

n = int(input("Digite um número: "))

produto = 0
i = 1

while(produto < n):
    produto = i * (i+1) * (i+2)
    if(produto == n):
        print(f"O número {n} é considerado triangular, {n} = {i} * {i+1} * {i+2}")
        break
    elif(produto > n):
        print(f"{n} não é triangular")
    i += 1