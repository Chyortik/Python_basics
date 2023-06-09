"""
Задание №1
✔ Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

"""

# Краткое решение

list_1 = [1, 2, 2, 3, 3, 4, 5]
unique_list = list(set(list_1))
print(unique_list)

# Длинное решение

list_1 = [1, 2, 2, 3, 3, 4, 5]
list_2 = []
for item in list_1:
    if item not in list_2:
        list_2.append(item)
print(list_2)
