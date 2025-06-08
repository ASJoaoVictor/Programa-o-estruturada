#Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem crescente de comprimento das strings.

frase = input("Frase: ")


frase = frase.replace(",", "")
frase = frase.replace(".", "")
palavras = frase.split()

posMenor:int = 1000
menor:str
for i in range(0, len(palavras)):
    for j in range(i, len(palavras)):
        if(len(palavras[j]) < posMenor):
            posMenor = len(palavras[j])
            menor = palavras[j]
            palavras[j] = palavras[i]
            palavras[i] = menor
    posMenor = 1000

print("="*10)
for i in palavras:
    print(f"{i}", end=", ")
