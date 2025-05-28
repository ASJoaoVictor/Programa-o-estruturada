"""Q21: Foi realizada uma pesquisa em Niterói, com um número desconhecido de pessoas. De cada entrevistado foram colhidos os seguintes dados:

Qual o seu clube de futebol de preferência (1 – Flamengo, 2 – Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros)
Qual o seu salário
Qual a sua cidade natal (1 – Niterói, 2 – Outra)
Escreva um programa que informe:

Número de torcedores por clube
Média salarial dos torcedores de cada time
Número de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio
Número de pessoas entrevistadas"""

from random import randint

torcedorresFlamengo = 0
torcedorresVasco = 0
torcedorresFluminense = 0
torcedorresBotafogo = 0
torcedorresOutros = 0

totalSalarioFlamengo = 0
totalSalarioVasco = 0
totalSalarioFluminense = 0
totalSalarioBotafogo = 0
totalSalarioOutros = 0

pessoasNiteroi = 0


totalPessoas = randint(1, 10)

for i in range(1, totalPessoas):
    clube = int(input("Qual o seu clube de futebol de preferência (1 – Flamengo, 2 – Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros: "))
    salario = float(input("Qual o seu salário: "))

    match clube:
        case 1:
            torcedorresFlamengo += 1
            totalSalarioFlamengo += salario
        case 2:
            torcedorresVasco += 1
            totalSalarioVasco += salario
        case 3:
            torcedorresFluminense += 1
            totalSalarioFluminense += salario
        case 4:
            torcedorresBotafogo += 1
            totalSalarioBotafogo += salario
        case 5:
            torcedorresOutros += 1
            totalSalarioOutros += salario

    nasc = int(input("Qual a sua cidade natal (1 – Niterói, 2 – Outra): "))
    
    if(nasc == 1 and clube == 5):
        pessoasNiteroi += 1

print(f"""NÚMERO DE TORCEDORES POR CLUBE:
FLAMENGO: {torcedorresFlamengo}
VASCO: {torcedorresVasco}
FLUMINENSE: {torcedorresFluminense}
BOTAFOGO: {torcedorresBotafogo}
OUTROS: {torcedorresOutros}
""")

print(f"""MÉDIA SALARIAL POR CLUBE:
FLAMENGO: {totalSalarioFlamengo/torcedorresFlamengo}
VASCO: {totalSalarioVasco/torcedorresVasco}
FLUMINENSE: {totalSalarioFluminense/torcedorresFluminense}
BOTAFOGO: {totalSalarioBotafogo/torcedorresBotafogo}
OUTROS: {totalSalarioOutros/torcedorresOutros}
""")

print(f"número de pessaos nascidas em niteroi que não torce para nenhum time: {pessoasNiteroi}")

print(f"Total de pessoas entrevistadas: {totalPessoas}")
