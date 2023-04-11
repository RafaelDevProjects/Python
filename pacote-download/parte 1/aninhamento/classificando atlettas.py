from datetime import date
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=-='*30)
nasc=int(input('Informe o seu ano de nacimento:'))
atual=date.today().year
idade=atual-nasc
if idade <=9:
    print('O atleta tem {} anos, é um atleta categoria:MIRIM'.format(idade))
elif idade <=14:
    print('O atleta tem {} anos, é um atleta categoria: INFANTIL'.format(idade))
elif idade <=19:
    print('O atleta tem {} anos, é um atleta categoria:JUNIOR'.format(idade))
elif idade <=25:
    print('O atleta tem {} anos, é um atleta categoria:SENIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, é um atleta categoria:MASTER'.format(idade))
 