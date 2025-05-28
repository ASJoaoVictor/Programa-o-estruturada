"""Q25: Generalize o exercício anterior, de forma que ele calcule e mostre na tela os quadrados de todos os números naturais menores que 1000, 
usando o método da soma de ímpares."""

def calcQuadrado(n: int):
    i = 1
    impar = 1
    quadrado = 0
    while(i <= n):
        quadrado += impar
        impar += 2
        i+=1
    return quadrado

for n in range(1, 1000):
    print(f"{n}^2 = {calcQuadrado(n)}")