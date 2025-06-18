sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite aqui seu sexo [M] masculino ou [F] feminino: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('''\033[31mPor favor, ao inserir seu sexo digite apenas a tecla [F] para feminino
ou a tecla [M] para masculino.\033[m''')
if sexo == 'M':
    print('Você é homem !')
else:
    print('Você é mulher !')
