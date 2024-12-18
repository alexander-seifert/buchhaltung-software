import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import QtGui
from Views.mainview import Ui_MainWindow
from Views.resultview import Ui_ResultWindow
from Views.viewmodel import ViewModel


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.viewModel = ViewModel()
        self.viewModel.filesChanged.connect(self.updateFileList)
        self.viewModel.resultsChanged.connect(self.showResults)

        self.ui.btnAddFiles.clicked.connect(self.addFiles)
        self.ui.btnDeleteFile.clicked.connect(self.deleteFile)
        self.ui.btnResultView.clicked.connect(self.showResultWindow)
        self.ui.btnResultConsole.clicked.connect(self.printResultsToConsole)

    def addFiles(self):
        try:
            files, _ = QFileDialog.getOpenFileNames(self, "Select CSV Files", "", "CSV Files (*.csv)")
            print("Selected files:", files)  # Debug-Ausgabe
            if files:
                for file in files:
                    self.viewModel.addFile(file)
            else:
                print("No files selected")  # Debug-Ausgabe
        except Exception as e:
            print("Error in addFiles:", e)  # Debug-Ausgabe

    def deleteFile(self):
        index = self.ui.lvCsvFiles.currentIndex()
        if index.isValid():
            filepath = self.viewModel.files[index.row()]
            self.viewModel.removeFile(filepath)

    def updateFileList(self, files):
        model = QtGui.QStandardItemModel()
        for file in files:
            item = QtGui.QStandardItem(file)
            model.appendRow(item)
        self.ui.lvCsvFiles.setModel(model)

    def showResults(self):
        try:
            resultWindow = QMainWindow()
            ui = Ui_ResultWindow()
            ui.setupUi(resultWindow)
            self.viewModel.calculateResults()
            # Debug
            print("Results:", self.viewModel.getResultsForConsole())
            resultWindow.show()
        except Exception as e:
            print("Error in showResults:", e)  # Debug

    def printResultsToConsole(self):
        results = self.viewModel.getResultsForConsole()
        print(results)

    def showResultWindow(self):
        self.showResults()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec())
