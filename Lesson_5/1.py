"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


import collections


Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

base_enterprise = {}

n = int(input("Введите количество предприятий: "))

for i in range(n):
    name = input('Введите название предприятия: ')
    q1_profit = int(input('Введите прибыль за 1-й квартал: '))
    q2_profit = int(input('Введите прибыль за 2-й квартал: '))
    q3_profit = int(input('Введите прибыль за 3-й квартал: '))
    q4_profit = int(input('Введите прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        q1 = q1_profit,
        q2 = q2_profit,
        q3 = q3_profit,
        q4 = q4_profit
    )


total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')
