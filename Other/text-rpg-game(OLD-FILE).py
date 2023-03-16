#Hello, this is my code
import random #Activates the random number
print("TEXT RPG FREE TRIAL") #The Name Of The Game
class RPG(): #Class RPG()
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage
    def INPUT(self):
        going = 0
        walking = True
        enemies = False
        wait = input("Where we need to go?")
        if wait == "left":
            while walking == True:
                randomed = random.randint(0,10)
                if randomed != 5:
                    print("-----------------------")
                    going += 1
                else:
                    print("You meet a enemy")
                    walking = False
                    enemies = True
                    print("You went", going, "KM")
        if wait == "right":
            while walking == True:
                randomed = random.randint(0,10)
                if randomed != 5:
                    print("-----------------------")
                    going += 1
                else:
                    print("You meet a enemy")
                    walking = False
                    enemies = True
                    print("You went", going, "KM")
    def ENEMY(self):
        lucky = random.randint(1,3)
        health = random.randint(10,50)
        damage = random.randint(10,50)
        going = random.randint(0,1090)
        health_enemy = health
        running = 0
        walk = True
        gold = random.randint(0,1000)
        while_fight = True
        sec_fight = 0
        damage_enemy = damage
        feed = input("What you do?")
        if feed == "run":
            while walk == True:
                if going != 5:
                    print("RUNNING")
                    running += 1
                if lucky == 1:
                    print("You're lucky because enemy lost you while you running away")
                    print("You runned", running,"KM")
                    walk = False
                elif lucky == 2:
                    health = 0
                    print("You're dead!")
                    print("You runned", running,"KM")
                    walk = False
                else:
                    health = 50
                    print("You got hurt but you escaped!")
                    print("You runned", running,"KM")
                    walk = False
                    wait = input("Where we need to go?")
        elif feed == "fight":
            while while_fight == True:
                lucky_fight = random.randint(1,3)
                if lucky_fight == 1:
                    print("Continue on fighting")
                    sec_fight += 1
                elif lucky_fight == 2:
                    print("You killed him!")
                    print("You got", gold, "Money's")
                    while_fight = False
                else:
                    health = 0
                    print("You're dead!")
                    while_fight = False
name = input("Whats your name?")
health = random.randint(100,1000)
money = random.randint(0,10000)
Heroes = RPG(name,health,money)
print("Your Name:", name)
print("Your Health:", health)
print("Your Money:", money)
Heroes.INPUT()
Heroes.ENEMY()
