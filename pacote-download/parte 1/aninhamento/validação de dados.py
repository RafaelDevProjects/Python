
s =str(input('Informe seu sexo: [M/F]:')).upper() [0].strip()
while s not in 'MF':
    s= str(input('Dados inválidos. digite novamente seu sexo:')).upper() [0].strip()
print('Sexo {} registrado com sucesso'.format(s))

