# view.py
import tkinter as tk
from tkinter import filedialog, messagebox
from ViewModels.view_model import SalesViewModel


class SalesView:
    def __init__(self, root):
        self.root = root
        self.view_model = SalesViewModel()

        # UI erstellen
        self.file_label = tk.Label(root, text="Keine Datei ausgewählt")
        self.file_label.pack()

        self.file_button = tk.Button(root, text="Datei auswählen", command=self.load_file)
        self.file_button.pack()

        self.analyze_console_button = tk.Button(root, text="In Konsole analysieren", command=self.analyze_console)
        self.analyze_console_button.pack()

        self.analyze_window_button = tk.Button(root, text="Im Fenster analysieren", command=self.analyze_window)
        self.analyze_window_button.pack()

    def load_file(self):
        """Dateiauswahl-Dialog öffnen und Datei laden."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV-Dateien", "*.csv")])
        if file_path:
            self.file_label.config(text=file_path)
            try:
                self.view_model.load_file(file_path)
                messagebox.showinfo("Erfolg", "Datei erfolgreich geladen!")
            except ValueError as e:
                messagebox.showerror("Fehler", str(e))
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Laden der Datei: {e}")

    def analyze_console(self):
        """Analysieren und Ergebnis in der Konsole anzeigen."""
        self.view_model.analyze_sales()
        print("Sortierte Umsätze:")
        for day, sales in self.view_model.sorted_sales.items():
            print(f"{day}: {sales}")
        print("\nTop-Filialen:")
        for day, (index, value) in self.view_model.top_filialen.items():
            print(f"{day}: Filiale {index + 1} mit Umsatz {value}")

    def analyze_window(self):
        """Analysieren und Ergebnis im Fenster anzeigen."""
        self.view_model.analyze_sales()
        result_window = tk.Toplevel(self.root)
        result_window.title("Analyseergebnisse")

        tk.Label(result_window, text="Sortierte Umsätze:").pack()
        for day, sales in self.view_model.sorted_sales.items():
            tk.Label(result_window, text=f"{day}: {sales}").pack()

        tk.Label(result_window, text="\nTop-Filialen:").pack()
        for day, (index, value) in self.view_model.top_filialen.items():
            tk.Label(result_window, text=f"{day}: Filiale {index + 1} mit Umsatz {value}").pack()