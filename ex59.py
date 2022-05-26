numberOne = float(input('\nDigite o primeiro número: '))
numberTwo = float(input('Digite o Segundo número: '))

c = 1
while c != 0:
    print("""
    --- Menu ---
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior 
[ 4 ] Novos números
[ 5 ] Sair do programa
    """)
    choiceNumber = int(input('Escolha uma opção:'))

    if choiceNumber == 1:
        print(f'{numberOne}+{numberTwo}= {numberTwo+numberOne}')

    elif choiceNumber == 2:
        print(f'{numberOne}x{numberTwo}= {numberTwo*numberOne}')

    elif choiceNumber == 3:
        if numberOne > numberTwo:
            print(f'{numberOne} é maior que o número {numberTwo}')
        else:
            print(f'{numberTwo} é maior que o número {numberOne}')

    elif choiceNumber == 4:
        print('informe os números novamentes')
        numberOne = float(input('\nDigite o primeiro número: '))
        numberTwo = float(input('Digite o Segundo número: '))

    elif choiceNumber == 5:
        c = 0

    elif choiceNumber <= 0 or choiceNumber > 5:
        print('Opção inválida! tente novamente')



