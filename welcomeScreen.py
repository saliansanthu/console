# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\welcomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcomeScreen(object):
    def setupUi(self, welcomeScreen):
        welcomeScreen.setObjectName("welcomeScreen")
        welcomeScreen.resize(1243, 866)
        welcomeScreen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        welcomeScreen.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(welcomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logoView = QtWidgets.QGraphicsView(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoView.sizePolicy().hasHeightForWidth())
        self.logoView.setSizePolicy(sizePolicy)
        self.logoView.setMinimumSize(QtCore.QSize(200, 200))
        self.logoView.setMaximumSize(QtCore.QSize(200, 200))
        self.logoView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.logoView.setStyleSheet("")
        self.logoView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logoView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logoView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logoView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.logoView.setObjectName("logoView")
        self.verticalLayout_2.addWidget(self.logoView)
        self.sortingButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortingButton.sizePolicy().hasHeightForWidth())
        self.sortingButton.setSizePolicy(sizePolicy)
        self.sortingButton.setMinimumSize(QtCore.QSize(200, 50))
        self.sortingButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sortingButton.setFont(font)
        self.sortingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sortingButton.setStyleSheet("border-radius: 10%;\n"
"color: rgb(65, 65, 65);\n"
"background-color: rgb(245, 245, 245);\n"
"")
        self.sortingButton.setObjectName("sortingButton")
        self.verticalLayout_2.addWidget(self.sortingButton)
        self.loginButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QtCore.QSize(200, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("border-radius: 10%;\n"
"color: rgb(65, 65, 65);\n"
"background-color: rgb(245, 245, 245);\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.exitButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(200, 50))
        self.exitButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("border-radius: 10%;\n"
"color: rgb(65, 65, 65);\n"
"background-color: rgb(245, 245, 245);\n"
"\n"
"")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ethStatusView = QtWidgets.QGraphicsView(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ethStatusView.sizePolicy().hasHeightForWidth())
        self.ethStatusView.setSizePolicy(sizePolicy)
        self.ethStatusView.setMinimumSize(QtCore.QSize(50, 50))
        self.ethStatusView.setMaximumSize(QtCore.QSize(50, 50))
        self.ethStatusView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.ethStatusView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ethStatusView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ethStatusView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ethStatusView.setObjectName("ethStatusView")
        self.horizontalLayout_2.addWidget(self.ethStatusView)
        self.verticalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        welcomeScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcomeScreen)
        QtCore.QMetaObject.connectSlotsByName(welcomeScreen)

    def retranslateUi(self, welcomeScreen):
        _translate = QtCore.QCoreApplication.translate
        welcomeScreen.setWindowTitle(_translate("welcomeScreen", "MainWindow"))
        self.sortingButton.setText(_translate("welcomeScreen", "ON"))
        self.sortingButton.setShortcut(_translate("welcomeScreen", "S"))
        self.loginButton.setText(_translate("welcomeScreen", "LOGIN"))
        self.loginButton.setShortcut(_translate("welcomeScreen", "L"))
        self.exitButton.setText(_translate("welcomeScreen", "EXIT"))
        self.exitButton.setShortcut(_translate("welcomeScreen", "Ctrl+Q"))
