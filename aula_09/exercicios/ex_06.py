"""6 - A partir do dicionário de nomes e idades de pessoas a seguir, faça um programa que
 imprima em ordem a partir dos nomes das pessoas, mostre a soma das idades, a média das 
 idades e a pessoa mais velha."""

people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 2000000,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 21,
    "Jill": 32,
    "Jack": 32,
}

people_sorted = dict(sorted(people.items()))

somaIdade = 0
maiorIdade = 0

for idade in people_sorted.values():
    somaIdade += idade
    if idade > maiorIdade:
        maiorIdade = idade

mediaIdade = somaIdade / len(people_sorted)

print(f"A soma de todas as idade: {somaIdade}")
print(f"A média das idades: {mediaIdade}")
print(f"A maior idade: {maiorIdade}")

