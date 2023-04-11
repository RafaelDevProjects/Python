print(50*'=')
print(f'{"CONTADOR DE VOGAIS":^50}')
print(50*'=')
palavras=('acento','lapis','fone','mesa','cadeira','computador','liçao',
          'computador','fone','fome','olhar','teclado','celular','pythom','ensinar')
for p in palavras:
    print(f'\nNa palavra \033[0;32m{p.upper()}\033[m temos:', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')