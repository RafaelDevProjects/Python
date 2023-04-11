from time import sleep
print('ANALISADOR DE TRIANGULOS')
print('--=--'*20)
print('Dê o comprimento de 3 retas')
a = float(input('reta A='))
b = float(input('reta B='))
c = float(input('reta C='))
print('analisando se é um triangulo...')
sleep(3)
if a < b + c and b < a + c and c < a + b:
    print ('Essas retas formam um triangulo ',end='')
    if a == b == c :
        print('EQUILATERO!!')
    if a != b and c != a and c !=b :
        print('ESCALENO!!')
    else:
        print('ISÓCELES')

else:
    print('Com essas retas não é possiel criar um triangulo')

