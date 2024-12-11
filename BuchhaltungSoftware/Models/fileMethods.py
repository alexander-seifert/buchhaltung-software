import os
import string

from PyQt6.QtWidgets import QFileDialog
fd = QFileDialog()

def getFilepathAsString():
    return fd.getOpenFileName()

def loadFileFromFilepath(filepath: string):
        if filepath[0] and os.path.isfile(filepath[0]):
            with open(filepath[0], 'r') as file:
                return file.read()