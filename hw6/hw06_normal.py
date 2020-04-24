# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """

    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print('Некорректное значение')




# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
from easy import make_dir, remove_dir, files_in_dir, files


# print(sys.argv)

def main():
    while True:
        print('''1 Перейти в папку
2 Просмотреть содержимое текущей папки
3 Удалить папку
4 Создать папку
5 Выйти''')
        task = input()
#Перейти в папкуty
        if task == '1':
            dirname = input('Введите имя директории: ')
            try:
                os.chdir(dirname)
                print('Вы перешли в {}'.format(dirname), os.getcwd())
            except FileNotFoundError:
                print('Такого файла не существует!')

#Просмотреть содержимое текущей папки
        elif task == '2':
            print(os.getcwd(), files())

#Удалить папку
        elif task == '3':
            dirname = input('Введите имя директории: ')
            remove_dir(dirname)

#Создать папку
        elif task == '4':
            dirname = input('Введите имя директории: ')
            make_dir(dirname)

        elif task == '5':
            break
main()