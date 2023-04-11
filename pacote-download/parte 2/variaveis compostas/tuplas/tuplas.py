lanche= ('hamburguer','suco','pizza','pudim')
print(lanche)
print(lanche[0])
print(lanche[0:2])
print(lanche[-1])
print(lanche[2:])
print(f'na lista tem {len(lanche)} comidas') #len conta quantos objetos tem na tupla
for comida in lanche: #repete todas comida em todos os prints, forma o laço
    print(f'Eu vou comer {comida}')
for cont in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!!')
for pos,comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print(sorted(lanche)) #deixa em ordem

a=(1 , 3 , 4 , 5)
b=( 5 , 1 , 3 , 0)
c= a + b # soma as duas tuplas
print(c)
print(c.count(3)) #.count mostra quantas vezes o numero () foi usado
print(c.index(3)) #.index mostra aonde esta certo numero () em uma certa posição começando com 0]
del c #deleta a variavel