from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
#QApplication Создает приложение
#QWidget Добавлят окно в приложении
#QPushButton Добавляет кнопку в приложении
#QLabel Добавляет надписи в приложении
#QVBoxLayout Создаёт вертикальную линию для расположение
import random  #Генерирует случайное число
from time import *  #Добавляет модуль время
exe = QApplication([]) #Создает обьект приложение
main_win = QWidget() #Создает окно приложение
main_win.setWindowTitle("Vlan Studio") #Создает название приложение
win = QLabel("!") #Создает надпись приложения
win.setText("Добро пожаловать в магазин от Vlana!") #Меняет надпись приложения
button = QPushButton("Зарегестрироваться") #Создает кнопку приложения
v_line = QVBoxLayout() #Создает вертикальную линию для расположение в приложении
v_line.addWidget(win, alignment = Qt.AlignCenter) #Добавляет вертикальную линию текста
v_line.addWidget(button, alignment = Qt.AlignCenter) #Добавляет вертикальную линию кнопки
main_win.setLayout(v_line) #Показывает вертикальную линию приложения
main_win.move(900, 70) #Направляет окно приложения в конкретной координате
main_win.resize(80, 20) #Изменяет начальное разрешение окна
main_win.show() #Показывает окно приложение
exe.exec_() #Позволяет зыкрыть приложение
#Строки которые не используется в коде приложения
#main_win.hide() #Прячет окно приложение