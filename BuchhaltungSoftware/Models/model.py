import os
import pandas as pd
from PyQt6.QtWidgets import QFileDialog

class FileModel:
    def __init__(self):
        self.fd = QFileDialog()

    def getFilepathAsString(self):
        return self.fd.getOpenFileName()

    def loadCsvFromFilepath(self, filepath: str):
        if filepath and os.path.isfile(filepath):
            if filepath.lower().endswith('.csv'):
                df = pd.read_csv(filepath, encoding='latin1')
                print(f"Spalten in {filepath}: {df.columns.tolist()}")  # Debug-Ausgabe
                return df
