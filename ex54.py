from datetime import date
counter = 0
people = int(input('Quantas pessoas querem saber se já são de maiores? '))

for majority in range(1, people + 1):
    years = int(input('Em que ano você nasceu? '))
    s = date.today().year - years
    assert date.today().year >= 2022, 'A data do computador está errada'
    if s >= 18:
        counter += 1

print(f'{people - counter} pessoas não atingiram a maioridade e {counter} já são maiores')
