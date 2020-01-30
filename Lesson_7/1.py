"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import random

QUANT = int(random() * 10)
A = [0]*QUANT

for i in range(QUANT):
    A[i] = int(random() * 100)
print(f"Исходный массив: {A}")

def sort_bubble(A, QUANT):

    for i in range(QUANT):
        for j in range(QUANT - i-1):
            if A[j] < A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]

    return A

sort_bubble(A,QUANT)

print(f"Отсортированый массив \n{A}")
