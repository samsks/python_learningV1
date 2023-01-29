import math


def delta(a, b, c):
    return b**2 - 4 * a * c
# melhor forma:  return pow(b, 2) - 4 * a * c


def bhaskara(a, b, c):
    d = delta(a, b, c)

    if d < 0:
        return 'Delta Negativo'

    raiz_delta = round(math.sqrt(d), 2)

    x1 = round((-b + raiz_delta) / (2 * a), 2)
    x2 = round((-b - raiz_delta) / (2 * a), 2)

    return f'x1={x1}, x2={x2}'


print(bhaskara(7, 3, 4))
# Delta Negativo

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56

print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12
