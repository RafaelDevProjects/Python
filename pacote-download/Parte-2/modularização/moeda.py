def dobro(preço=0, form=False):
    res= preço * 2
    return res if form is False else moeda(res)


def metade(preço=0, form=False):
    res= preço / 2
    return res if form is False else moeda(res)


def aumentar(preço=0, y=0, form=False):
    res = preço + (preço * y / 100)
    return res if form is False else moeda(res)


def diminuir(preço=0, y=0, form=False):
    res = preço - (preço * y / 100)
    return res if form is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def escreva(msg):
    tam=len(msg)+15
    print('-' * tam)
    print(f'{msg}'.center(tam))
    print('-'* tam)


def resumo(p=0, taxaa=0, taxad=0):
    escreva('RESUMO DO VALOR')
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True):}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'20% de aumento: \t{aumentar(p,taxaa,True)}')
    print(f'10% de redução: \t{diminuir(p,taxad,True)} ')
    print('-'*30)


