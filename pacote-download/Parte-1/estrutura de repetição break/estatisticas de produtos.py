print('-' * 30)
print('    MERCADINHO DO BAIRRO')
print('-' * 30)
total=tot1000=menor=cont=0
barato=' '
while True:
    produto=str(input('Nome do produto:'))
    preço=int(input('Preço: R$'))
    cont+=1
    if cont==1 or preço < menor:
        menor=preço
        barato=produto
    total += preço
    if preço >= 1000:
        tot1000+=1
    resp= ' '
    while resp not in 'SN':
        resp=str(input('Quer continuaR [S/N]?')).upper().strip()[0]
        print('-' * 30)
    if resp == 'N':
        break

print(f'''O total da compra foi de R$ {total:.2f} 
Produtos que custaram mais de R$ 1000.00: {tot1000}
Produto mais barato foi {barato} e custa R$ {menor:.2f}
''')