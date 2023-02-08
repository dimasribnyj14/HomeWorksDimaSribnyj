import pygame
pygame.init()
class button:
    def __init__(self,
                    x = None,
                    y = None,
                    w = None,
                    h = None,
                    c = None):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.c = c
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,pygame_window):
        pygame.draw.rect(pygame_window,self.c,self.rect)
but1 = button(x=0,y=0,w=600,h=300,c=(0,0,255))