"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

ascii_min = 32
ascii_max = 127

i = ascii_min

while True :
    for j in range(10) :
        if i + j > ascii_max :
            break
        print(f'{i + j} - {chr(i + j)}', end='\t')

    print('')

    if i + j > ascii_max :
        break
    i += 10