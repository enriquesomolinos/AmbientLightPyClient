__author__ = 'Waldo'

import ui
from logger import log
from PyQt4 import QtGui, QtCore

class TitleBar(QtGui.QFrame):
    def __init__(self, *args):
        super(TitleBar, self).__init__(*args)
        self.ui = ui.Ui_TitleBar()
        self.handle = self.ui.setupUi(self)

        self.toolbarClicked = False

        # Set drop shadow on title text
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        self.ui.titleLabel.setGraphicsEffect(dropShadowEffect)
        
        log.info("TitleBar setup!")

    def on_closeButton_clicked(self, *args):
        if not args:
            self.window().close()

    def on_minimizeButton_clicked(self, *args):
        if not args:
            self.window().setWindowState(QtCore.Qt.WindowMinimized)

    def mousePressEvent(self, e):
        self.toolbarClicked = (e.button() == QtCore.Qt.LeftButton)
        if self.toolbarClicked:
            window = self.window()
            posInWindow = self.mapTo(window, self.pos())
            self.tbMouseStart = (e.x() + posInWindow.x(), e.y() + posInWindow.x())

    def mouseReleaseEvent(self, e):
        if self.toolbarClicked and e.button() == QtCore.Qt.LeftButton:
            self.toolbarClicked = False

    def mouseMoveEvent(self, e):
        if self.toolbarClicked:
            self.window().move(e.globalX() - self.tbMouseStart[0], e.globalY() - self.tbMouseStart[1])