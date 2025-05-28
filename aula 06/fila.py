from time import sleep

posicao_na_fila = 10


while(posicao_na_fila > 0):
    print("Esperando...")
    print("Posicao da fila: ", posicao_na_fila)
    posicao_na_fila -= 1# posicao_na_fila = posicao_na_fila - 1
    sleep(4)
