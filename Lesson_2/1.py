"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
while 1 == 1:

    A = int(input("Введите первое число "))
    B = int(input("Введите второе число "))
    USER_OPERATION = input("Введите знак операции '+', '-', '*', '/'. Для завершения программы введите '0' ")
    if USER_OPERATION == "+" or USER_OPERATION == "-" or USER_OPERATION == "*" :
        if USER_OPERATION == "+" :
            C = str(A + B)
            print("Результат" + C)
        elif USER_OPERATION == "-" :
            C = str(A - B)
            print("Результат" + C)
        elif USER_OPERATION == "*" :
            C = str(A * B)
            print("Результат" + C)
    elif USER_OPERATION == "/" :
        if B != 0:
            C = str(A / B)
            print("Результат деления: " + C)
        else:
            print("На ноль делить нельзя, введите другое число")
    elif USER_OPERATION == "0":
        break
print("Спасибо, что были с нами")
