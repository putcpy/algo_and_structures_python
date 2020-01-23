"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


def hex_val(num):
    hv = 0
    for i in range(len(num)):
        hv += int(num[i], 16) * (16 ** (len(num) - i - 1))
    return hv

HEX_DICT = collections.defaultdict(list)
A = input("Введите первое число: ")
B = input("Введите второе число: ")
HEX_DICT[A] = list(A)
HEX_DICT[B] = list(B)

HEX_SUM = str(hex(hex_val(HEX_DICT[A] ) + hex_val(HEX_DICT[B])))[2::]
HEX_MULT = str(hex(hex_val(HEX_DICT[A] ) * hex_val(HEX_DICT[B] )))[2::]

print(f"Сумма чисел {HEX_SUM}, Произведение {HEX_MULT}")