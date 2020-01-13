"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

A = input("введите число 1 ")
B = input("введите число 2 ")
C = input("введите число 3 ")

def sum_for_string(A):
    sum = 0
    for num in A:
        sum = sum + int(num)
    return sum

A_STR_SUM = int(sum_for_string(A))
B_STR_SUM = int(sum_for_string(B))
C_STR_SUM = int(sum_for_string(C))

if A_SUM > B_SUM and A_SUM > C_SUM:
    print (f'Победило число {A}. Сумма его цифр {A_SUM}')
elif B_SUM > A_SUM and B_SUM > C_SUM:
    print (f'Победило число {B}. Сумма его цифр {B_SUM}')
elif C_SUM > A_SUM and C_SUM > B_SUM:
    print (f'Победило число {C}. Сумма его цифр {C_SUM}')
else:
    print ("Что-то пошло не так")


