"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random
QUANT = int(random() * 10)
A = [0]*QUANT
A_SUM = 0

for i in range(QUANT):
    A[i] = int(random() * 100)

MIN_A = min(A)
MAX_A = max(A)

for i in range (QUANT):
    A_SUM = A_SUM + A[i]

A_SUM = A_SUM - MIN_A - MAX_A

print(f'Сумма всех чисел массива {A} равна {A_SUM}, не включая минимальное значение {MIN_A} и максимальное значение {MAX_A}')