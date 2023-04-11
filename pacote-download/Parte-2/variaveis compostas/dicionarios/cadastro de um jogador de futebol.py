jogadores=list()
jogador={}
gol=list()
while True:
    jogador['nome']= str(input('Nome do jogador: '))
    tot= int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    gol.clear()
    for c in range (0,tot):
        gol.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols']=gol[:]
    jogador['total'] = sum(gol)
    jogadores.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar [S/N] ?')).strip()[0]
        if resp in 'SNsn':
            break
        else:
            print('[S/N] tente novamente...')
    if resp in 'Nn':
        break
print('='*40)
print(f'cod ',end='')
for i in jogador.keys():
    print(f' {i:<15}' ,end='')
print()
print('='*40)
for k, v in enumerate(jogadores):
    print(f' {k:>2} ',end= '')
    for d in v.values():
        print(f' {str(d):<15} ',end= '')
    print()
print('='*40)
while True:
    busca= int(input('Mostrar dados de qual jogador? (999 pra parar)'))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f' ERRO !, não exite o jogador com o cod {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in  enumerate (jogadores[busca]["gols"]):
            print(f'--> Na partida {i+1} o jogador fez {g} gols')
print('<<<ENCERRANDO>>>')