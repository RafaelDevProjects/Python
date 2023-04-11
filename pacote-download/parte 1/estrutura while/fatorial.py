num=int(input('\033[0;32;40mDigite um número para descobrir seu fatorial:\033[m'))
c= num
f=1
print('>>>>>Calculando {}!= '.format(num),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('\033[0;32;40m{}\033[m'.format(f))
