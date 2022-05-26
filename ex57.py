s = 1
while s != 0:
    gender = str(input('Qual é o seu sexo? [M/F]')).upper().strip()
    if gender == 'M':
        gender = 'Masculino'
        s = 0

    elif gender == 'F':
        gender = 'Feminino'
        s = 0

    else:
        print('Você digitou um valor inválido, tente novamente')

print(f'Seu sexo é {gender}')