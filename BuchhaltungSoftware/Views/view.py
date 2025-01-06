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

        self.file_button = tk.Button(button_frame, text="Datei auswählen", command=self.load_file)
        self.file_button.pack(pady=5)

        self.delete_button = tk.Button(button_frame, text="Datei löschen", command=self.delete_file)
        self.delete_button.pack(pady=5)

        self.analyze_console_button = tk.Button(button_frame, text="In Konsole analysieren", command=self.analyze_console)
        self.analyze_console_button.pack(pady=5)

        self.analyze_window_button = tk.Button(button_frame, text="Im Fenster analysieren", command=self.analyze_window)
        self.analyze_window_button.pack(pady=5)

    def load_file(self):
        # Open file dialog and load file
        file_paths = filedialog.askopenfilenames(filetypes=[("CSV-Dateien", "*.csv")])
        if file_paths:
            for file_path in file_paths:
                self.file_listbox.insert(tk.END, file_path)
                try:
                    self.view_model.load_file(file_path)
                    messagebox.showinfo("Erfolg", f"Datei {file_path} erfolgreich geladen!")
                except ValueError as e:
                    messagebox.showerror("Fehler", f"Fehler beim Laden der Datei {file_path}: {e}")

    def delete_file(self):
        # Loesche die ausgewaehlte Datei in der Listbox und im ViewModel
        selected_indices = self.file_listbox.curselection()
        for index in selected_indices[::-1]:
            self.file_listbox.delete(index)
            self.view_model.removeFile(index)

    def analyze_console(self):
        # Analysieren und Ergebnis in der Konsole anzeigen
        self.view_model.analyze_sales()
        print("Sortierte Umsätze:")
        for day, sales in self.view_model.sorted_sales.items():
            print(f"{day}: {sales}")
        print("\nTop-Filialen:")
        for day, (index, value) in self.view_model.top_filialen.items():
            print(f"{day}: Filiale {index + 1} mit Umsatz {value}")

    def analyze_window(self):
        # Analysieren und Ergebnis im Fenster anzeigen
        self.view_model.analyze_sales()
        result_window = tk.Toplevel(self.root)
        result_window.title("Analyseergebnisse")

        tk.Label(result_window, text="Sortierte Umsätze:").pack()
        for day, sales in self.view_model.sorted_sales.items():
            tk.Label(result_window, text=f"{day}: {sales}").pack()

        tk.Label(result_window, text="\nTop-Filialen:").pack()
        for day, (index, value) in self.view_model.top_filialen.items():
            tk.Label(result_window, text=f"{day}: Filiale {index + 1} mit Umsatz {value}").pack()