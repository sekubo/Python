# -*- coding: utf-8 -*-
'''
Game: Mine Sweeper.
'''
import sys
import os
import random
import Miner_error
import Miner
from PyQt4 import QtCore, QtGui

class StartWindow(QtGui.QWidget):
    '''
    Start game settings.
    '''
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setWindowTitle('Miner')
        self.setGeometry(100, 100, 400, 150)
        #self.setSizeConstraint(QWidget.setFixedSize)
        layout = QtGui.QGridLayout()
        settingLayout = QtGui.QGridLayout()
        buttonLayout = QtGui.QGridLayout()
        layout.addLayout(settingLayout, 0, 0)
        layout.addLayout(buttonLayout, 1, 0)

        self.bombQuantity = QtGui.QLineEdit('40')
        self.bombQuantity.setAlignment(QtCore.Qt.AlignRight)
        font = self.bombQuantity.font()
        font.setPointSize(font.pointSize() + 8)
        self.bombQuantity.setFont(font)
        self.bombQuantity.setMaxLength(3)
        settingLayout.addWidget(QtGui.QLabel(u'Введите желаемые параметры для игры в "САПЕРА":'), 0, 1, 1, 3)
        settingLayout.addWidget(QtGui.QLabel(u'Количество бомб:'), 1, 0)
        settingLayout.addWidget(self.bombQuantity, 1, 1)
        settingLayout.addWidget(QtGui.QLabel(',        '), 1, 2)
        settingLayout.addWidget(QtGui.QLabel(u'Размер игрового поля:'), 1, 3)
        self.fieldSize = QtGui.QLineEdit('16')
        self.fieldSize.setAlignment(QtCore.Qt.AlignRight)
        self.fieldSize.setFont(font)
        self.fieldSize.setMaxLength(2)
        settingLayout.addWidget(self.fieldSize, 1, 4)
        
        startgameButton = QtGui.QPushButton('Start')
        quitButton = QtGui.QPushButton('Cancel')
        QtCore.QObject.connect(startgameButton, QtCore.SIGNAL('clicked()'), self.clickedStartButton)
        QtCore.QObject.connect(quitButton, QtCore.SIGNAL("clicked()"), QtCore.QCoreApplication.instance().quit)
        buttonLayout.addWidget(startgameButton, 0, 0)
        buttonLayout.addWidget(quitButton, 0, 1)
        
        self.setLayout(layout)
        
        self.show()
        
    def clickedStartButton(self):
        fild = self.fieldSize.text()
        bomb = self.bombQuantity.text()
        if not (fild.isdigit() and bomb.isdigit()):
            Miner_error.main(u'Вы ввели не правильные параметры для игры. Попробуйте еще раз')
        elif int(fild) ** 2 <= 2 * int(bomb):
            Miner_error.main(u'Количество бомб превышает 50% ячеек от заданого поля')
        else:
            Miner.main(fild , bomb)

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartWindow()
    sys.exit(app.exec_())
    