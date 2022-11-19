# 1. Імпортувати модуль pygame
import pygame
# 2. Імпортувати модуль os
import os
# 3. Імпортувати модуль random
import random
# 4. Імпортувати модуль lesson_pygame_four_3settings
import lesson_pygame_four_settings as settings
import lesson_pygame_four_dict as dictgame
# 5. Ініціалізувати налаштування pygame
pygame.init()
# 6. Створити клас Sprite, який наслідує клас Settings з модуля lesson_pygame_four_settings
class Sprite(settings.Settings):
    # 7. Створюємо метод __init__ та наслідуємо параметри класу Батька, використовуємо метод super()
    def __init__(self, x, y, width, height, name_img):
        super().__init__(x, y, width, height, name_img)
    # 8. Створюємо метод gravity, що змушує спрайт рухатись вниз, працюємом з координатою Y, 
    # не забуваємо змінювати як координату Y зображення так і координту Y властивості RECT 
    def gravity(self):
        if not self.Y >= 405:
            self.Y += 1

sprite = Sprite(700/2,700/2,150,200,"1.png")
# 7. Створити об'єкт класу Sprite, з ім'ям sprite