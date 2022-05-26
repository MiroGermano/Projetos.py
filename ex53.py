frase = str(input('Escreva uma palavra ou frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.\n')

if junto == inverso:
    print(f'{frase.capitalize()} é um palíndromo')
else:
    print(f'{frase.capitalize()} Não é um palíndromo')