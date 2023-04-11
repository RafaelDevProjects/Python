'''help() #comando para usar no console, (entre os parenteses colocar uma função)'''


def somar(a=0,b=0,c=0):
    """
    :param a:Numero para somar 
    :param b: Numero para somar
    :param c: Numero para somar
    :return: return em s
    """   #O novo help da função somar()
    s= a + b + c
    return s  #Retorna as respostas para o determinado elemento antes de somar (r1,r2,r3)
r1=somar(2,4)
r2=somar(1,0)
r3=somar(4,1)
print(f'As somas foram {r1},{r2},{r3}')
help(somar)


def par(n=0): #(n=0) se eu não colocar nenhum [n], o n ira valer 0
    if n % 2 == 0:
        return True  #diz se o retorno é verdadeiro
    else:
        return False  #diz se o retorno é falso
num=int(input('Digite um numero:'))
if par(num):
    print(f'Par!!')
else:
    print(f'Impar!!')