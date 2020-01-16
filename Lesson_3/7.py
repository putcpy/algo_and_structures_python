"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random


QUANT = int(random() * 10)
A = [0]*QUANT
B = []

for i in range(QUANT):
    A[i] = int(random() * 100)

MIN_A = min(A)
MIN_A_INDEX = A.index(MIN_A)
print(f'Из массива {A}')

del A[MIN_A_INDEX]

B = A
MIN_B = min(B)
MIN_B_INDEX = B.index(MIN_B)

del B[MIN_B_INDEX]

print(f'получаем {B}, удалив два минимальных значения: {MIN_A} и {MIN_B}')



