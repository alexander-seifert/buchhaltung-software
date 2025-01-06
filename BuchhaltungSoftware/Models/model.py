# model.py
import csv


class SalesModel:
    def __init__(self):
        self.sales_data = {}

    def load_csv(self, file_path):
        """Lade CSV-Daten mit spezifischer Kodierung und speichere sie."""
        with open(file_path, newline='', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            days = next(reader)  # Erste Zeile enthält die Wochentage
            self.sales_data = {day.strip(): [] for day in days}

            for row in reader:
                for day, value in zip(days, row):
                    cleaned_value = (
                        value.replace('€', '')
                             .replace('.', '')  # Entferne Tausendertrennzeichen
                             .replace(',', '.')  # Ersetze Dezimaltrennzeichen
                             .strip()
                    )
                    try:
                        if cleaned_value:
                            self.sales_data[day.strip()].append(float(cleaned_value))
                    except ValueError:
                        raise ValueError(f"Ungültiges Zahlenformat: {value}")

    def get_sorted_sales(self):
        """Gibt eine sortierte Liste der Einnahmen pro Tag zurück."""
        sorted_data = {}
        for day, values in self.sales_data.items():
            sorted_data[day] = sorted(values, reverse=True)
        return sorted_data

    def get_top_filialen(self):
        """Ermittelt die umsatzstärkste Filiale für jeden Wochentag."""
        top_filialen = {}
        for day, values in self.sales_data.items():
            max_value = max(values)
            top_filialen[day] = (values.index(max_value), max_value)
        return top_filialen
