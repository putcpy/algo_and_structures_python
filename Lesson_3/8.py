"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

A_ROW = 4
A_COL= 4
A = []

for i in range(A_ROW):
    b = []
    for j in range(A_COL):
        USER_NUM = int(input("введите число: "))
        b.append(USER_NUM)
    b_sum = sum(b)
    b.append(b_sum)
    A.append(b)

for i in A:
    for num in i:
        print(f"{num:4d}", end='')
    print()
