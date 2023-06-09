"""
Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все
компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def profit_or_loss(inp: list[int | float]) -> bool:
    for item in inp:
        if sum(inp[item]) < 0:
            return False
    return True


data = {'company_1': [800, -500], 'company_2': [500, -400], 'company_3': [700, -550]}

print(profit_or_loss(data))
