velocidade = float(input('Escreva a velocidade do carro para saber se foi multado: '))

if velocidade > 80:
    print('Você foi multado e a multa vai custar {}'.format((velocidade - 80)*7))

print('Tenha um bom dia! Dirija com segurança!')

