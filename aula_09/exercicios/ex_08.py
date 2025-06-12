"""8 - Problema: Compra e Venda de Ações Você recebe uma lista prices onde prices[i] é o 
preço de uma determinada ação no dia i. Você deseja maximizar seu lucro escolhendo um dia
 para comprar uma ação e escolhendo um dia diferente no futuro para vender essa ação. 
 Retorne o lucro máximo que você pode obter com essa transação. Se não for possível obter 
 lucro algum, retorne 0.

Exemplo 1:

Entrada: prices = [7,1,5,3,6,4]

Saída: 5

Explicação: Compre no dia 2 (preço = 1) e venda no dia 5 (preço = 6), lucro = 6-1 = 5. Observe que comprar no dia 2 e vender no dia 1 não é permitido, pois você deve comprar antes de vender.

Exemplo 2:

Entrada: prices = [7,6,4,3,1]

Saída: 0

Explicação: Neste caso, nenhuma transação é realizada e o lucro máximo é 0."""

def buyDay(lista):
    menorPrice = lista[0]
    dia = 1
    for i, price in enumerate(lista, 1):
        if price < menorPrice:
            menorPrice = price
            dia = i
    
    return dia, menorPrice

def sellDay(lista, compra):
    maiorPrice = compra[1]
    dia = compra[0]

    for i, price in enumerate(lista[compra[0]:], compra[0]+1):
        if price > maiorPrice:
            maiorPrice = price
            dia = i
    return dia, maiorPrice


prices = [1,6,8,3,7]

compra = buyDay(prices)

venda = sellDay(prices, compra)

if compra[0] == venda[0]:
    print(0)
else:
    lucro = venda[1] - compra[1]
    print(lucro)



