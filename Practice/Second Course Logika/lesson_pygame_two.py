# 1. Подключаем модуль pygame
import pygame
# 2. Подключаем модуль os
import os
# 3. Создаем словарь с именем settings_screen, словарь содержит четыре ключа и значения.
# - key "WIDTH" and value 550
# - key "HEIGHT" and value 600
# - key "COLOR" and value (255, 229, 204)
# - key "CAPTION" and value "GAME"
settings_screen = {
                "WIDTH":550,
                "HEIGHT":600,
                "COLOR":(255,229,204),
                "CAPTION":"GAME"
                    }
# 4. Создаем словарь с именем settings_button, словарь содержит четыре ключа и значения.
# - key "WIDTH" and value 150
# - key "HEIGHT" and value 100
# - key "COLOR" and value (255, 169, 0)
# - key "BORDER_COLOR" and value (0,0,0)
# - key "STEP" and value 20
settings_button = {
                "WIDTH":150,
                "HEIGHT":100,
                "COLOR":(255,169,0),
                "BORDER_COLOR":(0,0,0),
                "STEP":20
                }

# 5. Создаем класс Button.
# В скобках методе __init__ задаем 6 аргументов со значением None
# - width 
# - height
# - x
# - y
# - color
# - border_color
class Button:
    def __init__(self,width=None,height=None,x=None,y=None,color=None,border_color=None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.COLOR = color
        self.BORDER_COLOR = border_color
        self.RECT = pygame.Rect(self.X,self.Y,self.WIDTH,self.HEIGHT)
    # Задаем 7 свойств в методе __init__. Свойство RECT задаем используя встроенный класс модуля pygame.Rect().
    # Вспоминаем сколько значений принимает класс Rect или смотрим по ссылке в телеграмм документацию, или заглядываем в свой конспект
    # - WIDTH
    # - HEIGHT
    # - X
    # - Y 
    # - COLOR
    # - BORDER_COLOR
    # - RECT

    # 6. Задаем метод draw_rect(), метод принимает один аргумент - окно игрового экрана
    # Задача вашего метода draw_rect() рисовать рект объекты на экране, используем встроенный модуль draw и его метод rect().
    def draw_rect(self,win):
        pygame.draw.rect(win,settings_button["COLOR"],self.RECT)
        pygame.draw.rect(win,settings_button["BORDER_COLOR"],self.RECT,settings_button["STEP"])


# 8. За классом создаем игровое окно с именем win и размерами, которые берем из словаря 
win = pygame.display.set_mode((settings_screen["WIDTH"], settings_screen["HEIGHT"]))
# 9. Задаем название игровому окну, также обращаемся к словарю
pygame.display.set_caption(settings_screen["CAPTION"])
# 10. Создаем основную функцию игры run_game:
def run_game():
    # - создаем объект класса Button c именем button, задаем значения аргументам - берем из словаря settings_button,
    button = Button(settings_button["WIDTH"],settings_button["HEIGHT"],200,250,settings_button["COLOR"],settings_button["BORDER_COLOR"])
    # - задаем переменную game отвечающую за работу цикла  
    game = True
    # - задаем игровой цикл while, 
    while game == True:
    # - задаем условие закрытия игрового окна,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    # - задаем фон игровому окну (мотод fill), цвет берем из словаря
        win.fill(settings_screen["COLOR"])
    # - задействуем объект button и вызываем его метод draw_rect(), отрисовуем RECT на игровом окне, в центре экрана
        button.draw_rect(win)
        
        
    # - задаем обновление игрового экрана
        pygame.display.flip()
# 11. И самое главное - вызываем основную функцию игры


run_game()