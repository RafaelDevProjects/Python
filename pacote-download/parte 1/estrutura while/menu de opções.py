from time import sleep
print('\033[0;32;40m=-=-=-=-=-=-=Menu de opções=-=-=-=-=-=-=\033[m')
valor1=int(input('Digite um valor:'))
valor2=int(input('Digite outro valor:'))

resposta=0
while not resposta==5:
    print(20 * '==')
    print('  [ 1 ] Somar\n'
          '  [ 2 ] multiplicar\n'
          '  [ 3 ] maior\n'
          '  [ 4 ] novos números\n'
          '  [ 5 ] sair do programa')
    resposta=int(input('>>>>> Digite a sua opção:'))
    if resposta == 1:
        soma=valor1+valor2
        print('\033[0;32;40mA soma de {} + {} é igual a {}\033[m'.format(valor1,valor2,soma))
    elif resposta == 2:
        multiplicação=valor1*valor2
        print('\033[0;32;40mA multiplicação de {} x {} é igual a {}\033[m'.format(valor1, valor2, multiplicação))
    elif resposta==3:
        if valor1<valor2:
            print('\033[0;32;40mO {} é o maior\033[m'.format(valor2))
        elif valor1>valor2:
            print('\033[0;32;40mO {} é o maior\033[m'.format(valor1))
        else:
            print('\033[0;32;40mOs dois valores {} e {} são iguais\033[m'.format(valor1,valor2))
    elif resposta==4:
        print('Informe os valores novamente:')
        valor1=int(input('Informe o número:'))
        valor2=int(input('Informe o número:'))
    else:
        print('Opção invalida.Tente novamente.')
if resposta==5:
    print('finalizando...')
    sleep(2)
    print('\033[0;32;40mPrograma fechado.\033[m')


