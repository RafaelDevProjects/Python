pessoas = {'Nome':'Rafael','Idade':'18','Sexo':'M'} #dicionarios representados por chaves
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')

print(pessoas.keys())#mostra o indice de cada dicionario, as keys
print(pessoas.values())#mostra os valores de cada indice no dicionario
print(pessoas.items())#mostra as keys e values

for k in pessoas.keys():#mostra so as keys
    print(k)

for k,v in pessoas.items():#mostra as keys e valores em print
    print(f'O {k} tem {v}')
brasil=[]
estado1={'uf':'São paulo','sigla':'SP'}
estado2={'uf':'Rio de janeiro','sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['uf'])
estado={}
brasil=[]
for c in range (0,3):
    estado['uf']= str(input('Estado: '))
    estado['sigla']=str(input('Sigla: '))
    brasil.append(estado.copy) #estado.copy, copia o dicionario e cola ele na lista brasil
for e in brasil: #para cada estado no brasil
    for k,v in estado.items(): #para cada elemento dentro de estado
        print(f'{k}={v}')

