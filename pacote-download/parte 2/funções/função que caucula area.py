def area(a,b):
    s=a*b
    print(f'A area do terreno de {a}m X {b}m é igual a {s} metros quadrados ')
def titulo(msg):
    print('-'*20)
    print(msg)
    print('-' * 20)


titulo('CALCULO DE ÁREA')
a = float(input('Largura (m) :'))
b = float(input('Comprimento (m) :'))
area(a,b)