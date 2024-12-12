import os
import string

from PyQt6.QtWidgets import QFileDialog
fd = QFileDialog()

class FileMethod:

    def getFilepathAsString(self):
        return fd.getOpenFileName()

    def loadCsvFromFilepath(self, filepath: string):
        if filepath[0] and os.listdir().isfile(filepath[0]):
            with open(filepath[0], 'r') as file:
                if file.name.lower().endswith('.csv'):
                    return file