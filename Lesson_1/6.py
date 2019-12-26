# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

LETTER_NUM = int(input("Введите номер буквы"))
LETTER = chr(LETTER_NUM+96)
print(LETTER)