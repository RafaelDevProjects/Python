def fatorial(n,show=0):
    """
     ---> Calcula a fatorial de um numero.
    :parameter n: O numero a ser calculado.
    :parameter show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um numero n
    """
    f=1
    print(f'O valor do fatorial {n} é igual:')
    for c in range (n, 0, - 1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(25,True))
help(fatorial)