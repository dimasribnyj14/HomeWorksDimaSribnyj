import pygame
import os
import json

pygame.init()

card_width = 200
card_height = 320
step = 20
#Настройка шрифта в виде словаря
setting_font = {
    "FONT_SIZE": 60,
    "FONT_NAME": "font/dialog.otf",
    "FONT_COLOR": (255,255,255)
}
#Карты игрока в словаре
cards_player = dict(
                    [("WARRIOR", dict([("ELF", dict([("HP", 9), ("ATTACK", 5)]))]))]
                )
#Проверка карт в json
print(json.dumps(cards_player, indent=4))
#Добавляем шрифт с настройками
PATH_FONT = os.path.join(os.path.abspath(__file__ + "/.."), setting_font["FONT_NAME"])
MAIN_FONT = pygame.font.Font(PATH_FONT, setting_font["FONT_SIZE"])
# config = {
#             "screen_width": 680,
#             "screen_height": 480
#         }
config = dict()
#Создание функции для создания json
def createJson(name_json, name_dict):
    abspath_main_dir = os.path.join(os.path.abspath(__file__ + "/.."), "json")
    print("Абсолютный путь к дириктории игры:", abspath_main_dir)
    os.chdir(abspath_main_dir)
    with open(name_json, "w") as file:
        json.dump(name_dict, file, ensure_ascii= False, indent= 4)
#Создания функции для создание словаря
def createDict(name_json, name_dict):
    abspath_json_file = os.path.join(os.path.abspath(__file__ + "/.."), "json/" + name_json)
    print("1:", abspath_json_file)
    with open(abspath_json_file, "r") as file:
        name_dict = json.load(file)
    return name_dict
#Создание  словаря
config = createDict("config.json", config)
#Настраивание разрешение
win = pygame.display.set_mode((config["screen_width"], config["screen_height"]))
#Создание класса Card
class Card:
    #Первая главная функция
    def __init__(self, 
                    width = None, 
                    height= None, 
                    x= None, 
                    y= None, 
                    name_img= None,
                    #Игровое свойства карт
                    num_hp = None,
                    num_defense = None,
                    num_attack = None,
                    num_crystal = None

        ):
        self.WIDTH = width #Ширина
        self.HEIGHT = height #Высота
        self.X = x #Горизонталь
        self.Y = y #Вертикаль
        self.NAME_IMG = name_img #Имя картинки
        self.IMAGE = None #Картинка
        self.NUMBER_CARD = None #Номер карты
        self.KEY_PRESSED = False #Проверка нажатия
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) #Коллизия
        self.NUMBER_HP = self.create_text(cards_player["WARRIOR"]["ELF"]["HP"])
        self.NUMBER_DEFENSE = num_defense
        self.NUMBER_ATTACK = num_attack
        self.NUMBER_CRYSTAL = num_crystal
        #Прогрузка изображение
        self.load_img()
        #Конец первой функции
         
    #Прогрузку и настроки изображение и текста
    def load_img(self):
        path_img = os.path.join(os.path.abspath(__file__ + "/.."), self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
    def create_text(self, dict_name):
        text = MAIN_FONT.render(str(dict_name), True, setting_font["FONT_COLOR"])
        return text
#Список карт
list_cards = list()
#Функция создание карт
def create_cards():
    #Переменная горизонтали
    x = (config["screen_width"] // 2) - (card_width * 2) - (step * 1.5)
    # 4 Раза создаем карты
    for num in range(4):
        #Свойства карты
        card = Card(
                        width= card_width, # Ширина
                        height= card_height, # Высота
                        x = x, #Горизонтально
                        y= config["screen_height"] // 2 + step, #Вертикально
                        name_img= "image/" + str(num + 1) + ".png" #Название картинки
                    )
        list_cards.append(card) # list_cards[card, card, card, card] Добавляет карты в список
        list_cards[-1].NUMBER_CARD = num + 1 #Добавление остальных информацих в списке
        x += card_width + step #Каждая карта будет левее
#Использование функции и создание карт
create_cards()
#Свойства вражеской карты
enemy_card = Card(
                    width= card_width,
                    height= card_height,
                    x = config["screen_width"] // 2 - card_width // 2,
                    y= config["screen_height"] // 2 - card_height - step,
                    name_img= "image/1.png"
                )
#Прогрузка картинки
enemy_card.load_img()
#Функция для работы игры
def run_game():
    #Игра работает
    game = True
    while game:
        #Заливка
        win.fill((128, 0, 255))
        #Показываем карты
        for obj in list_cards:
            win.blit(obj.IMAGE, (obj.X, obj.Y))
            win.blit(obj.NUMBER_HP, (obj.X, obj.Y))
        #Показываем вражескую карту
        win.blit(enemy_card.IMAGE, (enemy_card.X, enemy_card.Y))
        #Используем клавиши и переименоваем из pygame.event.get() в event
        for event in pygame.event.get():
            #Если нажимаем на выход, игра закрывается
            if event.type == pygame.QUIT:
                game = False
            #Если нажато на левую кнопку мыши, то происходит реакция
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # точка нажатия, ее координаты х и у
                #Переименивоваем из list_cards в card
                for card in list_cards:
                    #Если карта дотронулся до карты
                    if card.RECT.collidepoint(x,y):
                        #то происходит реакция
                        print(f"Карта {card.NUMBER_CARD} нажат")
            #Если нажато на кнопку мышки, то происходит реакция
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            # Создать условие которое определяет какая клафиша мыши была нажата.
            # Обращаю ваше внимание, что event.button отвечает за фиксацию нажатия кнопки любой мыши
            # Нужно только создать условие, которое фиксирует нажатие мыши, а далее вывести на экран 
            # значение которое храниться в событии button и вы узнаете, какая цифра относится к нажатой
            # кнопке мыши
            
        #Обновление экрана
        pygame.display.flip()
#Запуск игры
run_game()