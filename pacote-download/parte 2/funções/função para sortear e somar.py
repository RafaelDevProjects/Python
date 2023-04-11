from random import randint


def sortear(lista):
    for c in range (0,5):
        numeros.append(randint(1,10))
    print(f'Os valores sorteados na lista foram:',end=' ')
    for v in numeros:
        print(f'{v}',end=' ')
    print(f'SORTEADO!')


def somapar(lista):
    soma=0
    for v in lista:
        if v % 2 == 0:
            soma+=v
    print(f'Somando os valores pares da lista {lista} temos {soma}')

numeros=[]
sortear(numeros)
somapar(numeros)
