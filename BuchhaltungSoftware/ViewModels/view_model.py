# view_model.py
from Models.model import SalesModel

class SalesViewModel:
    def __init__(self):
        self.model = SalesModel()
        self.sales_data = {}
        self.sorted_sales = {}
        self.top_filialen = {}

    def load_file(self, file_path):
        # Lädt die Datei und aktualisiert die Daten
        try:
            self.model.load_csv(file_path)
            self.sales_data = self.model.sales_data
        except UnicodeDecodeError:
            raise ValueError("Die Datei ist nicht im erwarteten Format. Bitte überprüfen Sie die Kodierung.")

    def analyze_sales(self):
       # Analysiert die Verkäufe und aktualisiert die ViewModel-Daten
        self.sorted_sales = self.model.get_sorted_sales()
        self.top_filialen = self.model.get_top_filialen()