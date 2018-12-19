# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\02_button_clicked.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 50, 231, 181))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_phonenumber = QtWidgets.QLabel(self.widget)
        self.label_phonenumber.setObjectName("label_phonenumber")
        self.gridLayout_2.addWidget(self.label_phonenumber, 1, 0, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout_2.addWidget(self.lineEdit_phone, 1, 1, 1, 1)
        self.label_email = QtWidgets.QLabel(self.widget)
        self.label_email.setObjectName("label_email")
        self.gridLayout_2.addWidget(self.label_email, 2, 0, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_2.addWidget(self.lineEdit_email, 2, 1, 1, 1)
        self.label_company = QtWidgets.QLabel(self.widget)
        self.label_company.setObjectName("label_company")
        self.gridLayout_2.addWidget(self.label_company, 3, 0, 1, 1)
        self.lineEdit_company = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.gridLayout_2.addWidget(self.lineEdit_company, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.print_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "close"))
        self.pushButton_2.setText(_translate("MainWindow", "print"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_phonenumber.setText(_translate("MainWindow", "电话"))
        self.label_email.setText(_translate("MainWindow", "邮箱"))
        self.label_company.setText(_translate("MainWindow", "公司"))

    def print_text(self):
        print("姓名:%s" % self.lineEdit_name.text())
        print("电话:%s" % self.lineEdit_phone.text())
        print("邮箱:%s" % self.lineEdit_email.text())
        print("公司:%s" % self.lineEdit_company.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
