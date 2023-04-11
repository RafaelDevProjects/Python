from lib.interface import *
from time import time
from lib.arquivo import *


arq = 'programadecadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessaos cadastradas','Cadastrar nova pessoa','Sair do programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO: digite uma opção valida\033[m')
    sleep(1)




