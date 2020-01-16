#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random


QUANT = random.randint(2, 10)
A = [0]*QUANT

for i in range(QUANT):
    A[i] = random.randint(-100, 100)

MIN_A = min(A)
MIN_A_INDEX = A.index(MIN_A)

print(f'Максимальный отридцательный элемент в массиве {A}: {MIN_A}, его индекс {MIN_A_INDEX}')