"""
Задание №4.
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый, как остаток от деления
суммы цифр id на семь
"""

import random
from classwork_3 import *


class Worker(People):
    __workers_id = []

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.__worker_id = None
        self.__secure_lvl = None

    @property
    def worker_id(self) -> int:
        if self.__worker_id is None:
            temp = random.randint(100000, 999999)
            while temp in Worker.__workers_id:
                temp = random.randint(100000, 999999)
            self.__worker_id = temp
            Worker.__workers_id.append(temp)
        return self.__worker_id

    @property
    def secure_lvl(self) -> int:
        if self.__secure_lvl is None:
            temp = sum((int(i) for i in str(self.worker_id))) % 7
            self.__secure_lvl = temp
        return self.__secure_lvl


if __name__ == '__main__':
    man = Worker(first_name=input('Введите имя: '),
                 second_name=input('Введите фамилию: '),
                 age=int(input('Введите возраст: ')))

    # man.birthday()
    # print(f'{man.first_name} празднует день рождения, исполнилось {man.age}')
    # man.full_name()
    # man.birthday()
    # man.birthday()
    # print(man.age)
    man.full_name()
    print(f'Идентификационный номер: {man.worker_id}')
    print(f'Уровень доступа: {man.secure_lvl}')
