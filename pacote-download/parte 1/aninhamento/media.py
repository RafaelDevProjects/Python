nota1=(float(input('Me mostre sua primeira nota=')))
nota2=(float(input('Me mostre sua segunda nota=')))
media= (nota1 + nota2)/2
if media <= 5.0:
    print('MEDIA={}'.format(media))
    print('A media foi menor que 5.0. Foi REPROVADO')
    print('Faça novamente a sua prova')
elif media >= 7.0:
    print('MEDIA= {}'.format(media))
    print('A media foi maior ou igual a 7.0. Foi APROVADO')
    print('Ate o proxima prova!!!')
elif media >= 5.0 and media < 7:
    print('MEDIA={}'.format(media))
    print('A sua media não foi o suficiente. esta em RECUPERAÇÃO')
    print('Boa sorte nessa prova!!')