from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ãngulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
