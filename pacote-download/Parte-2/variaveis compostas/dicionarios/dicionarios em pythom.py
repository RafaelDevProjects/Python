pessoa={}
pessoa['nome']= str(input('Nome: '))
pessoa['media']= float(input('Media: '))
print(f' A media de {pessoa["nome"]} foi de {pessoa["media"]}')
print(f'- O nome igual a {pessoa["nome"]}')
print(f'- A media igual a {pessoa["media"]}')
if pessoa['media']>=6:
    print(f'{pessoa["nome"].upper()} APROVADO !!!')
else:
    print(f'{pessoa["nome"].upper()} REPROVADO...tente novamente')