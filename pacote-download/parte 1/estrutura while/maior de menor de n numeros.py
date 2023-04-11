media = cont = num = soma=maior= menor=0
resposta = 'S'
while resposta in 'sS':
    num = int(input('Digite um número inteiro:'))
    cont=cont+1
    soma=soma+num
    if cont == 1:
        maior=menor=num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor=num
    resposta=str(input('Quer continuar[S/N]?')).strip().upper()[0]
media=soma/cont
print('A media dos {} números é igual a {:.2f}'.format(cont,media))
print('O maior número foi {} e o menor {}'.format(maior,menor))
