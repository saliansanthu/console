from email.mime import application

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


from welcomeScreen import Ui_welcomeScreen

import sys

class WelcomeScreen(QMainWindow):

    def __init__(self, app):
        super(WelcomeScreen, self).__init__()
        self.ui = Ui_welcomeScreen()
        self.ui.setupUi(self)
        self.app = app
        self.ui.exitButton.clicked.connect(self.onExit)
        self.ui.sortingButton.clicked.connect(self.updateSortingFlag)
        self.sorting_flag = False
        self.updateSortingButton()
        scene = QGraphicsScene(self)
        pixmap = QPixmap("logo.jpg")
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)
    

    def onExit(self):
        self.app.quit()
    
    def updateSortingFlag(self):
        if self.sorting_flag == True:
            self.sorting_flag = False
        else:
            self.sorting_flag = True
        self.updateSortingButton()
    
    def updateSortingButton(self):
        if self.sorting_flag == True:
            self.ui.sortingButton.setText("ON")
            self.ui.sortingButton.setStyleSheet("border-radius: 10%;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        else:
            self.ui.sortingButton.setText("OFF")
            self.ui.sortingButton.setStyleSheet("border-radius: 10%;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen(app)
    window.showFullScreen()
    sys.exit(app.exec())
