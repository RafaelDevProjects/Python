galera=[]
dados={}
soma=0
while True:
    dados.clear()
    dados['nome']=str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('ERRO! TENTE NOVAMENTE...')
    dados['idade']=int(input('Idade: '))
    soma+=dados['idade']
    galera.append(dados.copy())
    while True:
        resp=str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'NnsS':
            break
        print('ERRO! TENTE NOVAMENTE...')
    if resp == 'N':
        break
print('='*30)
numcadastros=len(galera)
print(galera)
print(f'A) Foram cadastradas {numcadastros} pessoas.')
media= soma / len(galera)
print(f'B) A media de idade de todas as pessoas cadastradas foi de {media:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo']=='F':
        print(f'{p["nome"]}', end= ' ')
print()
print(f'D) Lista de pessoas que estão acima da media:')
for p in galera:
    if p['idade'] >= media:
        print('   ',end=0)
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<<<ENCERRADO>>>')