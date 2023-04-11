def leiaint(msg):
    while True:
        try:
            inteiro=int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! o valor digitado não é valido para o programa\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuario decidiu não informar o valor\033[m')
            return 0
        else:
            return inteiro


def leiafloat(msg):
    while True:
        try:
            real=float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! o valor digitado não é valido para o programa\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuario decidiu não informar o valor\033[m')
            return 0
            break
        else:
            return real


inteiro=leiaint('Digite um numero inteiro: ')
real=leiafloat('Digite um numero real: ')
print(f'O valor digitado foi {inteiro}')
print(f'O valor digitado foi {real}')

