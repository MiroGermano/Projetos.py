from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
s = date.today().year - ano
print(f'Você tem {s} ano(s), você está na', end=' ')

if s <= 9:
    print('categoria \033[33mMIRIM.')
elif s <= 14:
    print('categoria \033[33mINFANTIL.')
elif s <= 19:
    print('categoria \033[33mJUNIOR')
elif s <= 25:
    print('categoria \033[33mSÊNIOR')
else:
    print('categoria \033[33mMASTER')


