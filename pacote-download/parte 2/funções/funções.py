
'''a=4 #codigos quase iguais
b=5
s= a+b
print(s)

a=8
b=9   #codigos quase iguais
s= a+b
print(s)

a=2
b=1  #codigos quase iguais
s=a+b
print(s)'''
def lin():
    print('-'*30)
def soma(a,b): #cria um comando [soma]
    print(f'A soma de {a} + {b}')
    s=a+b
    print(f'A soma dos dois é igual a {s}')

#programa principal
soma(4,5)
soma(8,9)
soma(2,1)
lin()


def contador(*num):  #define um contador. O [*num] quer dizer que vc pode colocar quantos numeros quiser no contador
    for valor in num:
        print(f'{valor}',end=' ')
    print('FIM!')#defi


contador(1, 2, 3, 4)
contador(5, 3, 6)
contador(0, 2, 8, 1, 'oi', 0, 2, 1)


def dobra(lista): #função de dobra de valores dentro de um lista
    pos=0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1

lin()
valores= [1, 6, 4 , 8]
dobra(valores)
print(valores)


