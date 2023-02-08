import os
import pygame
import all.modules.json_operation as amj # Подключаем модуль json_operation и переиминовываем в amj

pygame.init()
# 3. После создания файла json комментируем словарь cards_player, он ужесохранен в json файле cards_player.json
cards_player = dict(
                    [("WARRIOR", dict([("ELF", dict([("HP", 9), ("ATTACK", 5)]))]))]
                )
#Создаем операцию с путями
path = amj.create_abspath()
#Создаем словарь из настройк шрифта
setting_font = amj.createDict('setting_font.json')
#Создаем словарь из настроек карт
setting_card = amj.createDict('setting_cards.json')
#Создаем словарь из настроек запуска игры
config = amj.createDict("config.json")
# 1. Тут пишем код создания файла cards_player.json, проверяем его наличие в папке json

# 2. Тут пишем код создания словаря cards_player используя функцию createDict, смотрим примеры выше

#Создаем директорию шрифта
PATH_FONT = os.path.join(amj.create_abspath(), setting_font["FONT_NAME"])
#Создаем главный шрифт
MAIN_FONT = pygame.font.Font(PATH_FONT, setting_font["FONT_SIZE"])
#Создаем класс карт
class Card:
    #Начало класса
    def __init__(self, 
                    width = None, 
                    height= None, 
                    x= None, 
                    y= None, 
                    name_img= None,
                    #Значение каждых карт
                    num_hp = None,
                    num_defense = None,
                    num_attack = None,
                    num_crystal = None

        ):
        self.WIDTH = width #Ширина
        self.HEIGHT = height #Высота
        self.X = x #Горизонтально
        self.Y = y #Вертикально
        self.NAME_IMG = name_img #Имя картинки
        self.IMAGE = None #Картинка 
        self.NUMBER_CARD = None #Номер карты
        self.KEY_PRESSED = False #Нажато ли на кнопка
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) #Создание коллизией
        self.NUMBER_HP = self.create_text(cards_player["WARRIOR"]["ELF"]["HP"])
        self.NUMBER_DEFENSE = num_defense
        self.NUMBER_ATTACK = num_attack
        self.NUMBER_CRYSTAL = num_crystal
        #Загрузка картнки
        self.load_img()
    #Функция "Загрузка картинки"
    def load_img(self):
        path_img = os.path.join(amj.create_abspath(), self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
    #Функция "Создание текста"
    def create_text(self, dict_name):
        text = MAIN_FONT.render(str(dict_name), True, setting_font["FONT_COLOR"])
        return text
#Создаем список карт
list_cards = list()
#Функция "Создание карт"
def create_cards():
    #Настраиваем горизонталь
    x = (config["WIDTH"] // 2) - (setting_card["WIDTH"] * 2) - (setting_card["STEP"] * 1.5)
    #Четыре раза проделываем эти действия
    for num in range(4):
        #Создаем словарь
        card = Card(
                        width= setting_card["WIDTH"], #Ширина
                        height= setting_card["HEIGHT"], # Высота
                        x = x, #Горизонталь
                        y= config["HEIGHT"] // 2 + setting_card["STEP"], #Вертикаль
                        name_img= "image/" + str(num + 1) + ".png" #Имя картинки
                    )
        list_cards.append(card) # list_cards[card, card, card, card]
        list_cards[-1].NUMBER_CARD = num + 1 # Удаляем ненужное значение из списка
        x += setting_card["WIDTH"] + setting_card["STEP"] #Прибавляем горизонталь с каждого раза
#Создаем карт
create_cards()
#Создаем вражеского словаря
enemy_card = Card(
                    width= setting_card["WIDTH"], #Ширина
                    height= setting_card["HEIGHT"], #Высота
                    x = config["WIDTH"] // 2 - setting_card["WIDTH"] // 2,
                    y= config["HEIGHT"] // 2 - setting_card["HEIGHT"] - setting_card["STEP"],
                    name_img= "image/1.png"
                )
#Конец скрипта