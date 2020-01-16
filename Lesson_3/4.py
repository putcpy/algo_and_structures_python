# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random

QUANT = 100
A = [0]*QUANT

for i in range(QUANT):
    A[i] = int(random() * 10)
print(f"смотрим массив: {A}")

B = set(A)
max_elem_count = 0
max_freq_value = None

for i in B:
    this_elem_count = 0
    for j in A:
        if i == j:
            this_elem_count += 1

    if this_elem_count > max_elem_count:
        max_elem_count = this_elem_count
        max_freq_value = i

print(max_freq_value)
