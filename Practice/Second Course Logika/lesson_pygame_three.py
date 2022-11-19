# 1. Імпортувати модуль pygame
import pygame
# 2. Імпортувати модуль os
import os
# 3. Імпортувати модуль random
import random
# 4. Ініціалізувати налаштування pygame
pygame.init()
# 5. Створити функцію create_path, що знаходить абсолютний шлях до файлу.
# Застосовуємо модуль os.path та його методи abspath(), join()
def create_path(file):
    return os.path.join(os.path.abspath(__file__+"/.."),file)
# 6. Створити клас Sprite, в методі init задати 5 параметрів зі значенням за замовчуванням None
    # - координата x
    # - координата y
    # - ширина
    # - висота
    # - ім'я зображення
class Sprite:
    def __init__(self,x=None,y=None,width=None,height=None,name_img=None):
        # 7. Задати 7 властивостей:
        # - X 
        # - Y
        # - WIDTH
        # - HEIGHT
        # - NAME_IMG
        # - IMAGE 
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMG = name_img
        self.IMAGE = None
    # 8. Створити метод завантаження зображення до властивості IMAGE
    def load_image(self):
        # - створи змінну path, яка зберігає абсолютний шлях до файлу зображення, застосовуємо функцію create_path
        # - завантажити зображення до всластивості IMAGE
        # - трансформувати збережене в IMAGE зображення до розмірів,
        #   що збережені у властивостях WIDTH, HEIGHT. Та зберегти повторно у властивості IMAGE.
        self.IMAGE = create_path(self.NAME_IMG)
        self.IMAGE = pygame.image.load(self.IMAGE)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
    # 9. Створити метод, що промальовує завантажене зображення із властивості IMAGE, метод приймає один параметр - ігрове вікно
    def blit_sprite(self,play):
        # - застосовуємо метод blit() модуля pygame
        play.blit(self.IMAGE,(self.X,self.Y))
# 8. За класом створюємо ігровое вікно з ім'ям win 
play = pygame.display.set_mode((500,500))
# 9. Задаємо назву ігрового вікна
pygame.display.set_caption("Привет, Николай!")
# 10. Створюємо основну функцію гри run_game:
def run_game():
    # - створюємо метод clock 
    fps = pygame.time.Clock()
    # - створюємо об'єкт класу Sprite з ім'ям sprite,
    sprite = Sprite(0,0,250,250,"nanyat.png")
    sprite.load_image()
    # - задаємо змінну game, що відповідає за роботу циклу  
    game = True
    # - задаємо ігровий цикл while, 
    while game == True:
    # - задаємо умову закриття ігрового вікна,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    # - задаємо фон ігрового вікна (мотод fill)
        play.fill((0,255,80))
    # - задіємо об'єкт sprite і викликаємо його метод blit_sprite(), малюємо зображення на ігровому вікні, в центрі екрану
        sprite.blit_sprite(play)
        fps.tick(random.randint(0,60))
        pygame.display.flip()
    # - задаємо оновлення ігрового екрану
# 11. І найголовніше – викликаємо основну функцію гри
run_game()