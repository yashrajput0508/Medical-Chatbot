# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(800, 600)
        Form1.setMinimumSize(QtCore.QSize(800, 600))
        Form1.setMaximumSize(QtCore.QSize(800, 600))
        Form1.setStyleSheet("#topPanel { background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"\n"
"\n"
"\n"
"#label{color: rgb(0,0, 0);}\n"
"\n"
"#bottomPanel{background-image: url(images/bc1.jpg);}\n"
"\n"
"\n"
"#loginForm\n"
"{\n"
"  background: rgba(0, 0, 0, 80);\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"#yes{color:white;}\n"
"#no{color:white;}\n"
"#label_2{color:white;}\n"
"#restart:hover{background-color:blue;}\n"
"#quit:hover{background-color:blue;}\n"
"#submit:hover{background-color:lightblue;}")
        self.topPanel = QtWidgets.QWidget(Form1)
        self.topPanel.setGeometry(QtCore.QRect(0, 0, 800, 81))
        self.topPanel.setObjectName("topPanel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.topPanel)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.bottomPanel = QtWidgets.QWidget(Form1)
        self.bottomPanel.setGeometry(QtCore.QRect(-1, 79, 801, 521))
        self.bottomPanel.setObjectName("bottomPanel")
        self.loginForm = QtWidgets.QWidget(self.bottomPanel)
        self.loginForm.setGeometry(QtCore.QRect(90, 220, 631, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(350, 200))
        self.loginForm.setObjectName("loginForm")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 571, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.username.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.username.setFont(font)
        self.username.setFrame(True)
        self.username.setReadOnly(True)
        self.username.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.yes = QtWidgets.QRadioButton(self.loginForm)
        self.yes.setGeometry(QtCore.QRect(70, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.yes.setFont(font)
        self.yes.setIconSize(QtCore.QSize(16, 16))
        self.yes.setAutoExclusive(False)
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QRadioButton(self.loginForm)
        self.no.setGeometry(QtCore.QRect(70, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.no.setFont(font)
        self.no.setIconSize(QtCore.QSize(16, 16))
        self.no.setCheckable(True)
        self.no.setAutoExclusive(False)
        self.no.setObjectName("no")
        self.submit = QtWidgets.QPushButton(self.loginForm)
        self.submit.setGeometry(QtCore.QRect(270, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.bottomPanel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 801, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.logo.setFont(font)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/cc.png"))
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.restart = QtWidgets.QPushButton(self.bottomPanel)
        self.restart.setGeometry(QtCore.QRect(10, 480, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.restart.setFont(font)
        self.restart.setObjectName("restart")
        self.quit = QtWidgets.QPushButton(self.bottomPanel)
        self.quit.setGeometry(QtCore.QRect(710, 480, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.quit.setFont(font)
        self.quit.setObjectName("quit")

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Chatbot"))
        self.label.setText(_translate("Form1", "Welcome To Medical HelpLine"))
        self.label_2.setText(_translate("Form1", "Question:"))
        self.username.setText(_translate("Form1", "https://www.google.com"))
        self.yes.setText(_translate("Form1", "Yes"))
        self.no.setText(_translate("Form1", "No"))
        self.submit.setText(_translate("Form1", "Submit"))
        self.restart.setText(_translate("Form1", "Restart"))
        self.quit.setText(_translate("Form1", "Quit"))

