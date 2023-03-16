import random
rightkey = []
code = []
for i in range(random.randint(0,100)):
    randomcode = random.randint(10000,99999)
    code.append(randomcode)
keyrandom = random.randint(10000,99999)
rightkey.append(keyrandom)
print(rightkey)
goto = int(input("Введите свой код для подтверждение получение кодов других людей (обязательно иметь [23853]):"))
if goto == rightkey:
    print("Ключи других пользователей:", code)
else:
    print("Вы вели неправильный ключ, значит вы не являетесь администратором!")
