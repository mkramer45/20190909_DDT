# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DDTTextGen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_DaleDanT_TextGen(object):
    def setupUi(self, DaleDanT_TextGen):
        DaleDanT_TextGen.setObjectName("DaleDanT_TextGen")
        DaleDanT_TextGen.resize(925, 873)
        self.label = QtWidgets.QLabel(DaleDanT_TextGen)
        self.label.setGeometry(QtCore.QRect(290, 140, 381, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("DD_Small.PNG"))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DaleDanT_TextGen)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 470, 261, 81))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(DaleDanT_TextGen)
        self.pushButton.setGeometry(QtCore.QRect(400, 580, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(DaleDanT_TextGen)
        self.label_2.setGeometry(QtCore.QRect(310, 450, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DaleDanT_TextGen)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 531, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(DaleDanT_TextGen)
        self.textEdit.setGeometry(QtCore.QRect(310, 700, 261, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(DaleDanT_TextGen)
        self.label_4.setGeometry(QtCore.QRect(310, 680, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(DaleDanT_TextGen)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 820, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(DaleDanT_TextGen)
        QtCore.QMetaObject.connectSlotsByName(DaleDanT_TextGen)

        self.pushButton_2.clicked.connect(self.show_popup)

    def retranslateUi(self, DaleDanT_TextGen):
        _translate = QtCore.QCoreApplication.translate
        DaleDanT_TextGen.setWindowTitle(_translate("DaleDanT_TextGen", "Dialog"))
        self.pushButton.setText(_translate("DaleDanT_TextGen", "Generate Text!"))
        self.label_2.setText(_translate("DaleDanT_TextGen", "Enter Your Text:"))
        self.label_3.setText(_translate("DaleDanT_TextGen", "Dale Dan Tony Text Generator 9000"))
        self.label_4.setText(_translate("DaleDanT_TextGen", "Your Text:"))
        self.pushButton_2.setText(_translate("DaleDanT_TextGen", "Exit"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on how to blah blah")
        msg.setText("This is the main message blah blah!")

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DaleDanT_TextGen = QtWidgets.QDialog()
    ui = Ui_DaleDanT_TextGen()
    ui.setupUi(DaleDanT_TextGen)
    DaleDanT_TextGen.show()
    sys.exit(app.exec_())
