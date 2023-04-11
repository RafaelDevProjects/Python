cont=0
soma=0
while True: #estrutura infinita
    numero=int(input('Digite um numero:[999 para parar]'))
    if numero == 999:
        break #vai quebrar o looping infinito
    soma+=numero #vai somar sem o 999
    cont += 1  # contador não vai contar o 999
#print('A soma dos {} numeros registrados foi {}'.format(cont,soma))
print(f'A soma dos {cont} numeros registrados foi de {soma}') #novo modo de fstrings
