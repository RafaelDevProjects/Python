print('-'*30)
print(3*' ','\033[0;32;40mSEQUENCIA DE FIBONACCI\033[m')
print('-'*30)
n=int(input('Digite quantos termos quer ver na sequenia de Ficonacci:'))
t1=0
t2=1
print('{} ➝ {}'.format(t1,t2),end='')
cont=3
while cont <= n:
    t3 = t1 + t2
    print('➝ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➝ FIM')