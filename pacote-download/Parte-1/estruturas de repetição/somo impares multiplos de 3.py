s=0
cont=0
for c in range (1,51,2):
    if c % 3 ==0:
        cont += 1
        s +=c
print('A soma de todos os {} valores foi {}'.format(cont,s))
