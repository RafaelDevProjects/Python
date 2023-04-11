from datetime import date
nasc=date.today().year
totmaior=0
totmenor=0
for c in range (1,8):
    data=int(input('Data de nacimento da {}º pessoa:'.format(c)))
    idade=nasc-data
    if idade >= 21:
        totmaior+=1
    else:
        totmenor+=1
print('Ao todo tivemos {} pessoas maior de idade e {} menores de idade'.format(totmaior,totmenor))