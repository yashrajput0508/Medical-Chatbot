# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registeration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 600)
        Form.setStyleSheet("#topPanel { \n"
"background-image: url(images/bc3.jpg);}\n"
"\n"
"#signup{color: white;}\n"
"\n"
"#loginForm\n"
"{\n"
"  background: rgba(0, 0, 0, 80);\n"
"  border-radius: 8px;\n"
"}\n"
"QLabel { color: white; }\n"
"QLineEdit { border-radius: 3px; }\n"
"QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton:hover{background-color:lightblue;}\n"
"#chatbot{color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));}\n"
"#info{color:red;}")
        self.topPanel = QtWidgets.QWidget(Form)
        self.topPanel.setGeometry(QtCore.QRect(0, 0, 811, 600))
        self.topPanel.setObjectName("topPanel")
        self.signup = QtWidgets.QLabel(self.topPanel)
        self.signup.setGeometry(QtCore.QRect(0, 10, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(46)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setAlignment(QtCore.Qt.AlignCenter)
        self.signup.setObjectName("signup")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.topPanel)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 280, 801, 291))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginForm = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(350, 200))
        self.loginForm.setObjectName("loginForm")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 301, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.username.setMinimumSize(QtCore.QSize(0, 0))
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(30, 70, 301, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(46, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.emailid_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.emailid_2.setClearButtonEnabled(True)
        self.emailid_2.setObjectName("emailid_2")
        self.horizontalLayout_12.addWidget(self.emailid_2)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 110, 301, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.contactnumber = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.contactnumber.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.contactnumber.setClearButtonEnabled(True)
        self.contactnumber.setObjectName("contactnumber")
        self.horizontalLayout_7.addWidget(self.contactnumber)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 150, 301, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.loginForm)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 190, 301, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.password_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.password_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_7.setClearButtonEnabled(True)
        self.password_7.setObjectName("password_7")
        self.horizontalLayout_13.addWidget(self.password_7)
        self.Register = QtWidgets.QPushButton(self.loginForm)
        self.Register.setGeometry(QtCore.QRect(30, 240, 301, 31))
        self.Register.setCheckable(False)
        self.Register.setAutoDefault(False)
        self.Register.setFlat(False)
        self.Register.setObjectName("Register")
        self.horizontalLayout_2.addWidget(self.loginForm)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.topPanel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 801, 171))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registeration"))
        self.signup.setText(_translate("Form", "Register"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_10.setText(_translate("Form", "Email ID:"))
        self.label_5.setText(_translate("Form", "Contact No:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.label_11.setText(_translate("Form", "Confirm Password:"))
        self.Register.setText(_translate("Form", "Register"))

