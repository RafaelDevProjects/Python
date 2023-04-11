expressao=(str(input('digite a sua expressao:')))
pilha=[]
for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão esta correta')
else:
    print('A sua expressão esta incorreta')