# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-

# В большинстве GUI-приложений нам понадобится всего два класса. Это QtCore и QtGui. Модуль QtCore отвечает за обработку сигналов, слотов и за общее управление приложением. Модуль QtGui содержит в себе методы для создания и изменения различных GUI компонентов: окон и виджетов.

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

# Python поддерживает библиотеку стандартных модулей, которые встраиваются в интерпретатор и обеспечивают доступ к операциям, которые не являются частью основного языка. Один из таких модулей - sys, он предоставляет доступ к некоторым переменным и функциям, которые тесно взаимодействуют с интерпретатором. 

class myLCDNumber(QLCDNumber):
  value = 60
  # Следующий метод (слот) вызывется при каждом переполнении таймера  
  @pyqtSlot()
  def count(self):
    self.display(self.value)
    self.value = self.value-1


def main():    
    # нам нужен модуль sys, чтобы передать аргументы командной строки sys.argv в качестве параметра для класса QApplication. Он содержит список аргументов командной строки, передаваемых через Python. 

    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()

    # Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle('PyQt QTimer Секундомер')
    # Обновляем значение времени на форме  
    lcdNumber.display(60)
    timer = QTimer()
    # Связываем сигнал переполнения таймера со слотом
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
    # Задаем время срабатывания таймера (в мс)
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()