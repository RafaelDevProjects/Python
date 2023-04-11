print('='*10,'MERCADINHO','='*10)
preço=float(input('Preço da compra: R$'))
print('''ESCOLHA A FORMA DE PAGAMENTO':
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
n=int(input('forma de pagamento:'))
if n == 1:
    pago= preço - (preço * 10 / 100)
elif n == 2:
    pago= preço - (preço * 5 / 100)
elif n == 3:
    pago= preço
    parcela= preço/2
    print('Sua compra sera parcelada em 2x de R${}'.format(parcela))

if n == 4:
    parcelas=int(input('Numero de parcelas:'))
    pago = preço + (preço * 20 / 100)
    parcelamento= pago/parcelas
    print('Sua compra sera parcelada em {}X de R${} com JUROS'.format(parcelas,parcelamento))


print('O valor da compra no final é de R${}'.format(pago),end='')


