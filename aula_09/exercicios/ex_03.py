"""3- Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 
20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da 
seguinte forma: cada célulaé a soma dela mesma e das células anteriores. Imprima o vetor antes 
e depois da manipulação. Exemplo:

Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]"""

from random import randint

vetor_original = []
vetor_manipulado = []

for i in range(0, 10):
    vetor_original.append(randint(0, 20))

for i in vetor_original:
    elemento = i
    for j in vetor_manipulado:
        elemento += j
    vetor_manipulado.append(elemento)

print(vetor_original)
print(vetor_manipulado)
