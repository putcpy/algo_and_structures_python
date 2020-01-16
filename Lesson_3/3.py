#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random


QUANT = int(random() * 10)
A = [0]*QUANT
MIN_A = min(A)
MIN_A_INDEX = A.index(MIN_A)
MAX_A = max(A)
MAX_A_INDEX = A.index(MAX_A)
B = A

for i in range(QUANT):
    A[i] = int(random() * 100)

B[MIN_A_INDEX], B[MAX_A_INDEX] = A[MAX_A_INDEX], A[MIN_A_INDEX]
print(f'Было: {A}')
print(f'Стало: {B}')
