def notas(*num,sit=False):
    '''
        --> função para descobrir a situação de uma turma.
    :param num: medias dos alunos.
    :param sit: (opcional) situação dos alunos [otima,razoavel,ruim].
    :return:dicionario com varias imformações sobre a situação da turma.
    '''
    boletim={}
    boletim['total']=len(num)
    boletim['maior']=max(num)
    boletim['menor']=min(num)
    boletim['media']= sum(num) / len(num)
    if sit:
        if boletim['media'] >= 6:
            boletim['situação']= 'Razoavel'
        if boletim['media'] < 6:
            boletim['situação']= 'Ruim !!'
        if boletim['media'] >= 8:
            boletim['situação'] = 'OTIMO !!'
    return boletim




resp = notas(6,7.3,6.8,1.2,sit=True)
print(f'BOLETIM: {resp}')