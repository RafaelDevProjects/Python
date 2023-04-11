valor=(float(input("Qual é o valor da casa? R$")))
salario=(float(input('Qual é o eu salário? R$')))
anos=(int(input('Em quantos anos ira pagar?')))
print('-=-'*20)
prestação= valor / (anos * 12)
print("Para pagar um casa de R${:.2f}, em {} anos, cada prestação sera de R${:.2f}".format(valor, anos, prestação))
if prestação >= salario * 30 / 100:
    (print('O financiamento foi NEGADO'))
else:'O financiamento foi ACEITO'

