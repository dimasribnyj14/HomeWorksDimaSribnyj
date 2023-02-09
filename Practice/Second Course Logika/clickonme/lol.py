import pygame
import os
pygame.init()
click_time = pygame.time.Clock()
#check = os.path.join(os.path.abspath(__file__ + "/.."), "image/" + "what.jpg")
clicker = pygame.display.set_mode((300,300))
pygame.display.set_caption("CLICK ME PLS!!!")
clicker.fill((255,255,255))
#clicker = pygame.display.set_icon(check)
class CLICK_ME:
    def __init__(self):
        self.w = 300
        self.h = 300
        self.x = 0
        self.y = 0
        self.image = os.path.join(os.path.abspath(__file__ + "/.."), "image/" + "what.png")
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
class CLICKED:
    def __init__(self):
        self.w = 300
        self.h = 300
        self.x = 0
        self.y = 0
        self.image = os.path.join(os.path.abspath(__file__ + "/.."), "image/" + "clicked.png")
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
class CLICK_ME_SOUND:
    def __init__(self):
        self.music = os.path.join(os.path.abspath(__file__+"/.."), "sound/" + "click.wav")
        self.music = pygame.mixer.music.load(self.music)
        self.music = pygame.mixer.music.play()
class CLICK_SOUND:
    def __init__(self):
        self.music = os.path.join(os.path.abspath(__file__+"/.."), "sound/" + "button.wav")
        self.music = pygame.mixer.music.load(self.music)
        self.music = pygame.mixer.music.play()
class THANKS_SOUND:
    def __init__(self):
        self.music = os.path.join(os.path.abspath(__file__+"/.."), "sound/" + "thanks.wav")
        self.music = pygame.mixer.music.load(self.music)
        self.music = pygame.mixer.music.play()
def Play():
    clicking_me = False
    CLICKME = CLICK_ME()
    CLICK = CLICKED()
    you_clicking = True
    time = 0
    while you_clicking == True:
        clicker.blit(CLICKME.image,(CLICKME.x,CLICKME.y))
        time += 1
        if time >= 100:
            print("CLICK ME!")
            CLICK_ME_SOUND()
            time = 0
        for event in pygame.event.get(): #Переиминование
            if event.type == pygame.QUIT: #Если нажать на кнопку закрыть, игра закроется
                you_clicking = False
            elif event.type == pygame.K_ESCAPE: #Если нажать на клавиатуре кнопку Escape, игра закроется (Не работает)
                you_clicking = False
            if event.type == pygame.MOUSEBUTTONDOWN: #Если нажать на кнопку, кнопка нажимется и игра отблагодарит вам за нажатие.
                clicking_me = True
                clicker.blit(CLICK.image,(CLICK.x,CLICK.y))
                THANKS_SOUND()

                print("THANK YOU!")
            if event.type == pygame.MOUSEBUTTONUP: #Я не знаю, работает ли это или нет.
                clicker.blit(CLICKME.image,(CLICKME.x,CLICKME.y))
        click_time.tick(20)
        pygame.display.flip()
Play()