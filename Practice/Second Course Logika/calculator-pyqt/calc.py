from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                            QLabel,
                            QPushButton,
                            QVBoxLayout,
                            QWidget,
                            QMessageBox,
                            QHBoxLayout,
                            QDesktopWidget,
                            QRadioButton,
                            QGroupBox,
                            QToolBox
)
from PyQt5.QtGui import QFont
#QApplication Создает приложение
#QWidget Добавлят окно в приложении
#QPushButton Добавляет кнопку в приложении
#QLabel Добавляет надписи в приложении
#QVBoxLayout Создаёт вертикальную линию для расположение
#QHBoxLayout Создаёт горизонтальную линию для расположение
#QMessageBox Создаёт всплывающее окно
#QRadioButton создаёт кнопки с вариантами
#QGroupBox создаёт контейнер кнопок
#QDesktopWidget имеет окно с разрешением
#QToolBox это многостраничные виджеты. Каждая страница -- это подчиненный виджет.
exe = QApplication([]) #Создает обьект приложение
class MyWidget(QWidget): #Создаём класс виджета для расположение и разрешение экрана
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 350) #Создаёт своё разрешение экрана
    def center(self): #Функция отвечает за расположение на экране
        screen_geometry1 = QDesktopWidget().screenGeometry() #Записывается в переменные добавление геометрии окна
        widget = self.geometry() #Записывается в переменные параметры нашего окна
        x = screen_geometry1.width() // 2 - widget.width() // 2 #Определяет x
        y = screen_geometry1.height() // 2 - widget.height() // 2 #Определяет y
        self.move(x,y) #Перемещение окно в координаты x, y
app = MyWidget() #Создаёт экземпляр класса
app.center() #Вызывает фунцкию из класса
app.setWindowTitle("CalcStudio") #Называем приложение по своему
number_list=[] #Создаёт список кнопок
def settingButton(name,x,y,color):# Функция настроек кнопок
    name.setMaximumWidth(x)
    name.setMinimumHeight(y)
    name.setStyleSheet('background-color: '+color)
def NumberButton(): #Создаёт функцию для номеров
    for num in range(10): #Десять раз работает
        button = QPushButton(str(num)) #Создает кнопку с цифрами
        settingButton(button,50,50,'light')
        number_list.append(button) #Добавляет цифру в список
NumberButton() #Активирует функцию из 29 строке
push_plus = QPushButton("+") #Кнопка увеличение
push_minus = QPushButton("-") #Кнопка уменшение
push_multiply = QPushButton("*") #Кнопка умножение
push_division = QPushButton("/") #Кнопка деления
push_float = QPushButton(",") #Кнопка дроби
push_equal = QPushButton("=") #Кнопка равенства
push_CE = QPushButton("CE") #Кнопка CE
push_C = QPushButton("C") #Кнопка C
push_percent = QPushButton('%') #Кнопка процента
push_plus_minus = QPushButton('+/-') #
text_result = QLabel('0')
text_result.setAlignment(Qt.AlignRight)
# Шрифт 
font = QFont()
font.setFamily('Arial')
font.setPointSize(28)
text_result.setFont(font)
############################################
settingButton(push_C,50,50,'orange')
settingButton(push_CE,50,50,'orange')
settingButton(push_division,50,50,'gray')
settingButton(push_equal,50,50,'gray')
settingButton(push_float,50,50,'gray')
settingButton(push_plus,50,50,'gray')
settingButton(push_minus,50,50,'gray')
settingButton(push_multiply,50,50,'gray')
settingButton(push_percent,50,50,'gray')
settingButton(push_plus_minus,50,50,'gray')
#################################################
num_list = [] #Список значений введённых с калькулятора
do_list = [push_C,push_CE,push_division,push_equal,push_float,push_minus,push_multiply,push_percent,push_plus,push_plus_minus]
#################################################
class OnClick(MyWidget):
    def __init__(self,number_list,text_result):
        super().__init__()
        self.number_list = number_list #Список с кнопками,добавляем в класс
        self.text_result = text_result #добавляем в класс результат вычислений
        self.do_list = do_list #Список с действиями добавляем в класс
        self.point = 0 #счётчик для цикла
    def NumberButtonClick(self): #Функция для подключения кнопок на окно
        for point in range(10): #цыкл подключения кнопок
            self.number_list[point].clicked.connect(self.res) #Подключаем кнопки из списка с кноп
            self.do_list[point].clicked.connect(self.res) #подключаем кнопки из списка с действием
            point+=1 #добавляем к счётчику 1
    def number(self, num):
        if len(num_list) == 0:
            num_list.append(num)
            text_result.setText(num_list[0]) 
        elif len(num_list) == 1:
            num_list[0] += num
            print(num_list[0])
            text_result.setText(num_list[0]) 
        elif len(num_list) == 2:
            num_list.append(num)
            text_result.setText(num_list[2])             
        elif len(num_list) == 3:
            num_list[2] += num
            print(num_list[2])
            text_result.setText(num_list[2])         
    def res(self, x): #функция обработки сигналов с нажатия кнопки
        num = str(self.sender().text()) #записываем в переменную в виде строки
        result = 0 
        if num == '1':
            self.number(num)
        if num == '2':
            self.number(num)
        if num == '3':
            self.number(num)
        if num == '4':
            self.number(num)
        if num == '5':
            self.number(num)
        if num == '6':
            self.number(num)
        if num == '7':
            self.number(num)
        if num == '8':
            self.number(num)
        if num == '9':
            self.number(num)
        if num == '0':
            self.number(num)
        if num == '+' or num =='-' or num == '*' or num =='/':  
            text_result.setText(num)
            num_list.append(num)
        if num == '=':  
            if num_list[1] == "+":
                result = int(num_list[0]) + int(num_list[2])
                text_result.setText(str(result))
            elif num_list[1] == '-':
                result = int(num_list[0]) - int(num_list[2])
                text_result.setText(str(result))
            elif num_list[1] == '*':
                result = int(num_list[0]) * int(num_list[2])
                text_result.setText(str(result))
            elif num_list[1] == '/':
                if num_list[2] == 0:
                    text_result.setText('Devision by zero')
                    del num_list[-1]
                elif num_list[2] != 0 :
                    result = int(num_list[0]) / int(num_list[2])
                    text_result.setText(str(result))
        elif num == 'C':
            num_list.clear()
            text_result.setText('0')
        elif num == 'CE':
            if len(num_list) != 0:
                del num_list[-1]
                text_result.setText('0')            
