from time import sleep
def lin():
    print('-='*20)
def maior(*num):

    print('Analisando os valores passados...')
    cont=0
    maior=0
    menor=0
    for c in num:
        print(f'{c} ',end='')
        sleep(0.3)
        cont+=1
        if c == 0:
            maior=menor=c
        else:
            if c > maior:
                maior=c
            if c < menor:
                menor=c
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    lin()


lin()
maior(1, 2, 2, 3)
maior(9,0)
maior(12223,1212121,1,5,68,23)
maior()
maior(-1)