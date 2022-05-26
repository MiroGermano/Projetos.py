average = 0
man = 0
woman = 0
oldName = ''
for c in range(1, 5):
    print(f'-----{c}° Pessoa-----')
    name = str(input('Qual é o seu nome? ')).strip().capitalize()
    yearsOld = int(input('Qual é a sua idade? '))
    sex = str(input('Qual seu sexo?[M/F] ')).strip().upper()
    average += yearsOld
    if sex == 'M':
        if yearsOld > man:
            man = yearsOld
            oldName = name
    if sex == 'F':
        if yearsOld < 20:
            woman += 1

print(f'A média de idade do grupo é de {average/4}anos.')
print(f'O homem mais velho tem {man} anos e se chama {oldName}.')
print(f'Ao todo são {woman} mulheres com menos de 20 anos')


