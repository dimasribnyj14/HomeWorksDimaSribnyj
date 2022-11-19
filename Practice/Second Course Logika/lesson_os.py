# 1. Подключаем модуль os 
# 2. Подключаем модуль json
# 3. Подключаем модуль pygame
import os
import json
import pygame
#
pygame.init()
# 3. Создаем функцию с именем search_path, задача которой 
# находить абсолютный путь к файлу. Задайствуем такие методы модуля os как:
# - os.path.abspath()
# - os.path.join()
# - работаем с list
def search_path(file):
    return os.path.join(os.path.abspath(__file__+"/.."),file)
    #List = list()
# 4. Создаем класс с именем Sprite, методе __init__ задаем 5 параметров со значением None (аргументов)
# и соответсвенно 5 свойств:
# - свойство ширины
# - свойство высоты
# - свойство координаты х
# - свойство координаты y
# - свойство имени изображения, которое будем загружать в проект
# - свойство картинки, где будем сохранять загруженную картинку
class Sprite:
    def __init__(self, width = None, height = None, x = None, y = None, name_image = None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_IMAGE = name_image
        self.IMAGE = None

# 5. В классе Sprite после метода __init__ создаем метод загрузки изображения, 
# где для поиска пути к файлу картинки вызываем ранее созаднную функцию search_path,
# обязательно трансформирую картинку под размеры ширины и высоты заданные в свойствах.
    def load_image(self):
        #self.IMAGE = os.path.join(os.path.abspath(__file__+"/.."),self.NAME_IMAGE)
        self.IMAGE = search_path(self.NAME_IMAGE)
        self.IMAGE = pygame.image.load(self.IMAGE)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))

# 6. В классе Sprite после метода load_image создаем метод отрисовки спрайта на игровом экране
# В методе обязательно задаем параметр, который принимает значение объекта игрового экрана
# Для отрисовки спрайта используем метод blit(), обязательно передаем три параметра.  
    def blit_sprite(self,window):
        window.blit(self.IMAGE,(self.X,self.Y))

# 7. Вне класса создаем словарь с именем settings_screen c тремя ключами:
# WIDTH и его значением 500
# HEIGHT и его значением 500
# COLOR и его значением (сами выберите свой RGB цвет)
# CAPTION и его значением "GAME"
settings_screen = {
    "WIDTH":500,
    "HEIGHT":500,
    "COLOR":(20,255,30),
    "CAPTION":"GAME"
}
# 8. За классом создаем игровое окно с размерами, которые берем из словаря 
window = pygame.display.set_mode((settings_screen["WIDTH"],settings_screen["HEIGHT"]))
# 9. Задаем название игровому окну, также обращаемся к словарю
pygame.display.set_caption(settings_screen["CAPTION"])
# 10. Создаем основную функцию игры run_game:
def run_game():
    sprite = Sprite(500,400,0,50,"just a image.jpg")
# - создаем объект класса Sprite c именем sprite, задаем значения для свойст, 
    sprite.load_image()
# - задействуем объект sprite и вызываем его метод load_image, загружаем картинку к нашему объекту
    game = True
# - задаем игровой цикл, 
    while game == True:
# - задаем условие закрытия игрового окна,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False    
# - задаем фон игровому окну (мотод fill), цвет берем из словаря
        window.fill(settings_screen["COLOR"])
# - задействуем объект sprite и вызываем его метод blit_sprite, отрисовуем спрайт на игровом окне
        sprite.blit_sprite(window)
# - задаем обновление игрового экрана
        pygame.display.flip()
# 11. И самое главное - вызываем основную функцию игры
run_game()