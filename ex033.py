num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

print('Os números digitados recebem a seguinte sequência: ', end='')

if num1 > num3 and num1 > num2:
    if num2 > num3:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)

elif num2 > num3 and num2 > num1:
    if num3 > num1:
        print(num1, num3, num2)
    else:
        print(num3, num1, num2)
else:
    if num2 > num1:
        print(num1, num2, num3)
    else:
        print(num2, num1, num3)