buttons = OnClick(number_list,text_result)
buttons.NumberButtonClick()
#Layout требуется для размещение кнопок
layout1 = QHBoxLayout() #Создает горизонтальные линие для расположение
layout2 = QHBoxLayout() #Создает горизонтальные линие для расположение
layout3 = QHBoxLayout() #Создает горизонтальные линие для расположение
layout4 = QHBoxLayout() #Создает горизонтальные линие для расположение
layout5 = QHBoxLayout() #Создает горизонтальные линие для расположение
group_layout = QGroupBox() #Создаёт контейнер виджетов
#На горизонт создаёт кнопки C, CE
layout1.addWidget(push_C)
layout1.addWidget(push_CE)
layout1.addWidget(push_percent)
layout1.addWidget(push_plus_minus)
#Следующие будут создавать кнопки 1, 2, 3, минус
layout2.addWidget(number_list[1])
layout2.addWidget(number_list[2])
layout2.addWidget(number_list[3])
layout2.addWidget(push_minus)
#Далее будут тоже самое, только с другими кнопками, такие как 4, 5, 6, плюс
layout3.addWidget(number_list[4])
layout3.addWidget(number_list[5])
layout3.addWidget(number_list[6])
layout3.addWidget(push_plus)
#Предпоследнее будет как и прошлые, только тоже другие кнопки, такие как 7, 8, 9 и равно
layout4.addWidget(number_list[7])
layout4.addWidget(number_list[8])
layout4.addWidget(number_list[9])
layout4.addWidget(push_equal)
#Последнее будет создавать особенные кнопки по сравнению с прошлыми такие как 0, кома (,), отделение и умножение
layout5.addWidget(number_list[0])
layout5.addWidget(push_float)
layout5.addWidget(push_division)
layout5.addWidget(push_multiply)
#Создание layout с вертикальной линие
v_groupbox_layout = QVBoxLayout()
v_groupbox_layout.addLayout(layout1)
v_groupbox_layout.addLayout(layout2)
v_groupbox_layout.addLayout(layout3)
v_groupbox_layout.addLayout(layout4)
v_groupbox_layout.addLayout(layout5)
#Создаёт вертикальные линие
v_main = QVBoxLayout()
#Добавление группу в вертикальной линие
v_main.addWidget(text_result)
group_layout.setLayout(v_groupbox_layout)
v_main.addWidget(group_layout)
app.setLayout(v_main)
app.show()
exe.exec_()