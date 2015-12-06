# -*- coding: utf-8 -*-
'''
Game: Mine Sweeper.
'''
import sys
from PyQt4 import QtCore, QtGui

class ErrorWindow(QtGui.QWidget):
    '''
    Start game settings.
    '''
    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle('!!! ERROR !!!')
        label = QtGui.QLabel(varTransit, self)
        label.move(15, 10)
        self.show()

def main(errorType):
    global varTransit
    varTransit = errorType
    mapp = QtGui.QApplication(sys.argv)
    runapp = ErrorWindow()
    sys.exit(mapp.exec_())


if __name__ == "__main__":
    main('errorType')
  
