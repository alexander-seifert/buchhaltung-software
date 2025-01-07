import tkinter as tk
from tkinter import filedialog, messagebox
from ViewModels.view_model import SalesViewModel


class SalesView:
    def __init__(self, root):
        self.root = root
        self.view_model = SalesViewModel()

        # UI erstellen
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.file_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        button_frame = tk.Frame(frame)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)
        button_width = 20

        self.file_button = tk.Button(button_frame, text="Datei auswählen", command=self.load_file, width=button_width)
        self.file_button.pack(pady=5)

        self.delete_button = tk.Button(button_frame, text="Datei löschen", command=self.delete_file, width=button_width)
        self.delete_button.pack(pady=5)

        self.analyze_console_button = tk.Button(button_frame, text="In Konsole ausgeben", command=self.analyze_console, width=button_width)
        self.analyze_console_button.pack(pady=5)

        self.analyze_window_button = tk.Button(button_frame, text="Im Fenster ausgeben", command=self.analyze_window, width=button_width)
        self.analyze_window_button.pack(pady=5)

    def load_file(self):
        # Dateidialog oeffnen und Dateien auswaehlen
        file_paths = filedialog.askopenfilenames(filetypes=[("CSV-Dateien", "*.csv")])
        if file_paths:
            for file_path in file_paths:
                self.file_listbox.insert(tk.END, file_path)
                self.load_file_from_path(file_path)

    def load_file_from_path(self, file_path):
        try:
            self.view_model.load_file(file_path)
        except ValueError as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden der Datei {file_path}: {e}")

    def delete_file(self):
        # Loesche die ausgewaehlte Datei in der Listbox und im ViewModel
        selected_indices = self.file_listbox.curselection()
        for index in selected_indices[::-1]:
            self.file_listbox.delete(index)
            self.view_model.sales_data.clear()

        # Uebrig gebliebene Dateien neu laden
        for file_path in self.file_listbox.get(0, tk.END):
            self.load_file_from_path(file_path)

    def analyze_console(self):
        # Analysieren und Ergebnis in der Konsole anzeigen
        self.view_model.analyze_sales()
        print("Top-Filialen pro Tag:")
        for day, sales in self.view_model.sorted_sales.items():
            top_filiale = max(sales, key=lambda x: x[1])
            print(f"{day}: {top_filiale[0]} mit Umsatz {top_filiale[1]:.2f}")
        print("\nÜbersicht der umsatzstärksten Filialen:")
        for filiale, count in self.view_model.overview.items():
            print(f"{filiale}: {count} Tage")

    def analyze_window(self):
        # Analysieren und Ergebnis im Fenster anzeigen
        self.view_model.analyze_sales()
        result_window = tk.Toplevel(self.root)
        result_window.title("Analyseergebnisse")
        result_window.resizable(False, False)

        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
        for i, day in enumerate(days):
             tk.Label(result_window, text=day, font=('Arial', 15, 'bold')).grid(row=0, column=i, padx=10, pady=5)
    
        for i, (day, sales) in enumerate(self.view_model.sorted_sales.items()):
            top_filiale = max(sales, key=lambda x: x[1])
            for j, (file_name, value) in enumerate(sales):
                color = 'green' if (file_name, value) == top_filiale else 'black'
                filialenname = file_name.split('.')[0]
                tk.Label(result_window, text=f"{filialenname}: {value:.2f}", font=('Arial', 12, 'bold'), fg=color).grid(row=j+1, column=i, padx=10, pady=5)
