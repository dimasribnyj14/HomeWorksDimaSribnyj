from random import randint
from turtle import *
from time import sleep
shape('turtle')
speed(0)
color('red')
penup()
t=200
to=-200
def idti():
    goto(randint(to,t),randint(to,t))
def poimaet(x, y):
    write('You Win!', font=('Arial Black', 10, 'normal'))
    hideturtle()
onclick(poimaet)
while True:
    sleep(0.5)
    left(99999999)
    idti()
exitonclick()