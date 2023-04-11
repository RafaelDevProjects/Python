from datetime import datetime
print('-='*10,'CADASTRO DE TRABALHO','=-'*10)
cadastro={}
cadastro['nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
sexo=str(input('Sexo [M/F]: ')).strip()[0]
if sexo in 'Mm':
    cadastro['sexo']='masculino'
if sexo in 'Ff':
    cadastro['sexo']='feminino'
cadastro['ctps']=int(input('Carteira de trabalho (0 não tem) : '))
idade= datetime.now().year - nasc
cadastro['idade']=idade
if cadastro['ctps'] !=0:
    cadastro['ano de contratação']=int(input('Ano de contratação: '))
    cadastro['salario']=float(input('Salário: R$ '))
    if sexo in 'Mm':
        cadastro['idade de aposentadoria'] = (idade + cadastro['ano de contratação'] +35) -  datetime.now().year
    if sexo in 'Ff':
        cadastro['idade de aposentadoria'] = (idade + cadastro['ano de contratação'] + 30) - datetime.now().year
print('='*30)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor de {v} ')
print('='*30)
print('- O ano de aposentadoria para mulheres é de 30 anos de serviço\n'
      '- O dos homens é de 35 anos de serviço')
