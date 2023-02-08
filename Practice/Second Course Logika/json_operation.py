import json
import os
#Функция "Создание операция с путями"
def create_abspath():
    abspath_main_dir = os.path.abspath(__file__ + "/..") #Возращаем абсолютный путь
    abspath_main_dir = abspath_main_dir.split("\\") #Разбиваем путь на кортеж
    del abspath_main_dir[-1] #Возращаем назад из папки modules
    abspath_main_dir = "\\".join(abspath_main_dir) #Соединяем двух путей вместе (Назад из папки modules)
    return abspath_main_dir #Возращаем результат из функции
#Функция "Создание json файл"
def createJson(name_json, name_dict):
    abspath_main_dir = os.path.join(create_abspath(), "json") # 
    # print("Абсолютный путь к дириктории игры:", abspath_main_dir) #Проверка абсолютного путя к директории файла
    os.chdir(abspath_main_dir) #Меняем текущий каталог
    with open(name_json, "w") as file: #Создание файла
        json.dump(name_dict, file, ensure_ascii= False, indent= 4) #Здесь и создается json файл
#Функция "Создание словаря с помощью json"
def createDict(name_json): #Начало функции
    abspath_json_file = os.path.join(create_abspath(), "json/" + name_json)
    # print("1:", abspath_json_file) #Для проверки операции с путями
    with open(abspath_json_file, "r") as file: #Чтение файла
        name_dict = json.load(file) #Загружаем словарь 
    return name_dict #Возращаем результат из функции
#Конец скрипта