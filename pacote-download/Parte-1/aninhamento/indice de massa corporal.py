print('INDICE DE MASSA CORPORAL')
print('=-='*30)
peso=float(input('Qual é o seu peso (kg):'))
altura=float(input('Qual é a sua altura (m):'))
imc=peso / (altura * altura)
if imc < 18.5:
    print('IMC de {:.2f}. \nAbaixo de 18,5: Abaixo do Peso'.format(imc))
elif imc <= 25:
    print('IMC de {:.2f}. \nEntre 18,5 e 25: Peso Ideal'.format(imc))
elif imc <= 30:
    print('IMC de {:.2f}. \nEntre 25 até 30: Sobrepeso'.format(imc))
elif imc < 40:
    print('IMC de {:.2f}. \nEntre 30 até 40: Obesidade'.format(imc))
else:
    print('IMC de {:.2f}. \nAcima de 40: Obesidade Mórbida'.format (imc))


