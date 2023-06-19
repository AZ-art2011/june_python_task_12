# Задача 12
from math import sqrt

sum_x_y = int(input('Укажите сумму двух загаданных натуральных чисел: '))
prod_x_y = -int(input('Укажите их произведение: '))

discrim = sum_x_y ** 2 + 4 * prod_x_y
if discrim > 0:
    sq = sqrt(discrim) / 2
    p = sum_x_y / 2
    x1 = p - sq
    x2 = p + sq

print(f'Задуманные числа {int(x1), int(x2)}')