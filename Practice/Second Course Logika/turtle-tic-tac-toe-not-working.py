from turtle import*
hideturtle()
pensize(5)
speed(0)
#Отрисовка поля
def field():
    penup()
    goto(-200,200)
    pendown()
    #Отрисовка квадрата
    for i in range(4):
        forward(390)
        right(90)
    #Отрисовка клеточек
    for i in range(2):
        forward(130)
        right(90)
        forward(390)
        left(180)
        forward(390)
        right(90)
    left(180)
    forward(260)
    for i in range(2):
        left(90)
        pendown()
        forward(130)
        left(90)
        forward(390)
        left(180)
        forward(390)

field()

def numbering():
    penup()
    goto(-190,75)
    write("1", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(-60,75)
    write("2", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(70,75)
    write("3", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(-190,-55)
    write("4", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(-60,-55)
    write("5", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(70,-55)
    write("6", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(-190,-185)
    write("7", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(-60,-185)
    write("8", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
    goto(70,-185)
    write("9", move = False, align = "left", font = ( "Arial", 20, "normal" ) )
numbering()
color("red")
for i in range(9):
    move = input("Введите номер клетки")
    def cross():
        if move == "1":
            penup()
            goto(-195,75)
            pendown()
            goto(-75,195)
            penup()
            goto(-195,195)
            pendown()
            goto(-75,75)
        if move == "2":
            penup()
            goto(-65,195)
            pendown()
            goto(55,75)
            penup()
            goto(-65,75)
            pendown()
            goto(55,195)
        if move == "3":
            penup()
            goto(65,195)
            pendown()
            goto(185,75)
            penup()
            goto(65,75)
            pendown()
            goto(185,195)
        if move == "4":
            penup()
            goto(-195,65)
            pendown()
            goto(-75,-55)
            penup()
            goto(-195,-55)
            pendown()
            goto(-75,65)
        if move == "5":
            penup()
            goto(55,65)
            pendown()
            goto(-65,-55)
            penup()
            goto(55,-55)
            pendown()
            goto(-65,65)
        if move == "6":
            penup()
            goto(185,65)
            pendown()
            goto(65,-55)
            penup()
            goto(185,-55)
            pendown()
            goto(65,65)
        if move == "7":
            penup()
            goto(-195,-65)
            pendown()
            goto(-75,-185)
            penup()
            goto(-195,-185)
            pendown()
            goto(-75,-65)
        if move == "8":
            penup()
            goto(-65,-65)
            pendown()
            goto(55,-185)
            penup()
            goto(-65,-185)
            pendown()
            goto(55,-65)
        if move == "9":
            penup()
            goto(65,-65)
            pendown()
            goto(185,-185)
            penup()
            goto(65,-185)
            pendown()
            goto(185,-65)
    cross()    













exitonclick()