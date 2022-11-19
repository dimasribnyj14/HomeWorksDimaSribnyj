# 1. Імпортувати модуль pygame
import pygame
# 2. Імпортувати модуль os
import os
# 3. Імпортувати модуль random
import random
#    Імпортувати модуль lesson_pygame_four_settings
import lesson_pygame_four_settings as settings
#    Імпортувати модуль lesson_pygame_four_area
import lesson_pygame_four_area as area
#    Імпортувати модуль lesson_pygame_four_dict
import lesson_pygame_four_dict as dictgame
import lesson_pygame_four_sprite as sprite
# 4. Ініціалізувати налаштування pygame
pygame.init()
# 5. Створюємо ігровое вікно з ім'ям win 
win = pygame.display.set_mode((dictgame.main_settings_dict["WIDTH"],dictgame.main_settings_dict["HEIGHT"]))
# 6. Задаємо назву ігрового вікна
pygame.display.set_caption(dictgame.main_settings_dict["CAPTION"])
# 7. Створюємо основну функцію гри run_game:
def run_game():
    game = True
    time = pygame.time.Clock()
    # - задаємо змінну game, що відповідає за роботу циклу  
    while game:
    # - задаємо ігровий цикл while, 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    # - задаємо умову закриття ігрового вікна,
        win.fill(dictgame.main_settings_dict["COLOR"])
    # - задаємо фон ігрового вікна (мотод fill)
        sprite.sprite.load_image()
        sprite.sprite.blit_sprite(win)
    # - задіємо об'єкт sprite і викликаємо його метод blit_sprite(), малюємо зображення на ігровому вікні, в центрі екрану  по ширині але по висоті 0
        sprite.sprite.draw_rect(win)
        sprite.sprite.gravity()    # - задіємо об'єкт area і викликаємо його метод draw_rect(), малюємо зображення на ігровому вікні, в центрі екрану
        area.area.draw(win)
    # - задаємо оновлення ігрового екрану
        pygame.display.flip()
        time.tick(60)
# 8. І найголовніше – викликаємо основну функцію гри
run_game()