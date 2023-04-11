
def voto(ano):
    from datetime import datetime
    global idade
    global n
    idade= datetime.now().year - ano
    if idade < 16:
        n='NEGADO'
        return n
    elif 18 > idade >= 16 or idade > 65:
        n='OPCIONAL!'
        return n
    elif 70 > idade >= 18:
        n='OBRIGATORIO!'
        return n




voto(int(input('Ano de nascimento:')))

print(f'Com {idade} anos seu voto é {n} ')