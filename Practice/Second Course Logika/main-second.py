import pygame
import os
import json
import all.modules.cards as amc
import all.modules.json_operation as amj

pygame.init()
#Начинаем запускать игру
def run_game():
    #Создаем словарь из json файла
    config = amj.createDict("config.json")
    #Настраиваем разрешение
    win = pygame.display.set_mode((config["WIDTH"], config["HEIGHT"]))
    game = True
    while game:
        #Заливаем окно краской
        win.fill((128, 0, 255))
        #Отображаем карты
        for obj in amc.list_cards:
            win.blit(obj.IMAGE, (obj.X, obj.Y))
            win.blit(obj.NUMBER_HP, (obj.X, obj.Y))
        #Отображаем вражескую карту
        win.blit(amc.enemy_card.IMAGE, (amc.enemy_card.X, amc.enemy_card.Y))
        #Используем действия и переименовываем
        for event in pygame.event.get():
            #Если нажать на крестик, игра закроется
            if event.type == pygame.QUIT:
                game = False
            #Если нажать на левую кнопку мышки то произойдет действия
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # точка нажатия, ее координаты х и у
                #Переименовываем в card
                for card in amc.list_cards:
                    #Если нажатая мышка дотрагивается до карт то произойдет действия
                    if card.RECT.collidepoint(x,y):
                        #Проверка нажатие
                        print(f"Карта {card.NUMBER_CARD} нажат")
            #Заканчиваем действия
        #Обновляем экран
        pygame.display.flip()
#Запускаем игру
run_game()