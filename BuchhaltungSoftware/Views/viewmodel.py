import os
import pandas as pd
from PyQt6.QtCore import QObject, pyqtSignal
from Models.model import FileModel


class ViewModel(QObject):
    filesChanged = pyqtSignal(list)
    resultsChanged = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        self.model = FileModel()
        self.files = []
        self.results = pd.DataFrame()

    def addFile(self, filepath):
        if filepath and os.path.isfile(filepath):
            self.files.append(filepath)
            self.filesChanged.emit(self.files)

    def removeFile(self, filepath):
        if filepath in self.files:
            self.files.remove(filepath)
            self.filesChanged.emit(self.files)

    def calculateResults(self):
        all_data = []
        for file in self.files:
            data = self.model.loadCsvFromFilepath(file)
            print(f"Verarbeite Datei: {file}, Spalten: {data.columns.tolist()}")  # Debug-Ausgabe
            all_data.append(data)
        if all_data:
            combined_data = pd.concat(all_data, ignore_index=True)
            combined_data['Filiale'] = combined_data.index + 1  # Annahme: Jede Zeile ist eine Filiale
            combined_data = combined_data.melt(id_vars='Filiale', var_name='Tag', value_name='Einnahmen')
            print(f"Kombinierte Daten: {combined_data.head()}")  # Debug-Ausgabe
            try:
                # Nur die Daten von Montag bis Samstag berücksichtigen
                self.results = combined_data[combined_data['Tag'].isin(['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'])]
                self.results = self.results.groupby('Filiale').sum().sort_values('Einnahmen', ascending=False).reset_index()
                self.resultsChanged.emit(self.results)
            except KeyError as e:
                print(f"Fehlender Spaltenname: {e}")  # Debug-Ausgabe

    def getResultsForConsole(self):
        return self.results
