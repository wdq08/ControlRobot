# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Learning\CZXD\CZXD5\CZXD5.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
import json


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("控制小钉5.3")
        Form.resize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bkgd.jpeg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 201, 41))
        self.label_2.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:36px;\n"
                                   "color:skyblue;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 179, 601, 61))
        self.lineEdit.setStyleSheet("background-color:skyblue;\n"
                                    "font-family:微软雅黑;\n"
                                    "font-size:36px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 360, 151, 71))
        self.pushButton.setStyleSheet("background-color:skyblue;\n"
                                      "color:blue;\n"
                                      "font-family:微软雅黑;\n"
                                      "font-size:36px;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(500, 420, 54, 12))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(lambda: send(self.lineEdit.text()))  # type: ignore
        self.pushButton.released.connect(self.lineEdit.selectAll)  # type: ignore
        self.lineEdit.editingFinished.connect(self.pushButton.click)  # type: ignore
        self.pushButton.pressed.connect(self.lineEdit.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "控制小钉5.3"))
        self.label_2.setText(_translate("Form", "控制小钉5.3"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请在这里输入要发送的文字"))
        self.pushButton.setText(_translate("Form", "发送"))
        self.label_3.setText(_translate("Form", "By Wdq"))

def send(var):
    url = "https://oapi.dingtalk.com/robot/send?access_token=fd70752caa12ac7be000218d355c2baa8d90ed79a0e2dbe2a5a87ab3ccf540ff"
    text = (var + ".")
    if len(text) < 2:
        return 0
    program = {
        "isAtAll": "true",
        "msgtype": "text",
        "text": {"content": text},
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
