matriz = [[0, 0, 0],[0, 0, 0],[0 , 0, 0]]
spar=mai=scol=0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]= int(input(f'Digite um valor para a posição {[l ,c]}:'))
print('-='*30)
for l in range (0,3):
    for  c in range (0,3):
        print(f'[{matriz [l] [c]:^5}]',end= '')
        if matriz[l][c] % 2 == 0:
            spar+= matriz[c][l]
    print()
print('-='*30)

print(f'A soma de todos os pares = {spar}')
for l in range (0, 3):
    scol+= matriz[l][2]
print(f'A soma dos valores da terceira coluna = {scol}')
for c in range (0, 2):
    if c == 0:
        maior = matriz [1] [c]
    elif matriz [1] [c] > maior:
        maior= matriz [1] [c]
print(f'O maior valor da linha 2 = {maior}')
