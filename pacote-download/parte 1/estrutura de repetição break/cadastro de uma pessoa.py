print('-'*30)
print('       \033[0;32;40mÁREA DE CADASTRO\033[m')
mulheres=masculino=maiores=0
while True:
    print('-' * 30)
    print('CADRASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade:'))
    sexo=' '
    while sexo not in 'MmFf':
        sexo = str(input('Gênero [M/F]:')).upper().strip()[0]
    if idade >= 18:
        maiores+=1
    if sexo in 'Mm':
        masculino+=1
    if sexo in 'Ff' and idade <= 20:
        mulheres+=1
    continuar= ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]?')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('-' * 30)
print(f'{maiores} pessoas maiores de 18 anos')
print(f'{masculino} homens')
print(f'{mulheres} Mulheres com menos de 20 anos')

