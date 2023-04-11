dados=list()
dados.append('Rafael')
dados.append(18)
pessoas=list()
pessoas.append(dados[:])#uma lista dentro de outra lista
dados[0]='joao'
dados[1]='21'
pessoas.append(dados[:])
print(dados) # [:] represeta uma copia
print(pessoas)
galera=[['rafael',19], ['joana',21], ['matheus',30]]
print(galera)
print(galera[0][0])
print(galera[1][1]) #[1] representa o numero da lista. [1] representa o elemento dentro da lista
print(galera[2][0])
for p in galera: #para cada pessoa na lista...
    print(f'{p[0]} tem {p[1]} anos de idade') #mostra o nome e a idade