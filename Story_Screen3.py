# Form implementation generated from reading ui file 'Story_Screen3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_s_header3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_s_header3.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_s_header3.setFont(font)
        self.label_s_header3.setObjectName("label_s_header3")
        self.label_s_select_story = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_s_select_story.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_s_select_story.setFont(font)
        self.label_s_select_story.setObjectName("label_s_select_story")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 170, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.button_s_finish = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_s_finish.setGeometry(QtCore.QRect(110, 370, 75, 23))
        self.button_s_finish.setObjectName("button_s_finish")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_s_header3.setText(_translate("MainWindow", "View Entries"))
        self.label_s_select_story.setText(_translate("MainWindow", "Select Story:"))
        self.button_s_finish.setText(_translate("MainWindow", "Finish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())