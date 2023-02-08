import os
import pygame
import all.modules.json_operation as amj # 
#all.modules.
pygame.init()
# 3. После создания файла json комментируем словарь cards_player, он ужесохранен в json файле cards_player.json
#cards_player = dict(
#                    [("WARRIOR", dict([("ELF", dict([("HP", 9), ("ATTACK", 5)]))]))]
#                )
#
path = amj.create_abspath()
#
setting_font = amj.createDict('setting_font.json')
#
setting_card = amj.createDict('setting_cards.json')
#
config = amj.createDict("config.json")
# 1. Тут пишем код создания файла cards_player.json, проверяем его наличие в папке json
#cards_player = amj.createJson('cards_player.json', cards_player)
# 2. Тут пишем код создания словаря cards_player используя функцию createDict, смотрим примеры выше
cards_player_json = amj.createDict('cards_player.json')
#
PATH_FONT = os.path.join(amj.create_abspath(), setting_font["FONT_NAME"])
#
MAIN_FONT = pygame.font.Font(PATH_FONT, setting_font["FONT_SIZE"])
#
class Card:
    #
    def __init__(self, 
                    width = None, 
                    height= None, 
                    x= None, 
                    y= None, 
                    name_img= None,
                    #
                    num_hp = None,
                    num_defense = None,
                    num_attack = None,
                    num_crystal = None

        ):
        self.WIDTH = width #
        self.HEIGHT = height #
        self.X = x #
        self.Y = y #
        self.NAME_IMG = name_img #
        self.IMAGE = None #
        self.NUMBER_CARD = None #
        self.KEY_PRESSED = False #
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) #
        self.NUMBER_HP = self.create_text(cards_player_json["WARRIOR"]["ELF"]["HP"])
        self.NUMBER_DEFENSE = num_defense
        self.NUMBER_ATTACK = num_attack
        self.NUMBER_CRYSTAL = num_crystal
        #
        self.load_img()
    #
    def load_img(self):
        path_img = os.path.join(amj.create_abspath(), self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
    #
    def create_text(self, dict_name):
        text = MAIN_FONT.render(str(dict_name), True, setting_font["FONT_COLOR"])
        return text
#
list_cards = list()
#
def create_cards():
    #
    x = (config["WIDTH"] // 2) - (setting_card["WIDTH"] * 2) - (setting_card["STEP"] * 1.5)
    #
    for num in range(4):
        #
        card = Card(
                        width= setting_card["WIDTH"], #
                        height= setting_card["HEIGHT"], # 
                        x = x, #
                        y= config["HEIGHT"] // 2 + setting_card["STEP"], #
                        name_img= "image/" + str(num + 1) + ".png" #
                    )
        list_cards.append(card) # list_cards[card, card, card, card]
        list_cards[-1].NUMBER_CARD = num + 1 # 
        x += setting_card["WIDTH"] + setting_card["STEP"] #
#
create_cards()
#
enemy_card = Card(
                    width= setting_card["WIDTH"], #
                    height= setting_card["HEIGHT"], #
                    x = config["WIDTH"] // 2 - setting_card["WIDTH"] // 2,
                    y= config["HEIGHT"] // 2 - setting_card["HEIGHT"] - setting_card["STEP"],
                    name_img= "image/1.png"
                )
#