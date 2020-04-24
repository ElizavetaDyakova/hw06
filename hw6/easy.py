import os
def make_dir(dirname):
    try:
        #создаем директории
        os.mkdir(dirname)
        print("Данная директория создана")
    except FileExistsError:
        print("Данная директория уже существует")

def remove_dir(dirname):
    try:
        #удаление
        os.rmdir(dirname)
        print('{} удалена'.format(dirname))
    except FileNotFoundError:
        print("Данная директория уже удалена")

#Просмотреть содержимое заданной папки
def files_in_dir(dirname):
    list = os.listdir(dirname)
    for i in list:
        print(i)
#Просмотреть содержимое текущей папки
def files():
    list = os.listdir()
    for i in list:
        print(i)



