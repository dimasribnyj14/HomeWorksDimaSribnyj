import random 
win = 0
human = 0
pc = 0
n = 0
h = 0
p = 0
print("Привіт людино!")
a = input("Давай пограэмо в камінь-ножиці-бумага(1 - Давай , 2 - не хочу)")
if a == 2:
    print("Гаразд, пока")
while a == "1":
        print("Розпочнемо насчет 3")
        print("1")
        print("2")
        human = int(input("3 (1 - Камінь , 2 - ножиці , 3 - бумага)"))
        if human == 1 or human == 2 or human == 3:
            n = 1
        if human == 1:
            print("Ви обрали камінь.")  
        if human == 2:
            print("Ви обрали ножиці.") 
        if human == 3:
            print("Ви обрали бумагу.")
        pc = random.randint(1,3)
        if pc == 1:
            print("Компьютер вибрав камінь.") 
        if pc == 2:
            print("Компьютер вибрав ножиці.")
        if pc == 3:
            print("Компьютер вибрав бумагу.")
        if human == pc:
            win = 0
        if human == 1 and pc == 2:
            win = 1
        if human == 1 and pc == 3:
            win = 2 
        if human == 2 and pc == 1:
            win = 2
        if human == 2 and pc == 3:
            win = 1 
        if human == 3 and pc == 1:
            win = 1
        if human == 3 and pc == 2:
            win = 2
        if win == 0:
            print("Ничья!")
        if win == 1:
            print("Виграла людина!")
            h=h+1
        if win == 2:
            print("Виграв компьютер!")
            p=p+1
        a = input("Продовжим грати?(1 - Давай , 2 - не хочу)") 
        if n >= 1 and a == "1":
            n = n + 1   
        print("Дякую за гру, рахунок:", "Людина", h, "-", p, "Компьютер")   
