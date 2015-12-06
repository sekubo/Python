#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui


class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
        QtCore.QObject.connect(self.button[r][c], QtCore.SIGNAL("clicked()"), self.revealButtonWrapper )
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setStyleSheet("background-color: rgb(130, 130, 0); color: rgb(0,255,0)")
        
#-----------------------------------------------------
  def disableAll(self):
    for r in range(16):
      for c in range(16):
        self.button[r][c].setEnabled(False)
        self.button[r][c].setFlat(True)
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def revealButtonWrapper(self):
    if self.gamestarted == 0:
      self.time.start()
      self.timer.start(100)
      self.gamestarted = 1
    button = self.sender()
    self.revealButton( button )
#-----------------------------------------------------
  def revealButton(self, button):
    if button.bomb == True:
      txt = "X"
      color = QtGui.QColor.fromRgb(255,0,0)
      self.timer.stop()
      self.disableAll()
    else:
      txt = str( self.grepSurroundingBombCount(button.row, button.col) )
      color = QtGui.QColor.fromRgb(0,0,255)

    button.revealed = True
    button.setText(txt)
    button.setFlat(True)
    button.setEnabled(False)
    
    button.setPalette(QtGui.QPalette(color))
    if txt == "0":
      for r,c in self.grepSurroundingLocation(button.row, button.col):
        if self.button[r][c].revealed == False:
          self.revealButton( self.button[r][c] )
#-----------------------------------------------------
  def grepSurroundingBombCount(self, row, col):
    count = 0
    tmp = self.grepSurroundingLocation(row,col)
    for r,c in self.grepSurroundingLocation(row,col):
      count = count + 1 if self.button[r][c].bomb == True else count
    return(count)
#-----------------------------------------------------
  def grepSurroundingLocation(self, row, col):
    """
    Grep all the surrounding cells, and
    return back the location in a list of [row,col]
    format. e.g:-
    [ [row,col], [r,c], [r,c] ....]
    """
    ret = []
    top = row-1
    bot = row+1
    left = col-1
    right = col+1
    ### Getting top 3 cells if available
    if top > -1:
      ret.append( [top, col] )      # Top
    if bot < 16:
      ret.append( [bot, col] )      # Bot
    if left > -1:
      ret.append( [row, left] )     # Left
    if right < 16:
      ret.append( [row, right] )    # Right
    if top > -1 and left > -1:
      ret.append( [top, left] )   # UpperLeft
    if top > -1 and right < 16:
      ret.append( [top, right] )  # UpperRight
    if bot < 16 and left > -1:
      ret.append( [bot, left] )   # LowerLeft
    if bot < 16 and right < 16:
      ret.append( [bot, right] )  # LowerRight
    return(ret)
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
#__________________________________________________________________________
#__________________________________________________________________________