"""Exercício 12: Dada a lista de frutas e a lista de cores abaixo, utilize a função zip() e um loop "for" para imprimir cada fruta com sua respectiva cor."""

frutas = ['maçã', 'banana', 'laranja', 'uva']
cores = ['vermelho', 'amarelo', 'laranja', 'roxa']

for fruta, cor in zip(frutas, cores):
    print(f"A {fruta} é da cor {cor}")