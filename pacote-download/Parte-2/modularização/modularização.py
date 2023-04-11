def fatorial(n):
    f=1
    for n in range (1, n+1):
        f *= n
    return f


num=int(input('Digite um numero:'))
fat=fatorial(num)
print(f'O fatorial do numero {num} é {fat}')