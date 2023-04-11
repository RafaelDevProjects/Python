print('\033[0;32;40m=-=-=-Progressão aritimética=-=-=-=\033[m')
num=int(input('Primeiro termo:'))
print('=-='*10)
razao=int(input('Razão da PA:'))
termo= num
c=1
total=0
mais=10
while mais != 0:
    total=total+mais
    while c <= total:
        print('\033[0;32;40m{} → \033[m'.format(termo),end='')
        termo=termo + razao
        c+=1
    print('\033[0;32;40mPAUSA\033[m')
    mais=int(input('Quantos termos quer ver a mais?'))
    print('='*40)
print('Progressão finalizada com {} termos mostrados'.format(total))