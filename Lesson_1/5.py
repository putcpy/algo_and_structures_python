#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

LETTER1 = ord(input("Введите первую букву"))
LETTER2 = ord(input("Введите вторую букву"))
LETTER1_ORDER=LETTER1-96
LETTER2_ORDER=LETTER2-96
LETTER_DIST=max(0,abs(LETTER1-LETTER2)-1)
print(LETTER1_ORDER,LETTER2_ORDER,LETTER_DIST)