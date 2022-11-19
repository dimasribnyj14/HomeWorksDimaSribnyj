import pygame
import os
#
pygame.init()
#
dict_setting_window = {
    "WIDTH": 500,
    "HEIGHT": 500,
    "COLOR": (128,0,128),
    "CAPTION": "One",
    "FPS": 60
}
#
dict_setting_window2 = {
    "WIDTH": 500,
    "HEIGHT": 500,
    "COLOR": (175,238,238),
    "CAPTION": "Two",
    "FPS": 60
}
dict_setting_window3 = {
    "WIDTH": 500,
    "HEIGHT": 500,
    "COLOR": (0,255,128),
    "CAPTION": "Three",
    "FPS": 60
}
#
dict_font = {
    "FONT_SIZE": 100,
    "TEXT": "Гра",
    "COLOR_TEXT": (0,0,0)
}
#
dict_font_end = {
    "FONT_SIZE": 20,
    "TEXT": "Ви пройшли гру! Натисніть на кнопку, щоб закрити!",
    "COLOR_TEXT": (255,255,255)
}
#
class Button:
    def __init__(self, width = None, height = None, x = None, y = None, color= (255,255,0)):
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.X = x
        self.Y = y
        self.FONT = pygame.font.Font(None, dict_font["FONT_SIZE"])
        self.BUT_CAPTION = self.FONT.render(dict_font["TEXT"], True, dict_font["COLOR_TEXT"])
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
    #
    def blit_button(self, win):
        pygame.draw.rect(win, self.COLOR, self.RECT)
        win.blit(self.BUT_CAPTION, (self.X + self.WIDTH // 4, self.Y + self.HEIGHT // 3))
class Button_End:
    def __init__(self, width = None, height = None, x = None, y = None, color= (51,255,153)):
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.X = x
        self.Y = y
        self.FONT = pygame.font.Font(None, dict_font_end["FONT_SIZE"])
        self.BUT_CAPTION = self.FONT.render(dict_font_end["TEXT"], True, dict_font_end["COLOR_TEXT"])
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
    #
    def blit_button(self, win):
        pygame.draw.rect(win, self.COLOR, self.RECT)
        win.blit(self.BUT_CAPTION, (self.X + self.WIDTH // 4, self.Y + self.HEIGHT // 3))
#
def window_three():
    #
    win = pygame.display.set_mode((dict_setting_window3["WIDTH"], dict_setting_window3["HEIGHT"]))
    #
    pygame.display.set_caption(dict_setting_window3["CAPTION"])
    #
    clock = pygame.time.Clock()
    #
    game = True
    button_game3 = Button_End(
        width= dict_setting_window3["WIDTH"] // 2, #
        height= dict_setting_window3["HEIGHT"] // 2, #
        x = dict_setting_window3["WIDTH"] // 6 - dict_setting_window3["WIDTH"] // 6, #
        y = dict_setting_window3["HEIGHT"] // 2 - dict_setting_window3["HEIGHT"] // 4 #
    )
    while game:
        #
        win.fill(dict_setting_window3["COLOR"])
        #
        button_game3.blit_button(win)
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # 
                #
                if button_game3.RECT.collidepoint(x,y):
                    game = False
        clock.tick(dict_setting_window3["FPS"])
        pygame.display.flip()
def window_two():
    #
    win = pygame.display.set_mode((dict_setting_window2["WIDTH"], dict_setting_window2["HEIGHT"]))
    #
    pygame.display.set_caption(dict_setting_window2["CAPTION"])
    #
    clock = pygame.time.Clock()
    #
    button_game2 = Button(
        width= dict_setting_window2["WIDTH"] // 2, #
        height= dict_setting_window2["HEIGHT"] // 2, #
        x = dict_setting_window2["WIDTH"] // 2 - dict_setting_window2["WIDTH"] // 4, #
        y = dict_setting_window2["HEIGHT"] // 2 - dict_setting_window2["HEIGHT"] // 4 #
    )
    #
    game = True
    while game:
        #
        win.fill(dict_setting_window2["COLOR"])
        #
        button_game2.blit_button(win)
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # 
                #
                if button_game2.RECT.collidepoint(x,y):
                    game = False
                    #
                    window_three()
        clock.tick(dict_setting_window2["FPS"])
        pygame.display.flip()
#
def window_one():
    #
    win = pygame.display.set_mode((dict_setting_window["WIDTH"], dict_setting_window["HEIGHT"]))
    #
    pygame.display.set_caption(dict_setting_window["CAPTION"])
    #
    clock = pygame.time.Clock()
    #
    button_game = Button(
        width= dict_setting_window["WIDTH"] // 2, #
        height= dict_setting_window["HEIGHT"] // 2, #
        x = dict_setting_window["WIDTH"] // 2 - dict_setting_window["WIDTH"] // 4, #
        y = dict_setting_window["HEIGHT"] // 2 - dict_setting_window["HEIGHT"] // 4 #
    )
    #
    game = True
    while game:
        #
        win.fill(dict_setting_window["COLOR"])
        #
        button_game.blit_button(win)
        #
        for event in pygame.event.get():
            #
            if event.type == pygame.QUIT:
                game = False
            #
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # 
                #
                if button_game.RECT.collidepoint(x,y):
                    game = False
                    #
                    window_two()
        #
        clock.tick(dict_setting_window["FPS"])
        #
        pygame.display.flip()
#
window_one()
