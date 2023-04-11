def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! digite um número inteiro valido\033[m')
        if ok:
            break
    return valor



n=leiaint('Digite um numero:')
print(f'O numero digitado foi {n}')