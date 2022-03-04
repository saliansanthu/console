from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QDialog
from PyQt5.QtGui import QPixmap
from loginForm import Ui_loginWindow


from welcomeScreen import Ui_welcomeScreen

import sys

class WelcomeScreen(QMainWindow):

    def __init__(self, app):
        super(WelcomeScreen, self).__init__()
        self.ui = Ui_welcomeScreen()
        self.ui.setupUi(self)
        self.app = app
        self.sorting_flag = False
        self.ethernet_status = True
        self.ui.exitButton.clicked.connect(self.onExit)
        self.ui.sortingButton.clicked.connect(self.updateSortingFlag)
        self.ui.loginButton.clicked.connect(self.onLoginClick)
        self.setLogo()
        self.updateSortingButton()
        self.updateEthernetStatus()
        
        
    def setLogo(self):
        scene = QGraphicsScene(self)
        pixmap = QPixmap("logo.png")
        pixmap = pixmap.scaled(200, 200)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.logoView.setScene(scene)
    

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
        else:
            self.ui.sortingButton.setText("OFF")

    def updateEthernetStatus(self):
        scene = QGraphicsScene(self)
        if self.ethernet_status == True:
            pixmap = QPixmap("eth_up.png")
            self.ui.sortingButton.setHidden(False)
            self.ui.loginButton.setHidden(False)
        else:
            pixmap = QPixmap("eth_down.png")
            self.ui.sortingButton.setHidden(True)
            self.ui.loginButton.setHidden(True)

        pixmap = pixmap.scaled(50, 50)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.ethStatusView.setScene(scene)

    def onLoginClick(self):
        class LoginScreen(QDialog):
            def __init__(self):
                super(LoginScreen, self).__init__()
                self.ui = Ui_loginWindow()
                self.ui.setupUi(self)
                self.setWindowFlags( Qt.FramelessWindowHint | self.windowFlags())
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.setWindowOpacity(0.9)
                self.ui.exitButton.clicked.connect(self.onExit)
            
            def onExit(self):
                self.close()
        
        win = LoginScreen()

        win.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen(app)
    window.showFullScreen()
    sys.exit(app.exec())
