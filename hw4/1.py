# Вычислить число c заданной точностью d, пример:
# При $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *
import math

d = input('Задайте точность числа d: ')
getcontext().prec = len(d.split('.')[1]) + 1
p = Decimal(math.pi) + Decimal('0.0')
print (p)