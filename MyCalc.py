# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class myCalc(QtGui.QWidget):
	def __init__(self):
		super(myCalc,self).__init__()
		self.body()

	def body(self):
		self.setGeometry(geometry['bodyPosX'],geometry['bodyPosY'],geometry['bodySizeX'],geometry['bodySizeY'])
		#self.MSWindowsFixedSizeDialogHint()
		#self.WindowStaysOnTopHint()
		self.setWindowTitle('Calculator')
		for btn in buttons:
			btn = QtGui.QPushButton(self)
			#btn.setText(buttons[btn['name']]) 
			if buttons[btn]['name'] == '=':
				btn.setGeometry(buttons[btn]['X'],buttons[btn]['Y'],2 * geometry['btnSizeX'] + 10,geometry['btnSizeY'])
				btn.clicked.connect(equalpress)
			else:
				btn.setGeometry(buttons[btn]['X'],buttons[btn]['Y'],geometry['btnSizeX'],geometry['btnSizeY'])
				btn.clicked.connect(btnpress(btn))
		self.lineInput = QtGui.QLineEdit(linput)
		self.lineInput.setGeometry(geometry['LinePosX'], geometry['inLinePosY'], geometry['lineSizeX'], geometry['inLineSizeY'])
		self.lineInput.setText('0')
		self.lineInput.setReadOnly(True)
		self.lineOutput = QtGui.QLineEdit(loutput)
		self.lineOutput.setGeometry(geometry['LinePosX'], geometry['outLinePosY'], geometry['lineSizeX'], geometry['outLineSizeY'])
		self.lineOutput.setText('0')
		self.lineOutput.setReadOnly(True)
		self.show()
	
def main():
	
	
	app = QtGui.QApplication(sys.argv)
	ex = myCalc()
	sys.exit(app.exec_())
	
@QtCore.pyqtSlot()
def btnpress(btn):
	body.self.lineInput.setText(str(buttons[btn])) if body.lineInput.text == '0' else body.self.lineInput.setText(str(body.lineInput.text) + str(buttons[btn]))
@QtCore.pyqtSlot()
def equalpress():
	try:
		varMath = int(body.lineInput.text)
		body.self.lineOutput.setText(str(varMath))
	except:
		body.self.lineInput.setText('Error')  
geometry = {'bodyPosX':50,'bodyPosY':50, 'bodySizeX':440, 'bodySizeY':630, 'btnSizeX':70, 
	'btnSizeY':50, 'lineSizeX':420, 'inLineSizeY':50, 'outLineSizeY':120, 'LinePosX':10,
	'inLinePosY':10, 'outLinePosY':60}
collum1 = 20
collum2 = geometry['btnSizeX'] + 30
collum3 = 2 * geometry['btnSizeX'] + 40
collum4 = 3 * geometry['btnSizeX'] + 50
line1 = geometry['bodySizeY'] - geometry['btnSizeY'] - 20
line2 = geometry['bodySizeY'] - 2 * geometry['btnSizeY'] - 30
line3 = geometry['bodySizeY'] - 3 * geometry['btnSizeY'] - 40
line4 =	geometry['bodySizeY'] - 4 * geometry['btnSizeY'] - 50
buttons = {'zero':{'name':'0','X':collum1, 'Y':line1},\
			'one':{'name':'1','X':collum1, 'Y':line2},\
			'two':{'name':'2','X':collum2, 'Y':line2},\
			'three':{'name':'3','X':collum3, 'Y':line2},\
			'four':{'name':'4','X':collum1, 'Y':line3},\
			'five':{'name':'5','X':collum2, 'Y':line3},\
			'six':{'name':'6','X':collum3, 'Y':line3},\
			'seven':{'name':'7','X':collum1, 'Y':line4},\
			'eight':{'name':'8','X':collum2, 'Y':line4},\
			'nine':{'name':'9','X':collum3, 'Y':line4},\
			'equal':{'name':'=','X':collum2, 'Y':line1},\
			'plus':{'name':'+','X':collum4, 'Y':line2},\
			'minus':{'name':'-','X':collum4, 'Y':line1},\
			'divvy':{'name':'/','X':collum4, 'Y':line3},\
			'multiply':{'name':'+','X':collum4, 'Y':line4}} 	
if __name__ == '__main__':
	main()
	
	
