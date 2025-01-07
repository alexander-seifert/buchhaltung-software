import csv


class SalesModel:
    def __init__(self):
        self.sales_data = {}

    def load_csv(self, file_path):
        # Lade CSV-Daten mit spezifischer Kodierung und speichere sie
        file_name = file_path.split('/')[-1]
        with open(file_path, newline='', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            days = next(reader)  # Erste Zeile enthält die Wochentage
            if not self.sales_data:
                self.sales_data = {day.strip(): [] for day in days}
            for row in reader:
                for day, value in zip(days, row):
                    cleaned_value = (
                        value.replace('\x80', '')
                        .replace('.', '')  # Entferne Tausendertrennzeichen
                        .replace(',', '.')  # Ersetze Dezimaltrennzeichen
                        .strip()
                    )
                    try:
                        if cleaned_value:
                            self.sales_data[day.strip()].append((file_name, float(cleaned_value)))
                    except ValueError:
                        raise ValueError(f"Ungültiges Zahlenformat: {value}")

    def get_sorted_sales(self):
        # Sortiere die Umsätze jeder Filiale pro Tag alphabetisch nach Filialnamen
        sorted_data = {}
        for day, values in self.sales_data.items():
            sorted_data[day] = sorted(values, key=lambda x: x[0])
        return sorted_data

    def get_overview(self):
        # Übersicht, welche Filialen an wie vielen Tagen die höchsten Einnahmen hatten
        overview = {}
        for day, sales in self.get_sorted_sales().items():
            top_filiale = max(sales, key=lambda x: x[1])
            if top_filiale[0] not in overview:
                overview[top_filiale[0]] = 0
            overview[top_filiale[0]] += 1
        return overview
