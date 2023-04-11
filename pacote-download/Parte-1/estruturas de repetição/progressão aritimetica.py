print('===============PROGRESSÃO DE UMA PA==============')
n1=int(input('digite o primeiro termo: '))
n2=int(input('digite a razão da PA: '))
dec=n1 + (10 - 1) * n2
for c in range (n1 , dec+n2,  n2):
    print(c,end= " ->")
print('acabou')