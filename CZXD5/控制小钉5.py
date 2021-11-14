# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 422)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Python Learning\\CZXD5\\background.jpeg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 161, 51))
        self.label_2.setStyleSheet("color:pink;\n"
                                   "font-family:微软雅黑;\n"
                                   "font-size:26px;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 100, 511, 41))
        self.lineEdit.setStyleSheet("background-color:skyblue;\n"
                                    "font-family:微软雅黑;\n"
                                    "font-color:pink;\n"
                                    "font-size:24px;")
        self.lineEdit.setMaxLength(1000)
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(30, 162, 481, 41))
        self.progressBar.setStyleSheet("font-size:30px;\n"
                                       "font-family:微软雅黑;\n"
                                       "color:pink;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Send = QtWidgets.QPushButton(Form)
        self.Send.setGeometry(QtCore.QRect(90, 290, 341, 111))
        self.Send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Send.setMouseTracking(True)
        self.Send.setStyleSheet("font-family:楷体;\n"
                                "font-size:60px;\n"
                                "background-color:darkblue;\n"
                                "font-color:white;\n"
                                "QPushButton{\n"
                                "\n"
                                "background-color:transparent;\n"
                                "\n"
                                "border:1px solid black;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "\n"
                                "              opacity:0.2;\n"
                                "\n"
                                "              border:2px solid black;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed{\n"
                                "\n"
                                "background-color:transparent;\n"
                                "\n"
                                "border:1px solid black;\n"
                                "\n"
                                "}\n"
                                "")
        self.Send.setObjectName("Send")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 390, 54, 12))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "控制小钉5.0"))
        self.label_2.setText(_translate("Form", "控制小钉5.0"))
        self.lineEdit.setPlaceholderText("请输入你要发送的消息")
        self.Send.setText(_translate("Form", "点击发送"))
        self.label_3.setText(_translate("Form", "By Wdq"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
