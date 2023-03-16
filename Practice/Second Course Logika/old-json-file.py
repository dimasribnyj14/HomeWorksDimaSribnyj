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
dict_users1 = json.loads(new_json)
print(dict_users1)
#Добавили ещё 2 ключа в словарь dict_users
dict_users['age'] = 12
new_json = json.dumps(dict_users1, indent = 4)
#Перезаписываем файл json и записываем в него dict_users
new_json = json.dumps(dict_users,indent=4)
print(new_json)
# Записываем абсолютный путь в переменную
path1 = os.path.join(os.path.abspath(__file__+'/...'))
os.chdir(path1) #передаем абсолютный путь в директиву(изменяя её)
#Создаем файл json в папке 
with open('Old_Json1','w') as file:
    json.dump(dict_users1,file,indent=4)
with open('Old_Json1.json',"q") as file: #Открываем файл json в строку
    dict_users2 = json.load(file)
    print(dict_users2)