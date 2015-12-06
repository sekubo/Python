# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class myClass(QtGui.QWidget):
	def __init__(self):
		super(myClass,self).__init__()
		self.startmyClass()

	def startmyClass(self):
		self.setGeometry(50,50,500,500)
		self.setWindowTitle('MyWindow')
		btn = QtGui.QPushButton('Exit',self)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(btnpress)
		btn.setToolTip('Some Text')
		btn.resize(btn.sizeHint())
		btn.setGeometry(50,50,100,100)
		#btn.move(self.width() -25 /2,450)
		
		self.show()
	
def main():

    app = QtGui.QApplication(sys.argv)
    ex = myClass()
    sys.exit(app.exec_())
@QtCore.pyqtSlot()
def btnpress():
	print('kjsdhfksjdhf')   
if __name__ == '__main__':
    main()