#Начало скрипта
import random #Подключает модуль рандом
randoming = random.randint(10000,99999) #Делает случайное число (или же в современном названо рандом) так от 10000, так от 99999
logika = { #Создает список состоящии с ключом имени и паролем
    "name":["Ярик","Ростик","Дима"], #Ключ имени
    "password":[22866,11111,66600] #Ключ пароля
} #Конец списка
print(logika["name"]) #Выводит из списка ключа имя
print(logika["password"]) #Выводит из списка ключа пароль
logika["name"].append("Богдан") #Добавляет нового участника под имени "Богдан"
logika["password"].append(randoming) #Дает ему случайное число (или же в современном названо рандом) Богдану
print(logika) #Показывает всех ключи из списка
print("Вот все участники с их паролем.")
#Конец скрипта
#Строки которые я хотел добавить но не добавил
#names = random.randint(0,2)
#if names == 1:
#   logika["name"].append("Вадим")
#   logika["password"].append(randoming)
#if names == 2:
#   logika["name"].append("Глеб")
#   logika["password"].append(randoming)
#if names == 0:
#   logika["name"].append("Богдан")
#   logika["password"].append(randoming)