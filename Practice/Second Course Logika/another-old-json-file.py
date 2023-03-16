import json
import os 
dict_users = {}
dict_users1 = dict()
dict_users = {'name':'Dima','surname':'Sribnyj'}
print(dict_users)
#Создаем файл json и записываем его в new_json 
new_json = json.dumps(dict_users,indent=4)
print(new_json)
#Обратно в словарь сделали из json 
dict_users = json.loads(new_json)
print(dict_users)
#Добавили ещё 2 ключа в словарь dict_users
dict_users['login'] = 'SmirnovRoman123'
#Перезаписываем файл json и записываем в него dict_users
new_json = json.dumps(dict_users,indent=4)
print(new_json)
# Записываем абсолютный путь в переменную
path1 = os.path.join(os.path.abspath(__file__+'/..'))
os.chdir(path1) # передаем абсолютный путь в директиву(изменяя её)
#Создаем файл json в папке 
with open('New_JSon1','w') as file:
    json.dump(dict_users,file,indent=4)
with open('New_JSon1',"r") as file: # Открываем файл json в строку
    dict_users = json.load(file)
    print(dict_users)