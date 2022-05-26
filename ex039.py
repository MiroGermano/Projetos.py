from datetime import date
sexo = str(input('Qual é o seu sexo? ')).strip().lower()
if sexo == 'feminino':
    print('Você não precisa se alistar!')

elif sexo == 'masculino':

    ano = int(input('Qual o seu ano de nascimento? '))
    valor = date.today().year
    s = valor - ano

    print('Quem nasceu em {} tem {} anos em {}'.format(ano, s, valor))

    if s == 18:
        print('Está na hora de se alistar! ')
    elif s > 18:
        if s == 19:
            print('O seu alistamento está atrasado há 1 ano')
        else:
            print('O seu alistamento está atrasado há {} anos'.format(s-18))
    elif s < 18:
        if s == 17:
            print('Ainda falta 1 ano para seu alistamento')
        else:
            print('Ainda faltam {} anos para o seu alistamento'.format(18-s))
