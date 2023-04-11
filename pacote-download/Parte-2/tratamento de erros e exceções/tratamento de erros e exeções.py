try:        #tenta fazer alguma coisa
    a= int(input('Numerador: '))
    b= int(input('Denominado: '))
    r= a/b
except (ValueError, TypeError):   #cria uma exeção para os erros de valores e tipo de classe
    print(f'Infelizmente tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:       #erro de divisão por 0
    print(f'Não é possivel dividir um valor por zero')
except KeyboardInterrupt:       #erro de nenhum valor colocado, se o usuario sair do programa
    print(f'O usuario decidiu não informar os dados')
except Exception as erro:       #ferramenta para encontrar o tipo de erro
    print(f'O erro encontrado foi {erro.__cause__}')
else:       #se não der erro o resultado aparecera
    print(f'O resultado é {r}')
finally:    #Se tiver erro ou acerto o finally vai ser sempre o mesmo
    print('Volte sempre! ')


