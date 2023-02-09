import pygame
import os
import modules.button as draw
pygame.init()
pygame_window = pygame.display.set_mode((600,600))
pygame_name = pygame.display.set_caption("GIMN UKRAINE!")
class Image:
    def __init__(self):
        self.x = 150
        self.y = 150
        self.h = 300
        self.w = 300
        self.img = os.path.join(os.path.abspath(__file__ + "/.."),"image/gimn.png")
        self.img = pygame.image.load(self.img)
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
class sound:
        def __init__(self):
                self.music = os.path.join(os.path.abspath(__file__+"/.."),"sounds/ukraine.wav")
                self.music = pygame.mixer.music.load(self.music)
                self.music = pygame.mixer.music.play()
second = draw.button(x=0,y=300,w=600,h=300,c=(255,255,0))
def Play():
    game = True
    pygame_time = pygame.time.Clock()
    sound()
    while game == True:
        pygame_window.fill((255,255,255))
        draw.but1.draw(pygame_window)
        second.draw(pygame_window)
        pygame_window.blit(Image().img,(Image().x,Image().y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        pygame.display.flip()
        pygame_time.tick(50)
Play()