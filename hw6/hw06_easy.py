
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
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

try:
     #создаем директории
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except FileExistsError:
        print("Данная директория уже существует")
#пауза чтобы увидеть директории в папке
a = input("Директории созданы, введите что-нибудь ")
print(a)
try:
    #удаление
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except FileNotFoundError:
    print("Данная директория уже удалена")
print("Директории удалены ")
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

list = os.listdir()
for i in list:
    print(i)

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
try:
    shutil.copy('hw06_easy.py', 'copy.py')
    print('Копия создана')
except FileNotFoundError:
    print('Файл не найден')
except FileExistsError:
    print('Файл уже существует')