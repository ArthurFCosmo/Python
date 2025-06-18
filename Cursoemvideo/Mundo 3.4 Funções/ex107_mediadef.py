def notas(*N, sit=False):
    '''
    :Função ---> notas(*N, sit=True)
    :'*N' recebe vários valores notas (Valores numéricos, podem ser float ou int)
    :'sit=' Recebe True ou False

    retorna = um dicionário com: 
        :O total de notas
        :A maior nota digitada
        :A menor nota digitada
        :Todas as notas digitadas
        :Média das notas digitadas

    Se sit=True, mostra a situação em relação a média seguindo o seguinte padrão:
        :7 a 10 = aprovado
        :5 a 6.999 = recuperação
        :0 a 4.999 = reprovado

    Criado por arthur cosmo
    '''
    NOTAS = N
    R = {}
    R['Total de notas'] = len(N)
    R['Maior Nota'] = max(NOTAS)
    R['Menor Nota'] = min(NOTAS)
    R['Notas'] = N
    R['Média'] = f'{sum(N) / len(N):.2f}'
    if sit:
        if float(R['Média']) >= 7:
            R['Situação'] = 'Aprovado'
        if float(R['Média']) < 7 and float(R['Média']) > 5:
            R['Situação'] = 'Recuperação'
        else:
            R['Situação'] = 'Reprovado'
    return R


RESP = notas(5, 1, 8, sit=True)
print(RESP)