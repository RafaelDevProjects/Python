somaidade=0
cont=0
sexo=0
mediaidade=0
maioridadehomem=0
for c in range (1,5):
    print('---------{}º PESSOA--------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M\F]: ')).strip()
    if c == 1 and sexo in "Mm'":
        maioridadehomem=idade
        nomedomaivelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaivelho = nome
    if sexo in 'Ff' and idade < 20:
        cont+=1
    somaidade+=idade
    mediaidade=somaidade / 4
print('-=-'*20)
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é o {} e tem {} anos'.format(nomedomaivelho,maioridadehomem))
print('Tem {} com menos de 20 anos'.format(cont))
