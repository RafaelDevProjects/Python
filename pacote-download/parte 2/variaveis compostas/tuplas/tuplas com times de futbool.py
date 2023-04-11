times= ('CORINTHIANS','PALMEIRAS','ATLETICO','FLUMINENSE','SÃO PAULO','CURITIBA','BOTA FOGO','REAL MATRID','VASCO','BOCA JUNIORS',
'CHAPECOENSE','SANTOS','PSG','FLAMENGO','UBATUBANOS','TIMEDOCORA','TIME DOS ESQUISITOS', 'OS GORDIN DA ESQUINA','CARAMBOLAS','CHURAS')

print('LISTA DE TIMES')
print('~~'*20)
for t in times:
    print(t)
print('~~'*20)
print(f'Os 5 primeiros colocados são {times[0:6]}')
print('~~'*20)
print(f'Os quatro ultimos colocados são {times[-4:]}')
print('~~'*20)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('~~'*20)
print(f"O time do chapecoense esta na {times.index('CHAPECOENSE') + 1} posição ")