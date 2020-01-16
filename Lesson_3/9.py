# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
A_ROW = 5
A_COL = 5

A = []
MIN_IN_COL = []

for i in range(A_ROW):
    b = []
    for num in range(A_COL):
        b.append(randint(0, 10))
        print(f"{b[num]:4d}", end='')
    A.append(b)
    print(" ")

for j in range(A_COL):
    c = []
    for i in range(A_ROW):
        c.append(A[i][j])
    MIN_IN_COL.append(min(c))
print(f"Максимальный элемент среди минимальных значений столбцов матрицы: {max(MIN_IN_COL)}")
