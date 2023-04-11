from datetime import date
ano=(int(input('Informe o ano do seu nascimento=')))
print('-=-'*20)
atual= date.today().year
idade= atual - ano
if idade==18:
    print('Você tem 18 anos. Esta na hora do seu alistamento. Se aliste IMEDIATAMENTE')
elif idade < 18:
    saldo=18-idade
    print('Você tem {} anos . Ainda não esta na hora de se alistar. Tente novamente em {} anos'.format(idade,saldo))
    print('Seu alistamento sera em {}'.format(saldo+atual))
else:
    saldo=idade-18
    print('Você tem {} anos. ja pra você ter se alistado, há {} anos'.format(idade,saldo))
    print('Seu alistamento deveria ter sido em {}'.format(atual-saldo))
