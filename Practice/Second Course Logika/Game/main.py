import pygame #Подключение pygame
import os #Подключение os
import json #Подключение json
#Начинаем работу с кодом
pygame.init() #Дополнительные возможности pygame
card_width = 190 #Ширмна карт
card_height = 320 #Высота карт
step = 10 #Не знаю как это назвать, поэтому назову перемещение
# config = {
#             "screen_width": 680,
#             "screen_height": 480
#         }
config = dict() #Переменая использующии dict
#Создание конфига в папку json
def createJson(name_json, name_dict): #Функция создания конфига
    abspath_main_dir = os.path.join(os.path.abspath(__file__ + "/.."), "json") #Использование директорие в папку json
    print("Абсолютный путь к дириктории игры:", abspath_main_dir) #Проверка правильности директорие
    os.chdir(abspath_main_dir) #Перемещение в директорию
    with open(name_json, "w") as file: #Способ открытие файла
        json.dump(name_dict, file, ensure_ascii= False, indent= 4)#Действие файла

def createDict(name_json, name_dict): #Функция создание директории
    abspath_json_file = os.path.join(os.path.abspath(__file__ + "/.."), "json/" + name_json) #Использование директории в папку json
    print("1:", abspath_json_file) #Проверка на работу файла
    with open(abspath_json_file, "r") as file: #Способ открытие файла
        name_dict = json.load(file) #подгрузка конфига
    return name_dict #Возращение имени директории

# createJson("config.json", config)
config = createDict("config.json", config) #Создание конфига

win = pygame.display.set_mode((config["screen_width"], config["screen_height"])) #Разрешение взятых из конфига
win.fill((0, 100, 0)) #Цвет фона

button1 = pygame.Rect(config["screen_width"]//2 - 75, config["screen_height"]//2 - 25, 150, 50)#Кнопка

font1 = pygame.font.Font(None, 25) #Размер шрифта
text_win_size1 = font1.render("1024x820", True, (255,255,255)) #Текст
class Card: #Класс карт
    def __init__(self, width = None, height = None, x = None, y = None, name_img = None): #Ширина, высота, вертикально, горизонтально, название картинки и все из них None
        self.WIDTH = width #Ширина
        self.HEIGHT = height #Высота
        self.X = x #Горизонтально
        self.Y = y #Вертикально
        self.NAME_IMG = name_img #Имя картинки
        self.IMAGE = None #Картинка 
    def load_img(self): #Функция подгрузок картинок
        path_img = os.path.join(os.path.abspath(__file__+"/.."), self.NAME_IMG) #Добавление директории с помощью os
        self.IMAGE = pygame.image.load(path_img) #Возможность добавлять картинку
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))#Возможность сменить ширину и высоту
list_cards = list() #Список карт
#Создания карт
def create_card(): #Функция карт
    x = (config["screen_width"] // 2) - (card_width * 2) + (step * 1.5)  #Переменная для создания горизонтальной позиции
    #y = config["screen_height"] // 2 + step
    for card in range(4): #4 повторении
        cards = Card(width = card_width, #Ширина #Начало свойства
                    height = card_height, #Высота
                    x = x, #Горизонтальная позиция
                    y = config["screen_height"] // 2 + step, #y = y #Вертикальная позиция
                    name_img = "image/" + str(card + 1) + ".png" #Название картинки
                    ) #Конец свойства
        list_cards.append(cards) #Добавление в список карт
        list_cards[-1].load_img() #Подгрузка изображения
        x += card_width + step #Передвигание горизонтально при каждой создания свойства
create_card() #Создания 4 карт (вызов функции)
enemy_card = Card( #Начало свойства вражеской карты
            width = card_width, #Ширина
            height = card_height, #Высота
            x = config["screen_width"] // 2 - card_width // 2, #Горизонтальная позиция
            y = (config["screen_height"] - card_height) - step * 40, #y = y #Вертилкальная позиция
            name_img = "image/5.png" #Имя картинки 
            ) #Конец свойства
enemy_card.load_img() #Подгрузка изображение
#Главное для pygame
def run_game(): #Функция для работы игры)
    #Card_one = Card()
    game = True #Переменная с игрою (включен)
    while game: #Игра включена
        #pygame.draw.rect(win, (0,0,0), button1)
        for card in list_cards: #Переиминование
            win.blit(card.IMAGE, (card.X, card.Y)) #Отображение 4 карт
        win.blit(enemy_card.IMAGE,(enemy_card.X, enemy_card.Y)) #Отображение вражеской карты
        for event in pygame.event.get(): #Подключение действии
            if event.type == pygame.QUIT: #Реакция на кнопку закрыть
                game = False #Выключение игры
        #win.blit(text_win_size1, (config["screen_width"]//2 - 25, config["screen_height"]//2- 10))
        pygame.display.flip() #Обновление экрана
run_game() #Запуск игры
#Конец кода