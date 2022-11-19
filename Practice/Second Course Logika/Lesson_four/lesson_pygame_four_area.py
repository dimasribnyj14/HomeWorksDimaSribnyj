# 1. Імпортувати модуль pygame
import pygame
# 2. Імпортувати модуль os
import os
# 3. Імпортувати модуль random
import random
# 4. Імпортувати модуль lesson_pygame_four_settings
import lesson_pygame_four_settings as settings
import lesson_pygame_four_dict as dictgame
# 5. Ініціалізувати налаштування pygame
pygame.init()
# 6. Створити клас Area, який наслідує клас Settings з модуля lesson_pygame_four_settings
class Area(settings.Settings):
    def __init__(self, x, y, width, height,color = None,border = None):
        super().__init__(x, y, width, height)
        self.X_one = x
        self.Y_one = y
        self.WIDTH_one = width
        self.HEIGHT_one = height
        self.COLOR = color
        self.BORDER = border
        self.DRAW = None
        self.RECT_one = pygame.Rect(self.X_one,self.Y_one,self.WIDTH_one,self.HEIGHT_one)
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,self.RECT_one)

area = Area(200,600,300,100,(255,169,0),20)
# 7. Створити об'єкт класу Area, з ім'ям area