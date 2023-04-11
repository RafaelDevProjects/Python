print(10*'~','Soma de N numeros',10*'~')
cont=0
num=0
soma=0
num = int(input('Digite um numero inteiro [999 para parar]:'))
while num != 999:
    soma=soma+num
    cont=cont + 1
    num = int(input('Digite um numero inteiro [999 para parar]:'))
print('Você digitou {} números e a soma de todos eles é igual a {}'.format(cont,soma))


