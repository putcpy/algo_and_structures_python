"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import random

QUANT = int(random() * 10)
A = [0]*QUANT

for i in range(QUANT):
    A[i] = int(random() * 100)
print(f"Исходный массив: {A}")

def sort_merge(A):

    if len(A) > 1:
        left = A[:len(A) // 2]
        right = A[len(A) // 2:]

        sort_merge(left)
        sort_merge(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A

sort_merge(A)

print(f"Отсортированный массив: {A}")