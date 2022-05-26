from math import inf
major = - inf
smaller = inf

for c in range(1, 6):
    weight = float(input(f'peso da {c}° pessoa: '))
    if weight > major:
        major = weight
    if weight < smaller:
        smaller = weight

print(f'A pessoa mais pesada tem {major}kg')
print(f'A pessoa menos pesada tem {smaller}kg')




