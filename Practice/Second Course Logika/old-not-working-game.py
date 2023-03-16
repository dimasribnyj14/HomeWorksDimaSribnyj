import pygame
from time import *
from random import *
pygame.init()

clock=pygame.time.Clock()
bg=pygame.image.load("%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F_%3F%3F%3F%3F%3F%3F%3F_%3F%3F%3F%3F%3F%3F_%3F%3F%3F%3F (1).png")
back=(79,79,79)

mw=pygame.display.set_mode((800,800))


class Area():
    def __init__(self,x,y,width,height,color,speed=0):
        self.rect=pygame.Rect(x,y,width,height)
        self.fill_color=color
        self.speed=speed
    def color(self,new_color):
        self.fill_color=new_color
    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image=pygame.font.SysFont("verdana",fsize).render(text,True,text_color)
    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        mw.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
class Picture(Area):
    def __init__(self,filename,x,y,width,height,speed):
        Area.__init__(self,x=x,y=y,width=width,height=height,speed=speed,color=None)
        self.image=pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))           

Green=(0,255,0)
Red=(255,0,0)
Knight=Picture("png-transparent-digital-art-knight-pixel-text-fictional-character-technology (1).png",250,350,1,1,3)
Enemy=Picture("scale_1200.png",250,150,1,1,1)
Enemy1=Picture("scale_1200 (1).png",250,150,1,1,1.5)
Enemy2=Picture("scale_1200 (2).png",375,-50,1,1,2)
Enemy3=Picture("png-transparent-mario-bros-luigi-goomba-8-bit-mario-angle-heroes-text.png",250,150,1,1,1)
Enemy4=Picture("scale_1200.png",250,150,1,1,1.5)
Enemy5=Picture("Без названия.png",250,50,1,1,1)
Enemy6=Picture("187-1875808_squashed-goomba-super-mario-goomba-8-bit (1).png",250,150,1,1,0.5)
Enemy7=Picture("187-1875808_squashed-goomba-super-mario-goomba-8-bit.png",250,150,1,1,1.5)
Over=Label(0,0,500,500,Red)
Enemies=list()
Enemies.append(Enemy)
Over.set_text("GAME OVER!",100)
Win=Label(0,0,500,500,Green)
Win.set_text("Win!",100)
move_d=False
move_a=False
move_s=False
move_w=False
timestop=True
res=True
level=1
start_time=time()       
while res and level<9:
    mw.blit(bg,-10,-10)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                move_d=True
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                move_a=True    
            if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                move_s=True
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                move_w=True    
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                move_d=False
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                move_a=False   
            if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                move_s=False
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                move_w=False        
    if timestop:
        if move_d:
            Knight.rect.x+=Knight.speed 
        if move_a:
            Knight.rect.x-=Knight.speed
        if move_w:
            Knight.rect.y-=Knight.speed
        if move_s:
            Knight.rect.y+=Knight.speed
        if Knight.rect.x<=0:
            Knight.rect.x+=Knight.speed
        if Knight.rect.x>=430:
            Knight.rect.x-=Knight.speed
        if Knight.rect.y>=430:
            Knight.rect.y-=Knight.speed            
    Knight.draw() 
    for i in Enemies:
        if i!=Enemy4:
            i.draw()   
        if i.rect.x<Knight.rect.x:
            i.rect.x+=i.speed
        if i.rect.x>Knight.rect.x:
            i.rect.x-=i.speed
        if i.rect.y<Knight.rect.y:
            i.rect.y+=i.speed    
        if i.rect.y>Knight.rect.y:
            i.rect.y-=i.speed
        if i==Enemy3:
            end_time=time()
            if end_time-start_time>=1:
                i.rect.x=randint(10,490)
                i.rect.y=randint(10,490)  
                start_time=time()   
        if i==Enemy4:
            end_time=time()
            if end_time-start_time>=3:
                i.draw()
                start_time=time()
        if i==Enemy5:
            end_time=time()
            if end_time-start_time>=5 and timestop==True:
                start_time=time()
                timestop=False
            if end_time-start_time>=3 and timestop==False:
                start_time=time() 
                timestop=True 
        if i==Enemy6:
            end_time=time()
            if end_time-start_time>=1.5:
                Enemy6.speed+=0.5
                start_time=time()   
        if i==Enemy7:
            end_time=time()
            if end_time-start_time>=1.5:
                if Knight.rect.x>=Enemy7.rect.x:
                    Knight.rect.x-=10
                else:
                    Knight.rect.x+=10
                if Knight.rect.y>=Enemy7.rect.y:
                    Knight.rect.y-=10
                else:
                    Knight.rect.y+=10       
                start_time=time()

        if abs(Knight.rect.x-i.rect.x)<50 and abs(Knight.rect.y-i.rect.y)<=60 :
            Over.draw(50,200)  
            res=False  
            pygame.display.update()
            clock.tick(40)           
    if Knight.rect.y<=0:
        if level==1:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy1)
            Enemies.remove(Enemy)
            level+=1
        elif level==2:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy2)
            Enemies.remove(Enemy1)
            level+=1
        elif level==3:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy3)
            Enemies.remove(Enemy2)
            level+=1
        elif level==4:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy4)
            Enemies.remove(Enemy3)
            Enemy4.draw()
            level+=1
        elif level==5:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy5)
            Enemies.remove(Enemy4)
            level+=1
        elif level==6:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy6)
            Enemies.remove(Enemy5)
            level+=1
        elif level==7:
            Knight.rect.x=250
            Knight.rect.y=400
            Enemies.append(Enemy7)
            Enemies.remove(Enemy6)
            level+=1   
        elif level==8:
            level+=1                     
    pygame.display.update()
    clock.tick(40) 
if level>=9:
    Win.draw(200,200) 
pygame.display.update()
clock.tick(40)                        

