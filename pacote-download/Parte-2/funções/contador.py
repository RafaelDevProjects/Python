from time import sleep


def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p=1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    print('-=' * 20)
    if i < f:
        cont=i
        while cont <=f:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont += p
        print('FIM!')
        print('-=' * 20)
    else:
        cont= i
        while cont >= f:
            print(f'{cont} ',end= '')
            sleep(0.3)
            cont -= p
        print('FIM!')
        print('-=' * 20)



contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar o contador')
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Pulos: '))
contador(i, f, p)


