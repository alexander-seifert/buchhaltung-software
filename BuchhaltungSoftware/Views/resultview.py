# Form implementation generated from reading ui file 'resultview.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(419, 327)
        self.centralwidget = QtWidgets.QWidget(parent=ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblName = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(150, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblName.setFont(font)
        self.lblName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.lvResults = QtWidgets.QListView(parent=self.centralwidget)
        self.lvResults.setGeometry(QtCore.QRect(40, 70, 340, 220))
        self.lvResults.setObjectName("lvResults")
        self.btnNextDay = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnNextDay.setGeometry(QtCore.QRect(320, 30, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnNextDay.setFont(font)
        self.btnNextDay.setAutoFillBackground(False)
        self.btnNextDay.setObjectName("btnNextDay")
        self.btnPreviousDay = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnPreviousDay.setGeometry(QtCore.QRect(40, 30, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnPreviousDay.setFont(font)
        self.btnPreviousDay.setObjectName("btnPreviousDay")
        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Ergebnisfenster"))
        self.lblName.setText(_translate("ResultWindow", "Montag"))
        self.btnNextDay.setText(_translate("ResultWindow", ">"))
        self.btnPreviousDay.setText(_translate("ResultWindow", "<"))
