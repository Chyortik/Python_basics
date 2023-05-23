"""
Задание №2. Создайте в переменной data список значений разных типов,
перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число, только если он положительный
✔ результат проверки на строку только если он положительный.
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

a = 15
b = 'string'
c = (1, 4, 3, 8, 2)
d = {1: 2, 5: 8}
e = [5, 4, 8, 5, 6, 5, 8]
print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}, d - {type(d)}, e - {type(e)}')

data = [a, b, c, 15, 'string']
for i, el in enumerate(data, start=1):
    print(i, el, id(el), el.__sizeof__(), hash(el))
    if isinstance(el, int):
        print('Это целое число')
    if isinstance(el, str):
        print('Это строка')
