import math
numero=int(input('escolha um número inteiro='))
print('''Escolha uma das bases para conversão:
[ 1 ] para um numero HEXADECIMAL
[ 2 ] para um numero OCTAL
[ 3 ] para um numero BINARIO''')
opção=(int(input('Sua opção:')))
if opção == 1:
    print('{} convertido para hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para binario é igual a {}'.format(numero,bin(numero)[2:]))
else:
    print('DIGITE UM NUMERO VÁLIDO')
