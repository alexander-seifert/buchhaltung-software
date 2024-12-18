# mainview.py
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 244)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lvCsvFiles = QtWidgets.QListView(parent=self.centralwidget)
        self.lvCsvFiles.setGeometry(QtCore.QRect(30, 20, 220, 110))
        self.lvCsvFiles.setObjectName("lvCsvFiles")
        self.btnAddFiles = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAddFiles.setGeometry(QtCore.QRect(270, 30, 120, 40))
        self.btnAddFiles.setObjectName("btnAddFiles")
        self.btnDeleteFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDeleteFile.setGeometry(QtCore.QRect(270, 80, 120, 40))
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.btnResultView = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnResultView.setGeometry(QtCore.QRect(40, 150, 160, 40))
        self.btnResultView.setObjectName("btnResultView")
        self.btnResultConsole = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnResultConsole.setGeometry(QtCore.QRect(220, 150, 160, 40))
        self.btnResultConsole.setObjectName("btnResultConsole")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Umsatzauswertung"))
        self.btnAddFiles.setText(_translate("MainWindow", "Hinzufügen"))
        self.btnDeleteFile.setText(_translate("MainWindow", "Löschen"))
        self.btnResultView.setText(_translate("MainWindow", "Ergebnisse im Fenster"))
        self.btnResultConsole.setText(_translate("MainWindow", "Ergebnisse in Konsole"))
