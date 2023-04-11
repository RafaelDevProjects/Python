#lista=[] é feita por []
lista=['rafael','santos','cadeida']

lista.remove('rafael') #remove a palavra que vc escolher

lista.append('alface')#adiciona um item ao final

lista.sort(reverse=True)

lista[2]='SORTE' #mudou a paravra no item [2] para SORTE

print(f'essa lista tem {len(lista)} elementos') #len conta quantos elementos tem a lista
lista.insert(0,'cachorro') #na possição colocada, ele insere um elemento

lista.pop()#elimina o ultimo elemento

valores=[]
valores.append(2)
valores.append(5)#adiciona um item a lista
valores.append(10)
for v in valores: #mostra a lista só com os numeros
    print(f'{v}...')
for cont in range (0,5): #adiciona 5 valores de escolha do input
    valores.append(int(input('Digite um valor:')))
for c,v in enumerate(valores): #enumera as posições de cada item
    print(f'Na posição {c} encontrei o valor {v}!!!')
a= [1,2,3,5,6]
b=a #cria uma ligação entre as duas listas
b[2]=5 #devido a ligação entre as listas, a lista a e b vão ser mudadas
print(f'lista A {a}')
print(f'lista A {a}')
x=[1,2,4,7,9]
y=x[:] #desse modo cria uma copia e não uma lição entre elas
y[2]= 7 #agora da pra mudar uma lista da outra
print(f'lista x {x}')
print(f'lista y {y}')

print(sorted(valores))
