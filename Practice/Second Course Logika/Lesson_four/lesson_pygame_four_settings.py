# 1. Імпортувати модуль pygame
import pygame
# 2. Імпортувати модуль os
import os
# 3. Імпортувати модуль random
import random
# 4. Ініціалізувати налаштування pygame
pygame.init()
# 5. Створити функцію create_path, що знаходить абсолютний шлях до файлу. Приймає один параметр - name_file
# Застосовуємо модуль os.path та його методи abspath(), join(). Не забуваємо, що функція нічого не зберігає 
# і потрібно повертати результат, а саме знайденний шлях до вашего файлу.
def create_path():
    path = os.path.abspath(__file__ + "/..") 
    return path

# 6. Створити клас Sprite, в методі init задати 6 параметрів зі значенням за замовчуванням None
    # - координата x
    # - координата y
    # - ширина
    # - висота
    # - ім'я зображення
    # - колір рект об'єкту
class Settings:
    def __init__(self,x = None, y = None, width = None, height = None, name_img = None):
        # 7. Задати 8 властивостей:
        # - X 
        # - Y
        # - WIDTH
        # - HEIGHT
        # - NAME_IMG
        # - IMAGE
        # - RECT
        # - COLOR
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMG = name_img
        self.IMAGE = None
        self.RECT = pygame.Rect(self.X,self.Y,self.WIDTH,self.HEIGHT)
        self.COLOR = (255,169,0)
    # 8. Створити метод завантаження зображення до властивості IMAGE
    def load_image(self):
        # - створи змінну path, яка зберігає абсолютний шлях до файлу зображення, застосовуємо функцію create_path
        # - завантажити зображення до всластивості IMAGE
        # - трансформувати збережене в IMAGE зображення до розмірів,
        #   що збережені у властивостях WIDTH, HEIGHT. Та зберегти повторно у властивості IMAGE.
        path_img = create_path()
        path_img = os.path.join(path_img, self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
    # 9. Створити метод, що промальовує завантажене зображення із властивості IMAGE, метод приймає один параметр - ігрове вікно
    def blit_sprite(self,win):
        # - застосовуємо метод blit() модуля pygame
        win.blit(self.IMAGE,(self.X,self.Y))
    # 10. Створити метод draw_rect(), що промальовує рект об'єкти
    # метод приймає один параметр - об'єкт ігрового вікна.
    def draw_rect(self,win):
        #pygame.draw.rect(win,self.COLOR,self.RECT)
        #Работает
        pass